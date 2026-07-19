import { useEffect, useRef, useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

const API = import.meta.env.VITE_API_URL || "http://localhost:8000";

const REPLAY_SPEED = 6;
const REPLAY_MAX_GAP_MS = 1200;

// Preset texts must stay EXACTLY in sync with record_demo.py.
const PRESETS = [
  {
    slug: "battery-supplier-swap",
    label: "Battery supplier swap",
    text: "Change the primary battery supplier from Samsung SDI to LG Energy Solution. Assess the impact on certification timeline, unit cost, and supply chain risk.",
  },
  {
    slug: "first-flight-delay",
    label: "First Flight delay",
    text: "Delay First Flight by 6 months due to autonomy software certification issues. Assess impact on program cost, customer deliveries, and risk posture.",
  },
  {
    slug: "titanium-rotor-hub",
    label: "Titanium rotor hub",
    text: "Replace the aluminum main rotor hub with a titanium design to improve fatigue life. Assess impact on weight, cost, qualification testing, and the manufacturing ramp.",
  },
  {
    slug: "flight-computer-shortage",
    label: "Flight computer shortage",
    text: "The flight computer supplier has notified the program of a 12-month semiconductor allocation shortage affecting IMA core processor deliveries. Assess impact on production continuity, schedule, buffer stock strategy, and program risk.",
  },
  {
    slug: "production-rate-increase",
    label: "Rate increase to 6/yr",
    text: "Accelerate the production ramp from 2 to 6 aircraft per year beginning in LRIP-2 to meet growing wildfire fleet demand. Assess impact on manufacturing readiness, supply chain capacity, cost, and quality.",
  },
  {
    slug: "cargo-fleet-order",
    label: "Cargo fleet order",
    text: "A new customer has placed an order for 15 additional cargo variant aircraft with deliveries beginning 2029. Assess impact on the production schedule, supply chain, financials, and program risk.",
  },
];

const AGENT_ORDER = [
  "change_impact",
  "cost_margin",
  "manufacturing",
  "supply_chain",
  "risk_schedule",
];

const PHASES = [
  { id: "warmup", label: "Knowledge base" },
  { id: "agents", label: "Specialist agents" },
  { id: "documents", label: "Document impacts" },
  { id: "synthesis", label: "PMP synthesis" },
];

function docShortName(fileName) {
  return fileName.replace(/^maap1_/, "").replace(/\.md$/, "").replace(/_/g, " ");
}

function formatElapsed(seconds) {
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

export default function AriaTool() {
  const [change, setChange] = useState("");
  const [accessCode, setAccessCode] = useState("");
  const [status, setStatus] = useState("idle");
  const [mode, setMode] = useState(null);
  const [phase, setPhase] = useState(null);
  const [agents, setAgents] = useState({});
  const [documents, setDocuments] = useState([]);
  const [pmp, setPmp] = useState("");
  const [errorMsg, setErrorMsg] = useState("");
  const [elapsed, setElapsed] = useState(0);

  const pendingTokens = useRef("");
  const flushTimer = useRef(null);
  const sheetRef = useRef(null);
  const timerRef = useRef(null);

  useEffect(() => {
    if (status === "running") {
      timerRef.current = setInterval(() => setElapsed((e) => e + 1), 1000);
    }
    return () => clearInterval(timerRef.current);
  }, [status]);

  useEffect(() => {
    if (status === "running" && sheetRef.current) {
      sheetRef.current.scrollTop = sheetRef.current.scrollHeight;
    }
  }, [pmp, status]);

  function queueTokens(text) {
    pendingTokens.current += text;
    if (!flushTimer.current) {
      flushTimer.current = setTimeout(() => {
        setPmp((p) => p + pendingTokens.current);
        pendingTokens.current = "";
        flushTimer.current = null;
      }, 150);
    }
  }

  function handleEvent(evt) {
    switch (evt.type) {
      case "phase":
        setPhase(evt.phase);
        break;
      case "agent_started":
        setAgents((a) => ({
          ...a,
          [evt.agent]: { label: evt.label, state: "running", preview: "" },
        }));
        break;
      case "agent_completed":
        setAgents((a) => ({
          ...a,
          [evt.agent]: { label: evt.label, state: "complete", preview: evt.preview },
        }));
        break;
      case "documents_identified":
        setDocuments(evt.documents.map((d) => ({ name: d, state: "queued" })));
        break;
      case "document_completed":
        setDocuments((docs) =>
          docs.map((d) => (d.name === evt.document ? { ...d, state: "assessed" } : d))
        );
        break;
      case "synthesis_token":
        queueTokens(evt.text);
        break;
      case "done":
        clearTimeout(flushTimer.current);
        flushTimer.current = null;
        pendingTokens.current = "";
        setPmp(evt.pmp);
        setStatus("done");
        break;
      case "error":
        setErrorMsg(evt.message || "The analysis stopped unexpectedly.");
        setStatus("error");
        break;
      default:
        break;
    }
  }

  function resetRun() {
    setPhase(null);
    setAgents({});
    setDocuments([]);
    setPmp("");
    setErrorMsg("");
    setElapsed(0);
  }

  async function tryReplay(text) {
    const preset = PRESETS.find((p) => p.text === text);
    if (!preset) return false;

    let recording;
    try {
      const res = await fetch(`/demos/${preset.slug}.json`);
      if (!res.ok) return false;
      recording = await res.json();
    } catch {
      return false;
    }

    setMode("replay");
    setStatus("running");
    resetRun();

    let prevT = 0;
    for (const { t, event } of recording.events) {
      const gapMs = Math.min(((t - prevT) * 1000) / REPLAY_SPEED, REPLAY_MAX_GAP_MS);
      prevT = t;
      if (gapMs > 0) await sleep(gapMs);
      handleEvent(event);
    }
    return true;
  }

  async function runLive(text) {
    setMode("live");
    setStatus("running");
    resetRun();

    try {
      const res = await fetch(`${API}/api/analyze`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-Access-Code": accessCode,
        },
        body: JSON.stringify({ change_description: text }),
      });
      if (res.status === 401) {
        throw new Error(
          "custom changes run a live analysis, which needs an access code. Pick a preset scenario, or enter a valid code."
        );
      }
      if (!res.ok || !res.body) {
        throw new Error(`Server responded ${res.status}`);
      }

      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const frames = buffer.split("\n\n");
        buffer = frames.pop();
        for (const frame of frames) {
          const line = frame.trim();
          if (!line.startsWith("data:")) continue;
          try {
            handleEvent(JSON.parse(line.slice(5).trim()));
          } catch {
            // ignore malformed frame
          }
        }
      }
    } catch (err) {
      setErrorMsg(String(err.message || err));
      setStatus("error");
    }
  }

  async function runAnalysis() {
    const text = change.trim();
    if (!text || status === "running") return;
    const replayed = await tryReplay(text);
    if (!replayed) {
      await runLive(text);
    }
  }

  function downloadPmp() {
    const blob = new Blob([pmp], { type: "text/markdown" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "PMP_Update_MAAP-1.md";
    a.click();
    URL.revokeObjectURL(url);
  }

  const statusStamp =
    status === "running" ? "ANALYZING" : status === "done" ? "DRAFT COMPLETE" : status === "error" ? "HALTED" : "STANDBY";

  const showBoard = status !== "idle";

  return (
    <div className="tool">
      <header className="titleblock">
        <div className="tb-cell tb-brand">
          <span className="tb-name">Impact Console</span>
          <span className="tb-sub">MAAP-1 live analysis environment</span>
        </div>
        <div className="tb-cell">
          <span className="tb-key">Program</span>
          <span className="tb-val">MAAP-1</span>
        </div>
        <div className="tb-cell">
          <span className="tb-key">Document</span>
          <span className="tb-val">PMP Update</span>
        </div>
        <div className="tb-cell">
          <span className="tb-key">Elapsed</span>
          <span className="tb-val mono">{formatElapsed(elapsed)}</span>
        </div>
        <div className={`tb-cell tb-stamp stamp-${status}`}>
          <span>{statusStamp}</span>
        </div>
      </header>

      <section className="intake">
        <label className="eyebrow" htmlFor="change">
          Proposed engineering change
        </label>
        <textarea
          id="change"
          value={change}
          onChange={(e) => setChange(e.target.value)}
          maxLength={2000}
          rows={3}
          placeholder="Describe a change to the MAAP-1 heavy-lift autonomous helicopter program — a supplier swap, a schedule slip, a design change…"
          disabled={status === "running"}
        />
        <div className="intake-row">
          <div className="presets">
            {PRESETS.map((p) => (
              <button
                key={p.slug}
                className="chip"
                onClick={() => setChange(p.text)}
                disabled={status === "running"}
              >
                {p.label}
              </button>
            ))}
          </div>
          <div className="run-group">
            <input
              className="code-input"
              type="password"
              value={accessCode}
              onChange={(e) => setAccessCode(e.target.value)}
              placeholder="Access code (live runs)"
              disabled={status === "running"}
              aria-label="Access code for live runs"
            />
            <button
              className="run"
              onClick={runAnalysis}
              disabled={status === "running" || !change.trim()}
            >
              {status === "running" ? "Analysis in progress" : "Run impact analysis"}
            </button>
          </div>
        </div>
        <p className="fineprint">
          5 specialist agents · 10 program documents · powered by Claude ·
          presets replay recorded runs, time-compressed to ~2 min · custom
          changes run the full live pipeline (~10 min) and need an access code
        </p>
        {errorMsg && <div className="errorbar">Analysis halted: {errorMsg}</div>}
      </section>

      {showBoard && (
        <main className="board">
          <aside className="left">
            <div className="phases">
              {PHASES.map((p) => {
                const idx = PHASES.findIndex((x) => x.id === phase);
                const mine = PHASES.findIndex((x) => x.id === p.id);
                const state =
                  status === "done" || mine < idx ? "past" : mine === idx ? "now" : "next";
                return (
                  <div key={p.id} className={`phase phase-${state}`}>
                    <span className="phase-dot" />
                    {p.label}
                  </div>
                );
              })}
            </div>

            <h2 className="panel-title">Specialist agents</h2>
            <div className="agents">
              {AGENT_ORDER.map((key, i) => {
                const a = agents[key];
                const state = a ? a.state : "standby";
                return (
                  <div key={key} className={`agent agent-${state}`}>
                    <div className="agent-head">
                      <span className="agent-id mono">A-{String(i + 1).padStart(2, "0")}</span>
                      <span className="agent-label">
                        {a ? a.label : key.replace(/_/g, " ")}
                      </span>
                      <span className="agent-state mono">
                        {state === "running"
                          ? "RUNNING"
                          : state === "complete"
                          ? "COMPLETE"
                          : "STANDBY"}
                      </span>
                    </div>
                    {a && a.preview && <p className="agent-preview">{a.preview}</p>}
                  </div>
                );
              })}
            </div>

            {documents.length > 0 && (
              <>
                <h2 className="panel-title">Document impacts</h2>
                <div className="docs">
                  {documents.map((d) => (
                    <div key={d.name} className={`doc doc-${d.state}`}>
                      <span className="doc-name">{docShortName(d.name)}</span>
                      <span className="doc-state mono">
                        {d.state === "assessed" ? "ASSESSED" : "QUEUED"}
                      </span>
                    </div>
                  ))}
                </div>
              </>
            )}
          </aside>

          <section className="sheet-wrap">
            <div className="sheet-head">
              <span className="eyebrow">Project Management Plan update</span>
              <span className="fineprint">
                {mode === "replay" ? "replay of recorded live run" : mode === "live" ? "live run" : ""}
              </span>
              {status === "done" && (
                <button className="download" onClick={downloadPmp}>
                  Download .md
                </button>
              )}
            </div>
            <div className="sheet" ref={sheetRef}>
              {pmp ? (
                <div className="pmp">
                  <ReactMarkdown remarkPlugins={[remarkGfm]}>{pmp}</ReactMarkdown>
                  {status === "running" && <span className="caret" />}
                </div>
              ) : (
                <p className="sheet-empty">
                  {status === "running"
                    ? "Agents are analyzing the change. The plan drafts here as soon as synthesis begins."
                    : "The drafted plan appears here."}
                </p>
              )}
            </div>
          </section>
        </main>
      )}
    </div>
  );
}

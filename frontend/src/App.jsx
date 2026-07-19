import { useState } from "react";
import AriaTool from "./AriaTool";

/* ---- ARIA logo mark: SVG recreation of the brand mark ----------------- */
/* Gradient left stroke, slate right leg, rotor blade with linkage nodes.  */
function AriaLogo({ size = 34 }) {
  return (
    <svg
      className="logo-mark"
      width={size}
      height={size}
      viewBox="0 0 64 64"
      aria-hidden="true"
    >
      <defs>
        <linearGradient id="ariaGrad" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stopColor="#2BC7DF" />
          <stop offset="0.55" stopColor="#3E6FE6" />
          <stop offset="1" stopColor="#7A3BE0" />
        </linearGradient>
      </defs>
      {/* right leg (slate) */}
      <path
        d="M33 9 L51 55"
        stroke="#5E7290"
        strokeWidth="9"
        strokeLinecap="round"
        fill="none"
      />
      {/* left stroke (brand gradient) */}
      <path
        d="M33 9 L15 55"
        stroke="url(#ariaGrad)"
        strokeWidth="9"
        strokeLinecap="round"
        fill="none"
      />
      {/* rotor blade crossing the counter */}
      <path
        d="M56 24 L31 41"
        stroke="#5E7290"
        strokeWidth="7"
        strokeLinecap="round"
        fill="none"
      />
      {/* linkage nodes */}
      <circle cx="27" cy="46" r="3.4" fill="none" stroke="url(#ariaGrad)" strokeWidth="2.4" />
      <path d="M29.5 43.5 L33 40" stroke="url(#ariaGrad)" strokeWidth="2.4" strokeLinecap="round" />
      <circle cx="36" cy="34" r="2.6" fill="url(#ariaGrad)" />
    </svg>
  );
}

/* ---- MAAP-1 technical line art, side profile ------------------------- */
function AircraftArt() {
  return (
    <svg
      className="hero-art"
      viewBox="0 0 920 340"
      role="img"
      aria-label="Technical side-profile drawing of the MAAP-1 tandem-rotor heavy-lift autonomous helicopter"
    >
      <defs>
        <linearGradient id="heroGrad" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0" stopColor="#2BC7DF" />
          <stop offset="1" stopColor="#7A3BE0" />
        </linearGradient>
      </defs>
      <g stroke="var(--steel)" strokeWidth="1.3" fill="none" strokeLinecap="round">
        <path d="M150 210 q10 -34 52 -40 L560 166 q60 -2 96 14 l64 28 q10 6 4 14 l-14 16 -530 0 q-24 0 -30 -18 z" />
        <path d="M162 196 q14 -20 44 -23 l40 -3 -6 26 z" opacity="0.85" />
        <path d="M710 238 l60 -34" opacity="0.8" />
        <path d="M236 168 l10 -52 26 0 8 50" />
        <path d="M596 170 l14 -74 30 0 10 72" />
        <path d="M230 238 l0 22 M214 260 l32 0 M602 238 l0 22 M586 260 l32 0" />
        <circle cx="222" cy="266" r="7" />
        <circle cx="240" cy="266" r="7" />
        <circle cx="594" cy="266" r="7" />
        <circle cx="612" cy="266" r="7" />
        <circle cx="176" cy="216" r="7" opacity="0.85" />
      </g>
      <g stroke="url(#heroGrad)" strokeWidth="1.6" fill="none" strokeLinecap="round">
        <path d="M64 108 L454 104" />
        <path d="M120 96 L400 118" opacity="0.45" />
        <path d="M436 86 L866 78" />
        <path d="M492 70 L812 96" opacity="0.45" />
        <circle cx="259" cy="106" r="4" fill="#3E6FE6" stroke="none" />
        <circle cx="651" cy="82" r="4" fill="#7A3BE0" stroke="none" />
      </g>
      <g stroke="var(--steel)" strokeWidth="1" opacity="0.75">
        <path d="M150 302 L774 302" />
        <path d="M150 296 L150 308 M774 296 L774 308" />
        <path d="M259 106 L259 60 M651 82 L651 46" strokeDasharray="4 4" opacity="0.6" />
      </g>
      <g stroke="var(--steel)" strokeWidth="1" opacity="0.7">
        <path d="M330 176 L330 132 L392 132" />
        <path d="M690 210 L744 172 L800 172" />
      </g>
      <g
        fill="var(--steel)"
        fontFamily="'IBM Plex Mono', monospace"
        fontSize="10.5"
        letterSpacing="0.08em"
      >
        <text x="462" y="316" textAnchor="middle">OVERALL LENGTH 22.4 M</text>
        <text x="259" y="52" textAnchor="middle">FWD ROTOR</text>
        <text x="651" y="38" textAnchor="middle">AFT ROTOR Ø 16.2 M</text>
        <text x="398" y="136">AUTONOMY BAY</text>
        <text x="806" y="176">CARGO RAMP</text>
        <text x="150" y="290">EURUS SYSTEMS · MAAP-1 · TANDEM-ROTOR HEAVY-LIFT · UNCREWED</text>
      </g>
    </svg>
  );
}

/* ---- Drawing-tree excerpt: dense configuration tree ------------------- */
function DrawingTree() {
  const SUBS = [
    { name: "AIRFRAME", leaves: 9 },
    { name: "ROTOR SYS", leaves: 8 },
    { name: "PROPULSION", leaves: 7 },
    { name: "ELEC PWR", leaves: 6 },
    { name: "AVIONICS", leaves: 9 },
    { name: "AUTONOMY", leaves: 7 },
    { name: "MISSION SYS", leaves: 8 },
    { name: "LDG GEAR", leaves: 6 },
  ];
  const rootX = 578;
  const xs = SUBS.map((_, i) => 75 + i * 144);

  return (
    <svg className="tree" viewBox="0 0 1160 330" role="img" aria-label="Excerpt of the MAAP-1 configuration drawing tree, showing eight subsystems fanning into dozens of assemblies">
      <g fontFamily="'IBM Plex Mono', monospace" letterSpacing="0.08em">
        <text x="20" y="24" fontSize="11" fill="var(--ink-soft)">
          DWG TREE — MAAP-1 AIR VEHICLE (EXCERPT · TOP TWO LEVELS OF SEVEN)
        </text>
        <rect x={rootX - 84} y="40" width="168" height="30" fill="none" stroke="var(--ink)" strokeWidth="1.5" />
        <text x={rootX} y="59" fontSize="11" fill="var(--ink)" textAnchor="middle" fontWeight="600">
          MAAP-1 AIR VEHICLE
        </text>
        <path d={`M${rootX} 70 L${rootX} 92 M${xs[0]} 92 L${xs[7]} 92`} stroke="var(--ink)" strokeWidth="1" fill="none" />
        {SUBS.map((s, i) => {
          const x = xs[i];
          const L = s.leaves;
          const lxs = Array.from({ length: L }, (_, j) => x - ((L - 1) * 14) / 2 + j * 14);
          return (
            <g key={s.name}>
              <path d={`M${x} 92 L${x} 108`} stroke="var(--ink)" strokeWidth="1" />
              <rect x={x - 56} y="108" width="112" height="24" fill="var(--paper)" stroke="var(--ink)" strokeWidth="1.2" />
              <text x={x} y="124" fontSize="9.5" fill="var(--ink)" textAnchor="middle">{s.name}</text>
              <path
                d={`M${x} 132 L${x} 156 M${lxs[0]} 156 L${lxs[L - 1]} 156`}
                stroke="var(--ink-soft)"
                strokeWidth="0.9"
                fill="none"
              />
              {lxs.map((lx, j) => (
                <g key={j}>
                  <path d={`M${lx} 156 L${lx} 184`} stroke="var(--ink-soft)" strokeWidth="0.9" />
                  <rect
                    x={lx - 3}
                    y="184"
                    width="6"
                    height="6"
                    fill={j % 4 === 0 ? "var(--brand-b)" : "var(--ink-soft)"}
                  />
                  {j % 3 === 0 && (
                    <>
                      <path d={`M${lx} 190 L${lx} 212`} stroke="var(--ink-soft)" strokeWidth="0.8" opacity="0.7" />
                      <rect x={lx - 2.5} y="212" width="5" height="5" fill="none" stroke="var(--ink-soft)" strokeWidth="0.8" />
                    </>
                  )}
                </g>
              ))}
            </g>
          );
        })}
        <text x="20" y="266" fontSize="10.5" fill="var(--ink-soft)">
          EACH SQUARE CONTINUES INTO ITS OWN ASSEMBLY, INSTALLATION, AND PART-LEVEL TREE —
        </text>
        <text x="20" y="284" fontSize="10.5" fill="var(--ink-soft)">
          MAINTAINED SEPARATELY FOR THREE MISSION VARIANTS: CARGO · FIREFIGHTING · ISR
        </text>
        <text x="20" y="314" fontSize="10.5" fill="var(--brand-b)">
          ARIA RETRIEVES AND REASONS ACROSS THIS ENTIRE BASELINE ON EVERY RUN
        </text>
      </g>
    </svg>
  );
}

/* ---- Content data ----------------------------------------------------- */
const FLOW = [
  { label: "Change request", note: "Free-text engineering or program change" },
  { label: "5 specialist agents", note: "Change · Cost & Margin · Manufacturing · Supply Chain · Risk & Schedule — in parallel" },
  { label: "Document impact layer", note: "Every core baseline document assessed individually" },
  { label: "Synthesis", note: "One senior-PM voice, streamed live" },
  { label: "PMP update", note: "10-section decision-grade plan" },
];

/*
 * BASELINE_STATS: replace the "—" value with the REAL number from:
 *   python3 - <<'EOF'
 *   import glob
 *   files = glob.glob('data/maap1_*.md')
 *   words = sum(len(open(f, encoding='utf-8').read().split()) for f in files)
 *   print(f"{len(files)} docs, {words:,} words")
 *   EOF
 */
const BASELINE_STATS = [
  { value: "19", label: "controlled documents" },
  { value: "213,832", label: "words of program baseline" },
  { value: "3", label: "mission-variant drawing trees" },
  { value: "40+", label: "tracked risks, scored & owned" },
  { value: "5", label: "specialist agents per run" },
  { value: "10", label: "documents assessed every run" },
];

const DIFFERENTIATORS = [
  {
    title: "Guaranteed document coverage",
    body: "Most RAG systems let semantic similarity decide what gets read — and loud documents like a risk register win every time. ARIA uses a coverage manifest: the core baseline documents are analyzed on every run, by construction, with retrieval used only to discover extras.",
  },
  {
    title: "Document-native retrieval",
    body: "Each analysis retrieves from exactly the document it claims to be reading, via filename-filtered retrieval — not a global search that hopes the right chunks surface. The BOM analysis reads the BOM. Every time.",
  },
  {
    title: "An auditor, not a summarizer",
    body: "Because each document is read on its own terms, ARIA notices when documents disagree with each other — and says so, with action items and owners, instead of smoothing the conflict over.",
  },
  {
    title: "Decision-grade output",
    body: "The product isn't a chat answer. It's a 10-section Project Management Plan update: decision gates, reserve drawdowns, risk register entries with scores and owners, 90-day action plans, go/no-go criteria.",
  },
  {
    title: "Watchable reasoning",
    body: "Every phase streams to the console as it happens — agents completing, documents lighting up, the plan drafting token by token. Nothing hides behind a spinner.",
  },
  {
    title: "Honest economics",
    body: "Preset scenarios replay recorded live runs at zero inference cost — labeled as replays, time-compressed to ~2 minutes. Custom changes run the real ~10-minute pipeline, gated by access code. Cost engineering is engineering.",
  },
];

const VERTICAL = [
  {
    title: "One change, every discipline",
    body: "At a vertically integrated company, nothing changes alone. A battery swap is a certification question, a BOM revision, a supplier negotiation, a cash-flow event, and a work-instruction rewrite — simultaneously. ARIA analyzes the whole ripple, not one lane of it.",
  },
  {
    title: "The same picture at every level",
    body: "Impact analysis usually lives in the heads of a few senior people and surfaces weeks later in review decks. ARIA gives an intern and a VP the same decision-grade picture of a change — sourced from the same controlled baseline.",
  },
  {
    title: "Real time, not review-cycle time",
    body: "The question \"what does this change touch?\" normally waits for the next CCB cycle. ARIA answers it in minutes, with the risk entries, reserve impacts, and owner assignments already drafted for the board to react to.",
  },
];

const FINDINGS = [
  {
    id: "FINDING-001",
    title: "BOM chemistry conflict",
    body: "Asked to assess a lithium-ion battery supplier swap, ARIA cross-checked the Bill of Materials and found the baseline actually specifies Nickel-Cadmium chemistry for both battery assemblies — meaning the change request was written against the wrong baseline, or an undocumented design change was in flight. It refused to proceed quietly: it opened a Critical risk (score 16), assigned a 15-day action item to the Chief Engineer, and made resolution a hard gate before CCB approval.",
  },
  {
    id: "FINDING-002",
    title: "Milestone baseline conflict",
    body: "During a First Flight delay analysis, ARIA caught the Program Overview stating First Flight as Q2 2028 while the Integrated Master Schedule places it at 21 May 2030 — a pre-existing inconsistency in the baseline itself. It flagged the discrepancy, adopted the IMS as authoritative, and directed formal correction of the conflicting documents.",
  },
];

const DOC_GROUPS = [
  {
    group: "Technical baseline",
    docs: ["Program Requirements Baseline (+ continuation)", "Key Specifications", "Bill of Materials", "Drawing Trees — Cargo · Firefighting · ISR", "Safety Requirements", "Security Requirements"],
  },
  {
    group: "Program control",
    docs: ["Integrated Master Schedule", "Risk Register", "Test & Evaluation Master Plan", "Quality Management Plan", "Program Overview"],
  },
  {
    group: "Business & industrial",
    docs: ["Financial & Contract Management", "Supply Chain Procurement Plan", "Manufacturing Ramp Plan", "Customer Demand Forecast", "Vertical Integration & Make/Buy Strategy"],
  },
];

const BUILD_LOG = [
  {
    tag: "PH-01",
    title: "Synthetic program baseline",
    body: "Generated and curated a 19-document program baseline for a fictional aerospace program — schedules, risk registers, BOMs, financials — dense enough to support real cross-document reasoning.",
  },
  {
    tag: "PH-02",
    title: "RAG foundation",
    body: "Built semantic retrieval over the baseline with LlamaIndex and sentence-transformer embeddings, with a persisted vector index and thread-safe lazy loading.",
  },
  {
    tag: "PH-03",
    title: "Multi-agent architecture",
    body: "Five specialist agents running in parallel on Claude, each with its own document beat — then a document-impact layer assessing every core document individually.",
  },
  {
    tag: "PH-04",
    title: "Killing retrieval bias",
    body: "Diagnosed why semantic search over-served the Risk Register, and replaced hope with guarantees: manifest-driven coverage and per-document filtered retrieval. This is what unlocked the audit findings.",
  },
  {
    tag: "PH-05",
    title: "Streaming synthesis",
    body: "A senior-PM synthesis pass that drafts the full 10-section PMP as a live token stream — with prompt architecture (context first, instructions last) and output budgets tuned for documents this long.",
  },
  {
    tag: "PH-06",
    title: "The console",
    body: "FastAPI backend streaming Server-Sent Events to a React mission console — plus a record/replay system so real runs can be demonstrated at zero cost, and an access-code gate on live inference.",
  },
];

const ROADMAP = [
  "Inline citations — every claim in the PMP linked to the exact source passage it came from",
  "What-if comparison — run two change options side by side and diff the impact",
  "Native .docx export matching the program's controlled-document template",
  "Quantitative hooks — EVMS and Monte Carlo inputs computed, not just described",
  "Evaluation harness — scored regression tests so prompt and retrieval changes are measured, not vibed",
  "Multi-program support — point ARIA at any document baseline, not just MAAP-1",
];

function ContactForm() {
  const [state, setState] = useState("idle");

  async function onSubmit(e) {
    e.preventDefault();
    setState("sending");
    try {
      const res = await fetch("https://formspree.io/f/meeykjpl", {
        method: "POST",
        body: new FormData(e.target),
        headers: { Accept: "application/json" },
      });
      setState(res.ok ? "sent" : "error");
    } catch {
      setState("error");
    }
  }

  if (state === "sent") {
    return (
      <p className="form-done">
        Message sent. Thanks for reaching out — replies come from a relay, so
        check your inbox.
      </p>
    );
  }

  return (
    <form className="form" onSubmit={onSubmit}>
      <div className="form-row">
        <input type="text" name="name" placeholder="Name" required />
        <input type="email" name="email" placeholder="Your email (for the reply)" required />
      </div>
      <textarea
        name="message"
        rows={5}
        placeholder="Feedback on ARIA, ideas worth building, or just say hello…"
        required
      />
      <div className="form-foot">
        <span className="fineprint">Messages route through a relay — no address is exposed on this site.</span>
        <button className="run" type="submit" disabled={state === "sending"}>
          {state === "sending" ? "Sending…" : "Send message"}
        </button>
      </div>
      {state === "error" && (
        <div className="errorbar">The message didn't go through — try again in a moment.</div>
      )}
    </form>
  );
}

export default function App() {
  return (
    <div className="site">
      {/* ================= HERO ================= */}
      <div className="hero">
        <nav className="nav">
          <a className="nav-brand" href="#top">
            <AriaLogo />
            <span className="nav-name">ARIA</span>
          </a>
          <div className="nav-links">
            <a href="#console">Console</a>
            <a href="#how">How it works</a>
            <a href="#vertical">Why vertical</a>
            <a href="#findings">Findings</a>
            <a href="#program">The program</a>
            <a href="#build">Build log</a>
            <a href="#contact">Contact</a>
          </div>
        </nav>

        <div className="hero-inner" id="top">
          <p className="hero-eyebrow">Agentic Reasoning for Impact Analysis</p>
          <h1 className="hero-title">
            Propose a change.
            <br />
            Get the program plan.
          </h1>
          <p className="hero-sub">
            ARIA is a multi-agent AI system built for vertically integrated
            programs. It reads an aerospace program's entire document baseline —
            schedules, risk registers, BOMs, financials — and drafts the
            change-impact analysis a program office would: a full Project
            Management Plan update, with decision gates, reserve impacts, and
            owners.
          </p>
          <div className="hero-ctas">
            <a className="btn-primary" href="#console">Run a scenario</a>
            <a className="btn-ghost" href="#how">See how it works</a>
          </div>
        </div>

        <AircraftArt />
      </div>
      <div className="grad-bar" />

      {/* ================= CONSOLE ================= */}
      <section className="sec" id="console">
        <div className="sec-head">
          <span className="sec-num">§ 01</span>
          <h2>The Impact Console</h2>
          <p>
            Pick a scenario and watch a real analysis unfold — five specialist
            agents, per-document impact assessments, and a Project Management
            Plan drafting itself live. Presets replay recorded runs of the real
            pipeline, time-compressed to about two minutes. Custom changes run
            the full live pipeline — a real analysis takes roughly ten minutes
            and requires an access code.
          </p>
        </div>
        <AriaTool />
      </section>

      {/* ================= HOW IT WORKS ================= */}
      <section className="sec sec-alt" id="how">
        <div className="sec-head">
          <span className="sec-num">§ 02</span>
          <h2>How ARIA works</h2>
          <p>
            One change request fans out into parallel specialist analysis and
            document-by-document impact assessment, then converges into a
            single senior-PM voice.
          </p>
        </div>

        <div className="flow">
          {FLOW.map((f, i) => (
            <div className="flow-step" key={f.label}>
              <div className="flow-node">
                <span className="flow-label">{f.label}</span>
                <span className="flow-note">{f.note}</span>
              </div>
              {i < FLOW.length - 1 && <span className="flow-arrow">→</span>}
            </div>
          ))}
        </div>

        <div className="stack">
          <span className="eyebrow">Under the hood</span>
          <div className="stack-chips">
            {[
              "Claude Sonnet 4.6",
              "Python · FastAPI",
              "LlamaIndex RAG",
              "Sentence-transformer embeddings",
              "Parallel agent orchestration",
              "Server-Sent Event streaming",
              "React",
            ].map((t) => (
              <span className="chip" key={t}>{t}</span>
            ))}
          </div>
        </div>

        <div className="cards">
          {DIFFERENTIATORS.map((d) => (
            <div className="card" key={d.title}>
              <h3>{d.title}</h3>
              <p>{d.body}</p>
            </div>
          ))}
        </div>
      </section>

      {/* ================= VERTICAL INTEGRATION ================= */}
      <section className="band" id="vertical">
        <div className="band-inner">
          <span className="sec-num">§ 03</span>
          <h2>
            Built for <span className="grad-text">vertically integrated</span> programs
          </h2>
          <p className="band-lede">
            When design, manufacturing, supply chain, and finance live under one
            roof, every change touches all of them at once — and the impact
            picture usually lives in a handful of senior heads. ARIA puts that
            picture in front of anyone, at any level, in real time.
          </p>
          <div className="band-cards">
            {VERTICAL.map((v) => (
              <div className="band-card" key={v.title}>
                <h3>{v.title}</h3>
                <p>{v.body}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ================= FINDINGS ================= */}
      <section className="sec" id="findings">
        <div className="sec-head">
          <span className="sec-num">§ 04</span>
          <h2>What it catches</h2>
          <p>
            The strongest evidence that ARIA reads documents rather than
            pattern-matching them: unprompted, it has caught real
            inconsistencies planted deep in the program baseline.
          </p>
        </div>
        <div className="findings">
          {FINDINGS.map((f) => (
            <div className="finding" key={f.id}>
              <div className="finding-head">
                <span className="finding-id mono">{f.id}</span>
                <span className="finding-stamp mono">UNPROMPTED</span>
              </div>
              <h3>{f.title}</h3>
              <p>{f.body}</p>
            </div>
          ))}
        </div>
      </section>

      {/* ================= PROGRAM ================= */}
      <section className="sec sec-alt" id="program">
        <div className="sec-head">
          <span className="sec-num">§ 05</span>
          <h2>The MAAP-1 program baseline</h2>
          <p>
            ARIA's testbed is a fictional program built to feel real: Eurus
            Systems' MAAP-1, a tandem-rotor heavy-lift autonomous helicopter
            for wildfire, cargo, and ISR missions. Its baseline is not a toy
            dataset — it's a full, interlinked controlled-document set, seeded
            with the kinds of conflicts real programs accumulate.
          </p>
        </div>

        <div className="stats">
          {BASELINE_STATS.map((s) => (
            <div className="stat" key={s.label}>
              <span className="stat-value">{s.value}</span>
              <span className="stat-label">{s.label}</span>
            </div>
          ))}
        </div>

        <DrawingTree />

        <div className="docgroups">
          {DOC_GROUPS.map((g) => (
            <div className="docgroup" key={g.group}>
              <span className="eyebrow">{g.group}</span>
              <div className="doclist">
                {g.docs.map((d) => (
                  <span className="docchip" key={d}>{d}</span>
                ))}
              </div>
            </div>
          ))}
        </div>

        <p className="disclosure">
          Eurus Systems, MAAP-1, and every document, supplier reference, and
          figure in this system are fictional and synthetic. No real program
          data is used.
        </p>
      </section>

      {/* ================= BUILD LOG ================= */}
      <section className="sec" id="build">
        <div className="sec-head">
          <span className="sec-num">§ 06</span>
          <h2>Build log</h2>
          <p>
            ARIA is a portfolio system, built end to end by a program manager
            learning to engineer — data, retrieval, agents, backend, and
            frontend. The interesting parts were the failures.
          </p>
        </div>
        <div className="log">
          {BUILD_LOG.map((b) => (
            <div className="log-row" key={b.tag}>
              <span className="log-tag mono">{b.tag}</span>
              <div>
                <h3>{b.title}</h3>
                <p>{b.body}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* ================= ROADMAP ================= */}
      <section className="sec sec-alt" id="roadmap">
        <div className="sec-head">
          <span className="sec-num">§ 07</span>
          <h2>Roadmap</h2>
          <p>Where this goes next.</p>
        </div>
        <ul className="roadmap">
          {ROADMAP.map((r) => (
            <li key={r}>{r}</li>
          ))}
        </ul>
      </section>

      {/* ================= CONTACT ================= */}
      <section className="sec" id="contact">
        <div className="sec-head">
          <span className="sec-num">§ 08</span>
          <h2>Get in touch</h2>
          <p>
            Ideas for ARIA, feedback on the analysis quality, or interest in
            the approach — messages are welcome.
          </p>
        </div>
        <ContactForm />
      </section>

      <footer className="footer">
        <div className="footer-brand">
          <AriaLogo size={26} />
          <span className="nav-name">ARIA</span>
        </div>
        <span className="fineprint">
          Agentic Reasoning for Impact Analysis · Eurus Systems and MAAP-1 are
          fictional · analysis powered by Claude
        </span>
      </footer>
    </div>
  );
}

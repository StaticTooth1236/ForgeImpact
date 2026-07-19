"""
ForgeImpact — Demo Recorder
---------------------------
Runs a REAL analysis through the pipeline (~$2.30, ~10-12 min per scenario)
and records every event, with timestamps, into a JSON file the frontend can
replay for free with the same live feel.

Recordings are written to frontend/public/demos/<slug>.json.

Usage (from the project root):
    python3 record_demo.py <slug>       # record one scenario
    python3 record_demo.py all          # record every scenario missing a file
    python3 record_demo.py all --force  # re-record everything

IMPORTANT: The change_description texts below must stay EXACTLY in sync with
the PRESETS in frontend/src/App.jsx — the frontend matches on the exact text
to decide whether a recording exists for what's in the box.
"""

import json
import os
import sys
import time
from datetime import datetime, timezone

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.pipeline_events import run_analysis_events

DEMOS = {
    "battery-supplier-swap": (
        "Change the primary battery supplier from Samsung SDI to LG Energy "
        "Solution. Assess the impact on certification timeline, unit cost, and "
        "supply chain risk."
    ),
    "first-flight-delay": (
        "Delay First Flight by 6 months due to autonomy software certification "
        "issues. Assess impact on program cost, customer deliveries, and risk "
        "posture."
    ),
    "titanium-rotor-hub": (
        "Replace the aluminum main rotor hub with a titanium design to improve "
        "fatigue life. Assess impact on weight, cost, qualification testing, "
        "and the manufacturing ramp."
    ),
    "flight-computer-shortage": (
        "The flight computer supplier has notified the program of a 12-month "
        "semiconductor allocation shortage affecting IMA core processor "
        "deliveries. Assess impact on production continuity, schedule, buffer "
        "stock strategy, and program risk."
    ),
    "production-rate-increase": (
        "Accelerate the production ramp from 2 to 6 aircraft per year "
        "beginning in LRIP-2 to meet growing wildfire fleet demand. Assess "
        "impact on manufacturing readiness, supply chain capacity, cost, and "
        "quality."
    ),
    "cargo-fleet-order": (
        "A new customer has placed an order for 15 additional cargo variant "
        "aircraft with deliveries beginning 2029. Assess impact on the "
        "production schedule, supply chain, financials, and program risk."
    ),
}

OUT_DIR = os.path.join("frontend", "public", "demos")


def record(slug: str, change_description: str) -> None:
    print(f"\n=== Recording demo: {slug} ===")
    print(f"Change: {change_description[:80]}...\n")

    events = []
    t0 = time.time()
    for evt in run_analysis_events(change_description):
        events.append({"t": round(time.time() - t0, 3), "event": evt})
        if evt["type"] != "synthesis_token":
            print(f"  [{events[-1]['t']:7.1f}s] {evt['type']}")

    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, f"{slug}.json")
    with open(path, "w") as f:
        json.dump(
            {
                "slug": slug,
                "change_description": change_description,
                "recorded_at": datetime.now(timezone.utc).isoformat(),
                "duration_seconds": events[-1]["t"] if events else 0,
                "events": events,
            },
            f,
        )
    size_kb = os.path.getsize(path) // 1024
    print(f"\n✅ Saved {len(events)} events ({size_kb} KB) to {path}")


if __name__ == "__main__":
    if len(sys.argv) < 2 or (sys.argv[1] != "all" and sys.argv[1] not in DEMOS):
        print("Usage: python3 record_demo.py <slug>|all [--force]")
        print("Available slugs:", ", ".join(DEMOS))
        sys.exit(1)

    force = "--force" in sys.argv
    targets = list(DEMOS.keys()) if sys.argv[1] == "all" else [sys.argv[1]]

    for slug in targets:
        path = os.path.join(OUT_DIR, f"{slug}.json")
        if os.path.exists(path) and not force:
            print(f"⏭  {slug}: recording already exists, skipping (use --force to re-record)")
            continue
        record(slug, DEMOS[slug])
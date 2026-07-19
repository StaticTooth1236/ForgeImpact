"""
ARIA — API Server
------------------------
Exposes the analysis pipeline over HTTP for the web frontend.

Run locally (from project root, venv active):
    uvicorn api:app --port 8000

Endpoints:
    GET  /api/health   — liveness check
    POST /api/analyze  — body: {"change_description": "..."}
                         header: X-Access-Code (required if LIVE_ACCESS_CODE is set)
                         returns a Server-Sent Events stream of pipeline events

Access control:
    Set LIVE_ACCESS_CODE in .env to require a code for live runs. Recorded
    demo replays never touch this server, so the public site works without a
    code. If LIVE_ACCESS_CODE is unset, all live runs are allowed (dev mode).
"""

import json
import os

from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from src.pipeline_events import run_analysis_events

load_dotenv()

LIVE_ACCESS_CODE = os.getenv("LIVE_ACCESS_CODE", "")

app = FastAPI(title="ARIA API")

# Locked down to the real frontend domain at deploy time.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://aria-impact.com",
        "https://www.aria-impact.com",
        "https://YOUR-PROJECT.vercel.app",   # your actual .vercel.app URL
        "http://localhost:5173",             # keep local dev working
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnalyzeRequest(BaseModel):
    change_description: str


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/analyze")
def analyze(req: AnalyzeRequest, x_access_code: str = Header(default="")):
    if LIVE_ACCESS_CODE and x_access_code != LIVE_ACCESS_CODE:
        raise HTTPException(
            status_code=401,
            detail="A valid access code is required for live analysis runs.",
        )

    change = req.change_description.strip()
    if not change:
        raise HTTPException(status_code=400, detail="change_description is required")
    if len(change) > 2000:
        raise HTTPException(status_code=400, detail="change_description too long (max 2000 chars)")

    def event_stream():
        try:
            for event in run_analysis_events(change):
                yield f"data: {json.dumps(event)}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'message': str(e)})}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
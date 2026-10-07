"""
Dash_client.py
==============
Client helper for the wired paper's figure notebooks.

In the canonical wired-paper design this class queries a remote Dash/FastAPI
server. This project does not need a running server: all results are precomputed
into a single versioned `data.json` (the same file the standalone dashboard
reads), so this client simply loads that file and builds the Plotly figures,
optionally wired to ipywidgets controls for interactivity under Binder.

Point DATA_URL at your deployed dashboard's data.json, or at a local copy.
"""

from __future__ import annotations

import json
import statistics
from urllib.request import urlopen

import plotly.graph_objects as go

# Default: the data.json served alongside your deployed dashboard.
DATA_URL = "https://Sebrm2.github.io/retraction-analysis/data.json"

PALETTE = ["#8a2b2b", "#2a6b62", "#a97b26", "#3a5a78", "#b5533f",
           "#6d6875", "#606c38", "#9c6b3f", "#4a7a86", "#8d5b7a",
           "#557153", "#a8763e", "#3f5b78"]
SUBJECT_ORDER = ["Neuroscience", "Biostatistics/Epidemiology",
                 "Radiology/Imaging", "Nanotechnology"]


class RetractionClient:
    """Loads precomputed records and renders interactive Plotly figures."""

    # ---- data retrieval -----------------------------------------------------
    def __init__(self, data_url: str = DATA_URL):
        self.data_url = data_url
        self._data = None

    def _load(self):
        if self._data is None:
            if self.data_url.startswith("http"):
                with urlopen(self.data_url, timeout=30) as r:
                    self._data = json.loads(r.read().decode())
            else:
                with open(self.data_url) as f:
                    self._data = json.load(f)
        return self._data

    def records(self, subject="__all", year_from=None, year_to=None):
        d = self._load()
        cur = d.get("current_year", 9999)
        out = []
        for r in d["records"]:
            ry = r.get("ry")
            if ry is None or ry >= cur:
                continue
            if year_from is not None and ry < year_from:
                continue
            if year_to is not None and ry > year_to:
                continue
            if subject not in ("__all",) and r.get("sub") != subject:
                continue
            out.append(r)
        return out

    # ---- utils --------------------------------------------------------------
    @staticmethod
    def _median(xs):
        xs = [x for x in xs if x is not None]
        return statistics.median(xs) if xs else None

    def _layout(self, **over):
        base = dict(
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter, sans-serif", size=12, color="#4a4842"),
            margin=dict(l=55, r=18, t=10, b=45), showlegend=False,
        )
        base.update(over)
        return base

    # ---- visualizations -----------------------------------------------------
    def fig_annual(self, subject="__all"):
        rows = self.records(subject)
        counts = {}
        for r in rows:
            counts[r["ry"]] = counts.get(r["ry"], 0) + 1
        years = sorted(counts)
        fig = go.Figure(go.Scatter(
            x=years, y=[counts[y] for y in years], mode="lines+markers",
            fill="tozeroy", line=dict(color=PALETTE[0], width=2.5),
            marker=dict(size=4, color=PALETTE[0])))
        fig.update_layout(**self._layout(
            xaxis_title="Year of retraction", yaxis_title="Retractions"))
        return fig

    def fig_time_to_retraction(self, subject="__all"):
        rows = self.records(subject)
        vals = [r["ttr"] for r in rows if r.get("ttr") is not None]
        fig = go.Figure(go.Histogram(x=vals, xbins=dict(start=0, end=30, size=1),
                                     marker_color=PALETTE[1]))
        fig.update_layout(**self._layout(
            xaxis_title="Years to retraction", yaxis_title="Papers"))
        return fig

    def fig_reasons(self, subject="__all"):
        rows = self.records(subject)
        counts = {}
        for r in rows:
            for c in r.get("rs", []):
                counts[c] = counts.get(c, 0) + 1
        items = sorted(counts.items(), key=lambda kv: kv[1])
        fig = go.Figure(go.Bar(
            x=[v for _, v in items], y=[k for k, _ in items], orientation="h",
            marker_color=[PALETTE[i % len(PALETTE)] for i in range(len(items))]))
        fig.update_layout(**self._layout(
            margin=dict(l=220, r=18, t=10, b=40), xaxis_title="Retractions"))
        return fig

    def fig_subject_comparison(self):
        d = self._load()
        subs = [s for s in SUBJECT_ORDER if s in d.get("subjects", [])]
        counts = [len(self.records(subject=s)) for s in subs]
        fig = go.Figure(go.Bar(x=subs, y=counts,
                               marker_color=PALETTE[:len(subs)]))
        fig.update_layout(**self._layout(yaxis_title="Retractions"))
        return fig


def interactive_annual(client: "RetractionClient | None" = None):
    """Subject dropdown wired to the annual-trend figure (needs ipywidgets)."""
    import ipywidgets as widgets
    from IPython.display import display

    client = client or RetractionClient()
    d = client._load()
    options = [("All four fields", "__all")] + [
        (s, s) for s in SUBJECT_ORDER if s in d.get("subjects", [])]
    dropdown = widgets.Dropdown(options=options, description="Subject:")
    out = widgets.Output()

    def _draw(_=None):
        with out:
            out.clear_output(wait=True)
            client.fig_annual(dropdown.value).show()

    dropdown.observe(_draw, names="value")
    display(dropdown, out)
    _draw()

# Retraction patterns in biomedical fields — wired paper

This is the **wired paper** version of the retraction analysis: an interactive MyST article
whose figures are produced by live code and an embedded dashboard, rather than static
images. It is based on the [wired paper template](https://github.com/moranebienvenu/wired_papers_template)
by Morane Bienvenu / NeuroLibre.

## What a wired paper is

A wired paper embeds an interactive dashboard directly into the narrative of a scientific
article. Readers explore, filter, and visualise the data from within the article — no
programming required. The article is a lightweight client; computation lives outside it.

In the canonical design the figures query a live Dash/FastAPI server. **This project does
not need a separate server:** the companion dashboard already computes everything in the
browser from a small, versioned `data.json`. So the article embeds that dashboard directly
and the figure notebooks read the same `data.json`. You get a true wired paper without
standing up or paying for a backend.

## Repository layout

```
wired-paper/
├── paper.md                 # the article (MyST Markdown)
├── myst.yml                 # project config: authors, binder, Pages URL, bibliography
├── paper.bib                # references
├── runtime.txt              # Python version for Binder
├── content/
│   ├── Dash_client.py       # loads data.json, builds Plotly figures
│   └── figure_1.ipynb       # example figure notebook (interactive under Binder)
├── static/
│   └── fig1.png             # static placeholder shown before Binder attaches
├── binder/
│   ├── requirements.txt     # Python deps for the live runtime
│   ├── runtime.txt
│   └── data_requirement.json# declares the data.json download
└── .github/workflows/
    └── deploy.yml           # builds the MyST site and deploys to GitHub Pages
```

## Before you publish: three things to edit

1. **Point the article at your dashboard.** In `paper.md`, replace every
   `https://<your-github-username>.github.io/retraction-analysis/` with the live URL of your
   deployed dashboard (the `retraction-analysis` repo's GitHub Pages site).
2. **Fill in your details** in `myst.yml`: the `github` URL, `thebe.binder.repo`, the
   `site.url`, your email, and ORCID if you have one.
3. **Update the data URL** in `content/Dash_client.py` and `binder/data_requirement.json`
   to the same dashboard `data.json`.

## Deploy

1. Create a new GitHub repository (for example `wired-paper`) and push these files.
2. In the repo, go to **Settings → Pages** and set **Source** to **GitHub Actions**.
3. Push any commit (or use **Actions → Run workflow**). The workflow builds the MyST site
   and deploys it.
4. The article goes live at `https://<your-github-username>.github.io/wired-paper/`.

### Preview locally (optional)

```bash
npm install -g mystmd
myst start        # live preview at http://localhost:3000
```

## How the interactivity works for a reader

- **Hover and zoom** on the embedded dashboard work immediately for everyone.
- For the notebook figures, a reader can attach a **Binder** runtime (the power icon on a
  figure), which runs `content/*.ipynb` against the live `data.json` and replaces the static
  placeholder with a live Plotly chart.

## Add a static placeholder

Put a `static/fig1.png` (a screenshot of the figure) so the article always renders before a
runtime is attached. Add one per figure notebook you create.

## License

Article content: CC-BY-4.0. Code: MIT. The Retraction Watch Database is used under its terms
(CC BY via Crossref); citation data from iCite and OpenAlex under their respective terms.

# Retraction patterns in biomedical fields — wired paper

This is the **wired paper** version of the retraction analysis: an interactive MyST article
whose figures are produced by live code and an embedded dashboard. It is based on the [wired paper template](https://github.com/moranebienvenu/wired_papers_template) by Morane Bienvenu / NeuroLibre.

## What a wired paper is

A wired paper embeds an interactive dashboard directly into a scientific
article. Readers explore, filter, and visualise the data from within the article.

In the template design the figures query a live Dash/FastAPI server. However, this project does
not need a separate server: the companion dashboard already computes everything in the
browser from a small `data.json`. So the article embeds that dashboard directly
and the figure notebooks read the same `data.json`.

## Repository layout

```
wired-paper/
├── paper.md                 # the article (MyST Markdown)
├── myst.yml                 # project config: authors, binder, Pages URL, bibliography
├── paper.bib                # references
├── runtime.txt              
├── content/
│   ├── Dash_client.py       # loads data.json, builds Plotly figures
│   
├── static/
│   └── fig1.png             # static placeholder shown before Binder attaches
├── binder/
│   ├── requirements.txt     # Python deps for the live runtime
│   ├── runtime.txt
│   └── data_requirement.json# declares the data.json download
└── .github/workflows/
    └── deploy.yml           # builds the MyST site and deploys to GitHub Pages
```

## License

Article content: CC-BY-4.0. Code: MIT. The Retraction Watch Database is used under its terms
(CC BY via Crossref); citation data from iCite and OpenAlex under their respective terms.

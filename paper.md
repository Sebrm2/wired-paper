---
title: "Retraction patterns in quantitative and imaging-focused biomedical fields"
short_title: Biomedical retraction patterns
numbering:
  headings: true
---

+++ {"part": "abstract"}

Retraction is the scientific community's mechanism for removing invalid work from the
record, yet it is often slow and incomplete. We analyse retracted publications across four
quantitative, data- and image-intensive biomedical research areas — neuroscience,
biostatistics and epidemiology, radiology and imaging, and nanotechnology — using the
Retraction Watch Database. We characterise how many papers were retracted, the stated
reasons, the geographic distribution of author affiliations, the time elapsed between
publication and retraction, and the relationship between a paper's citation profile and how
quickly it is retracted. Rather than presenting static figures, this article embeds an
interactive dashboard: every figure can be filtered by field and by year directly in the
browser, with no software to install. We find that time-to-retraction is driven primarily
by the stated reason rather than the country of origin, and that more highly cited papers
tend to remain in the record longer before being retracted.

+++

## Introduction

When a paper is retracted, the intended effect is simple: the work leaves the usable
literature, citations to it stop, downstream syntheses are corrected, and the damage is
contained. In practice, retraction is frequently slow, uneven across fields and countries,
and incomplete — retracted work continues to be cited for years afterward
[@Hutchins2016; @RetractionWatchDB].

Most prior analyses of the retraction record either treat retractions in aggregate across
all of science or present their findings as static charts. General-purpose retraction
dashboards have begun to appear — for example, integrated analytics platforms that map
global retraction trends across reasons, journals, and countries [@Singh2026], and
nightly-updated trackers focused on post-retraction citation [@XeraRetractionTracker]. What
is missing is a *field-comparative* account: whether research areas that share a
methodological character — heavy reliance on quantitative data and on imaging — exhibit
distinct retraction signatures, and whether the speed of retraction is governed by where
the work came from or by what went wrong.

This article addresses that gap for four such fields. It is also, deliberately, an
experiment in format. It is written as a **wired paper** [@Bienvenu2026]: an article whose
figures are produced by live, interactive code rather than fixed images, so that a reader
can interrogate the data themselves. The analysis is fully reproducible, and the dashboard
that produces every figure is embedded directly below.

### The interactive analysis

The complete analysis is available as a single interactive dashboard. Readers can filter
each figure by subject area and by retraction-year range; the world map responds to hover
and zoom; and the citation-analysis panels relate a paper's prominence to how long it took
to retract.

<div style="position:relative;width:100%;height:850px;border:1px solid #d6d0c1;border-radius:3px;overflow:hidden;margin:1.5rem 0;">
  <iframe
    src="https://sebrm2.github.io/retraction-analysis/?app=1&v=7"
    style="width:100%;height:100%;border:0;"
    loading="lazy"
    referrerpolicy="no-referrer-when-downgrade"
    title="Interactive retraction dashboard">
  </iframe>
</div>

The interactive retraction dashboard. Use the **Subject focus** and **year range** controls
at the top to filter every tab at once, and switch tabs to move between overview, timing,
reasons, geography, and citation views.

:::{note} Prefer a full window?
The dashboard also runs as a standalone page:
[**Open the dashboard in a new tab →**](https://sebrm2.github.io/retraction-analysis/?app=1&v=7)
:::

## Methods

### Data source and scope

Retraction records were drawn from the Retraction Watch Database, provided by The Center
for Scientific Integrity and distributed through Crossref [@RetractionWatchDB]. We restricted
the records to notices whose nature is a *retraction* (excluding corrections, expressions of
concern, and reinstatements) and to four subject areas as tagged by Retraction Watch:
neuroscience, biostatistics and epidemiology, radiology and imaging, and nanotechnology.
A paper is included if it carries any of these subject tags.

### Cleaning and derived variables

Publication and retraction dates were parsed to compute **time to retraction** in years.
The approximately ninety raw reason codes were collapsed into thirteen interpretable
categories (for example, *Data and Results Issues*, *Peer Review and Editorial Issues*,
*Plagiarism and Duplication*). Author counts were derived from the author field, and
primary country from the first listed affiliation. The unfinished current calendar year is
excluded from every figure to avoid an artificial end-of-series dip.

### Citation enrichment

Each paper was matched to a citation count and, where available, the NIH Relative Citation
Ratio from iCite [@Hutchins2016] via its PubMed identifier, and to a citation count and
per-year citation history from OpenAlex [@Priem2022] via its DOI. Per-year counts allow a
pre- versus post-retraction comparison. DOIs are passed to OpenAlex in a single correctly
encoded batched filter; citation matching is incomplete and biased toward indexed journals,
which we treat as a limitation rather than a complete census.

### Reproducibility and the wired-paper format

All computation is performed in a small, versioned data file produced by an open pipeline,
and every figure is rendered client-side from that file. Because the dashboard is a
lightweight client over precomputed results, a correction to the underlying data or code
propagates to the article without rewriting the narrative — a central advantage of the
wired-paper format over static figures [@Bienvenu2026]. The versioned snapshot also makes
the analysis reproducible, which dashboard-style tools over continuously changing databases
often are not.

## Results

The embedded dashboard above is the primary results artifact; the subsections here guide
interpretation. All counts update with the reader's filter selections, so specific numbers
below describe the default view (all four fields, full year range).

### Temporal trends

Annual retraction counts rise over the study period, consistent with both a real increase
and improved detection. The time-to-retraction distribution is right-skewed: most retracted
papers are withdrawn within a couple of years, but a long tail persists in the record for a
decade or more.

### Reasons for retraction

Across the four fields, data- and results-related problems and investigation findings
dominate the reason profile, with peer-review and editorial issues and plagiarism also
prominent. The reason mix is the key explanatory variable for retraction speed (below).

### Geography

Author affiliations span many countries; the map shows counts by country, and the companion
table lists them in rank order. Raw counts are dominated by the largest producers of
biomedical literature and should be read as counts, not rates.

### Authorship and time to retraction

Retraction counts by number of authors are shown alongside the median time to retraction for
each author-count group, as two separate panels so that the count distribution and the
timing trend can each be read cleanly.

### Time to retraction by country, and the role of reason

Median time to retraction varies across countries. However, this variation is largely
accounted for by differences in which reasons dominate in each country: peer-review and
editorial problems are detected quickly everywhere, whereas data-integrity problems take
years everywhere. In our modelling, the stated reason explains far more of the variance in
time-to-retraction than the country of origin does.

### Citation analysis

The citation panels relate a paper's prominence to its retraction. More highly cited papers
tend to take longer to retract — a pattern visible both in the citations-versus-time scatter
(with a smooth trend line) and in the split comparison, where papers above the median
citation count show a substantially higher median time to retraction than those below it.
The post-retraction panel compares citations received before and after the retraction
notice; points above the diagonal are papers that continued to be cited at least as heavily
after retraction as before.

## Limitations

The Retraction Watch Database skews toward English-language, indexed literature, so rates
for non-anglophone systems are likely underestimated, and the data reflect retractions that
were *detected and acted upon* rather than the true prevalence of flawed work. Citation
matching is incomplete and favours prominent journals. The reason categorisation collapses a
fine-grained vocabulary into thirteen labels, and per-paper analyses use the first listed
reason as the primary reason. Time to retraction is measured to the formal notice date,
which lags the point at which problems were first identified.

## Conclusion

Treating four quantitative, imaging-heavy biomedical fields as a comparison set, we find
that the *reason* for retraction, more than the country of origin, governs how quickly the
record is corrected, and that citation prominence is associated with slower retraction. Just
as importantly, presenting the analysis as a wired paper lets readers test these claims
against the data directly, rather than trusting a fixed figure. The dashboard and the full
analysis pipeline are openly available.

+++ {"part": "acknowledgments"}

This article uses the Retraction Watch Database, made available by The Center for Scientific
Integrity through Crossref, and citation data from iCite and OpenAlex. The wired-paper format
and template are the work of Morane Bienvenu and the NeuroLibre project.

+++

---
title: "Retraction patterns in quantitative and imaging-focused biomedical fields"
short_title: Biomedical retraction patterns
numbering:
  headings: true
---

+++ {"part": "abstract"}

Retraction is how science removes flawed work from its record, but it is a slow and uneven
instrument, and the corrected record it leaves behind is itself worth studying. We examine
retractions across four quantitative, data- and image-intensive areas of biomedicine —
neuroscience, biostatistics and epidemiology, radiology and imaging, and nanotechnology —
drawn from the Retraction Watch Database. For each field we ask how many papers were
withdrawn, for what stated reasons, where their authors worked, how long the process took,
and whether a paper's citation record bears any relation to the speed of its correction.
Rather than fixing these questions in static charts, we present the analysis as an
interactive dashboard embedded in the article: every figure can be re-filtered by field,
year, country, reason, authorship, and notice access as the paper is read, and the per-section
figures below stay in step with the master dashboard. Two findings stand out. Time to
retraction depends far more on the stated reason than on the country of origin — editorial and
peer-review problems are resolved quickly almost everywhere, whereas data-integrity cases take
years in every national setting we examined. And the most heavily cited papers tend to persist
longer in the literature before being withdrawn, and to continue accruing citations after the
notice appears. We read these patterns as descriptive rather than causal, and the embedded
tools let readers test them against subsets of their own choosing.

+++

## Introduction

A retraction is meant to be decisive. Once a paper is withdrawn, the expectation is that it
leaves the usable literature, that citations to it taper off, that downstream reviews and
meta-analyses are corrected, and that whatever damage it caused is contained. In practice the
mechanism is far less tidy. Retraction is often slow, it varies in frequency and speed across
fields and countries, and it is incomplete: withdrawn work keeps being cited, sometimes for a
decade or more, and the notices that are supposed to explain what went wrong are frequently
terse, ambiguous, or paywalled [@TeixeiraDaSilva2025; @RetractionWatchDB]. Studying the
pattern of retractions — not any single case — is therefore one of the few empirical windows
onto how well the self-correcting machinery of science actually works.

Most analyses of that pattern do one of two things. They either pool retractions across all of
science, which blurs the very different cultures of, say, clinical trials and materials
chemistry, or they present a fixed set of summary charts that a reader cannot interrogate.
Searchable retraction dashboards have begun to close the second gap — integrated platforms
that map global trends by reason, journal, and country [@Singh2026], and trackers built around
post-retraction citation [@XeraRetractionTracker] — but these are general-purpose tools rather
than arguments about a particular question. What is comparatively rare is a *field-comparative*
account: whether research areas that share a methodological character — a heavy reliance on
quantitative data and on imaging — leave similar retraction signatures, and whether how quickly
a paper is corrected is governed more by where it came from or by what was wrong with it.

This article takes up that question for four such fields, and it does so in a deliberately
interactive form. It is written as a *wired paper* [@Bienvenu2026; @NeuroLibre]: the figures
are produced by live code running in the reader's browser rather than being baked into the
page, so the same figure that supports a claim in the text can be re-filtered to check how far
the claim travels. The complete analysis is available in the dashboard below, and every figure
in the Results section is a view onto that same dashboard — change a filter in one and the rest
follow.

### The interactive analysis

The dashboard below is the primary artifact of this paper. The controls at the top filter every
tab at once by subject area, retraction-year range, reason, country, author count,
collaboration type, and whether the retraction notice is open or paywalled; the tabs move
between counts, timing, reasons, geography, venues, and the two citation views. Everything is
computed in the browser from a small versioned data file, so there is nothing to install.

```{iframe} https://sebrm2.github.io/retraction-analysis/?app=1&v=15
:width: 100%
:class: dash-embed
:label: dashboard
```

Every figure in the Results section is a single tab of this dashboard, and all of them share
the same filter state. Setting the subject to *neuroscience* in the dashboard, for instance,
updates each figure below to match, and vice versa.

:::{note} Prefer a full window?
The dashboard also runs as a standalone page:
[**Open the dashboard in a new tab →**](https://sebrm2.github.io/retraction-analysis/?v=15)
:::

## Methods

### Data source and scope

Records were drawn from the Retraction Watch Database, maintained by The Center for Scientific
Integrity and distributed through Crossref [@RetractionWatchDB]. We kept only notices whose
nature is a *retraction*, excluding corrections, expressions of concern, and reinstatements,
and we restricted the set to four subject areas as tagged by Retraction Watch: neuroscience,
biostatistics and epidemiology, radiology and imaging, and nanotechnology. A paper enters the
analysis if it carries any of these tags, so a multidisciplinary paper may appear under more
than one field; the tabs that break results down by field account for this rather than forcing
each paper into a single bin.

### Cleaning and derived variables

Publication and retraction dates were parsed to the year and used to compute **time to
retraction** in years. Retraction Watch records reasons as a long controlled vocabulary of
roughly ninety codes; we collapsed these into thirteen interpretable categories — for example
*Data and Results Issues*, *Peer Review and Editorial Issues*, and *Plagiarism and
Duplication* — so that the reason profile is legible without discarding the distinctions that
matter for interpretation. A paper usually carries several reason codes, and in the reason
figure it is counted once under each category it bears; per-paper summaries that need a single
reason use the first listed one. Author counts come from the author field, and a paper's
country from its listed affiliations, with a paper attributed to each distinct country it
involves. Because the current calendar year is always incomplete at the time of analysis, it is
dropped from every time series to avoid a spurious end-of-record dip.

### Citation enrichment

Where a paper could be matched, we attached a citation count and, when available, the NIH
Relative Citation Ratio from iCite via its PubMed identifier [@Hutchins2016], and a citation
count with a per-year citation history from OpenAlex via its DOI [@Priem2022]. The per-year
history is what makes a before-versus-after comparison possible around the retraction date.
This matching is deliberately conservative — DOIs are sent to OpenAlex in a single correctly
encoded batched query — and it is incomplete: coverage is better for indexed, English-language
journals, so the citation views describe the matched subset rather than a complete census, a
point we return to in the limitations.

### Reproducibility and the interactive format

All computation happens in one small, versioned data file produced by an open pipeline, and
every figure is rendered client-side from that file. Because the article is a thin client over
precomputed results, correcting the underlying data or code propagates to every figure without
anyone rewriting the prose — the practical payoff of the wired-paper format over static images
[@Bienvenu2026]. The versioned snapshot also makes the analysis reproducible in a way that
live queries against a continuously updated database are not: the figures in this paper refer
to a fixed extract, even as Retraction Watch itself keeps growing.

## Results

The embedded dashboard is the full results artifact; the subsections here walk through it and
point to what we think matters. Because every figure re-computes with the reader's filter
selections, the specific numbers quoted below describe the default view — all four fields, the
full year range, no other filter applied — and will change as soon as a filter is set.

### Scale and field comparison

Across the four fields the extract holds on the order of five thousand retracted papers, and
the annual count climbs over the study period, with a pronounced rise in the last few years
(Figure 1). We read this as a mixture of two things that the data cannot separate: a
genuine increase in retractions and a sharpening of the community's ability to detect and act
on problems. The four fields differ in volume and, more interestingly, in tempo — the
by-field panels show that the median time to retraction is not the same across them, which is
the first hint that *what* a field tends to get wrong, more than the field label itself, drives
how fast it is corrected.

```{iframe} https://sebrm2.github.io/retraction-analysis/?fig=overview&v=15
:width: 100%
:class: fig-embed fig-overview
:label: fig-overview
```

**Figure 1.** Scale and field comparison: headline counts, annual retractions, and the count
and median time to retraction for each of the four fields. Interactive and synced to the
dashboard above.

### Timing and authorship

The time-to-retraction distribution is sharply right-skewed (Figure 2): most retracted
papers leave the record within a couple of years, but a long tail lingers for a decade or
longer, and it is this tail that does the lasting damage to downstream work. Breaking the same
papers down by number of authors shows that retractions are not confined to small teams or to
large ones; the count rises and falls with the ordinary authorship distribution of the fields,
and the median time to retraction is fairly flat across team sizes, giving little support to
the idea that collaboration scale by itself predicts how quickly a problem surfaces.

```{iframe} https://sebrm2.github.io/retraction-analysis/?fig=time&v=15
:width: 100%
:class: fig-embed fig-time
:label: fig-time
```

**Figure 2.** Timing and authorship: the distribution of time to retraction, the number of
retractions by author-count group, and the median time to retraction within each group.

### Reasons for retraction

Problems with the data and results themselves, together with the findings of formal
investigations, dominate the reason profile, with peer-review and editorial failures and
plagiarism also prominent (Figure 3). The exact ordering shifts as the fields are
filtered one at a time, but the top of the list is stable: these are fields in which the
integrity of quantitative and image data is the thing most often found wanting. The reason mix
turns out to be the single most useful variable for interpreting retraction speed, which is why
it reappears in the geography and citation sections below.

```{iframe} https://sebrm2.github.io/retraction-analysis/?fig=reasons&v=15
:width: 100%
:class: fig-embed fig-reasons
:label: fig-reasons
```

**Figure 3.** Reasons for retraction, as counts or as a share of papers. A paper may carry
several reasons and is counted once under each.

### Geography

Author affiliations span many countries (Figure 4). The map and its companion table are
counts, not rates, so they are dominated by the countries that simply publish the most
biomedical research, and they should be read that way: a high position reflects output as much
as conduct. Normalising by national publication volume — which the raw Retraction Watch extract
does not support directly — would be needed before any country could fairly be called an
outlier, and we are careful not to make that leap here.

```{iframe} https://sebrm2.github.io/retraction-analysis/?fig=map&v=15
:width: 100%
:class: fig-embed fig-map
:label: fig-map
```

**Figure 4.** Retractions by country of author affiliation, with a ranked table. Counts, not
per-capita or per-paper rates.

### Journals, publishers, and national timing

Retractions concentrate in a recognisable set of journals and publishers (Figure 5),
several of which have been the subject of large, publicised integrity actions, so their
prominence here is unsurprising. The third panel is the one we find most informative: the
median time to retraction for the fastest and slowest countries differs by years, not months.
Read alongside the reasons figure, this spread is better explained by *what* dominates in each
country than by the country itself — places where editorial and peer-review problems make up a
large share resolve quickly, while those where data-integrity cases dominate are slow, because
those cases are slow everywhere.

```{iframe} https://sebrm2.github.io/retraction-analysis/?fig=venues&v=15
:width: 100%
:class: fig-embed fig-venues
:label: fig-venues
```

**Figure 5.** Journals and publishers with the most retractions in the selection, and the
fastest and slowest countries by median time to retraction.

### Citation profile and retraction speed

For the subset of papers we could match to citation data, prominence and correction speed move
together in a direction worth dwelling on: more heavily cited papers tend to take *longer* to
retract, not shorter (Figure 6). The pattern is visible both in the scatter of
citations against time to retraction, with its smoothed trend, and in the velocity view that
normalises for how long a paper has been in circulation. One reading is uncomfortable but
plausible — that the papers doing the most to shape a field are also the ones the field is
slowest to disown.

```{iframe} https://sebrm2.github.io/retraction-analysis/?fig=citations&v=15
:width: 100%
:class: fig-embed fig-citations
:label: fig-citations
```

**Figure 6.** Citations versus time to retraction, and citation velocity versus time to
retraction, for papers matched to citation data.

### Post-retraction citation and impact

Splitting the matched papers at the median citation count makes the same point more bluntly:
the more-cited half shows a substantially higher median time to retraction than the less-cited
half (Figure 7). The second panel tracks what happens after the notice appears. Many
papers sit near or above the diagonal, meaning they continued to be cited about as heavily, or
more heavily, after retraction as before — the persistence of post-retraction citation that a
growing literature has flagged as a direct threat to the integrity of downstream work
[@TeixeiraDaSilva2025].

```{iframe} https://sebrm2.github.io/retraction-analysis/?fig=impact&v=15
:width: 100%
:class: fig-embed fig-impact
:label: fig-impact
```

**Figure 7.** Time to retraction for low- versus high-citation papers, and citations received
before versus after the retraction notice.

## Discussion

Taken together, the four fields tell a reasonably coherent story. The reason a paper is
retracted is the best single predictor we have of how quickly the record is put right: problems
that an editor or reviewer can adjudicate are handled in months, while problems that require
re-examining the underlying data or image evidence drag on for years, and this holds across
national settings rather than being a property of any one country. The apparent differences
between countries in retraction speed largely dissolve once the reason mix is taken into
account — a point we make descriptively, from the figures, rather than from a fitted model, and
one that the embedded tools invite readers to probe field by field and country by country.

The citation findings are the ones with the sharpest practical edge. That more heavily cited
papers are slower to retract, and that retracted papers keep being cited afterwards, together
describe a literature that is worst at correcting exactly the work that has spread furthest.
This is consistent with the broader concern that uncorrected citation of retracted work
propagates error through the citing network long after the formal notice [@TeixeiraDaSilva2025],
and it suggests that the value of faster, clearer, and openly accessible retraction notices is
greatest precisely for high-impact papers. The share of notices that are themselves paywalled —
which readers can isolate with the notice-access filter — is relevant here, since a warning that
sits behind a paywall is a warning many citing authors will never see.

We want to be clear about what these results are not. They are associations in a convenience
sample of papers that were *detected and acted upon*, not estimates of the true rate or true
causes of flawed work, and nothing here identifies a mechanism. The interactive format is part
of the argument rather than decoration: because any reader can re-slice the data, the claims
above are offered as ones that should survive reasonable re-filtering, and are easy to falsify
if they do not.

### Limitations

Several limitations bound these conclusions. The Retraction Watch Database leans toward
English-language, indexed literature, so retractions in non-anglophone and less-indexed venues
are almost certainly undercounted, and the whole dataset reflects detection and action rather
than the underlying prevalence of problems. The geographic figures are raw counts and are
dominated by the largest producers of research; without normalisation by national output they
cannot be read as rates. Citation matching is incomplete and biased toward prominent,
well-indexed journals, so the citation and post-retraction views describe the matched subset
and likely understate citation to less-visible retracted work. Collapsing roughly ninety reason
codes into thirteen categories trades some granularity for legibility, and per-paper analyses
that need a single reason use the first listed one, which can under-represent secondary causes.
Finally, time to retraction is measured to the formal notice date, which lags — sometimes by
years — the point at which a problem was first identified, so our timing results describe the
speed of the *public* correction, not of the investigation behind it.

## Conclusion

Treating four quantitative, imaging-heavy biomedical fields as a comparison set, we find that
the reason for retraction, more than the country of origin, governs how quickly the record is
corrected, and that citation prominence is associated with slower retraction and with continued
citation after the fact. Presenting the analysis as a wired paper lets a reader test each of
these claims against the slice of the data they care about, rather than taking a fixed figure
on trust. Both the dashboard and the analysis pipeline behind it are openly available.

+++ {"part": "acknowledgments"}

This article uses the Retraction Watch Database, made available by The Center for Scientific
Integrity through Crossref, with citation data from iCite and OpenAlex. The wired-paper format
and template are the work of Morane Bienvenu and the NeuroLibre project.

+++

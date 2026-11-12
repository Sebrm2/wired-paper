---
title: "Retraction patterns in quantitative and imaging-focused biomedical fields"
short_title: Biomedical retraction patterns
numbering:
  headings: true
---

+++ {"part": "abstract"}

Retraction is the main mechanism for removing flawed work from the scientific record, but it is
often slow, uneven across fields and countries, and incomplete. I analysed retracted
publications in four quantitative, data- and image-intensive areas of biomedicine: neuroscience,
biostatistics and epidemiology, radiology and imaging, and nanotechnology, using the Retraction
Watch Database. For each field I quantified how many papers were retracted, the stated reasons,
the countries of the authors' affiliations, the time between publication and retraction, and the
relationship between a paper's citation profile and how quickly it was retracted. Rather than
presenting a fixed set of figures, the analysis is presented as an interactive dashboard
embedded in the article, and every figure in the Results can be re-filtered by field, year,
country, reason, authorship, and notice access as the paper is read. Two results were consistent
across the four fields. Time to retraction depended more on the stated reason than on the
country of origin: editorial and peer-review problems were resolved quickly in most countries,
whereas data-integrity problems took years in every national setting examined. More heavily
cited papers also tended to remain in the literature longer before being retracted, and to
continue accumulating citations after the retraction notice appeared. I interpret these patterns
as descriptive associations rather than causal effects, and the embedded tools allow readers to
test them against subsets of their own choosing.

+++

## Introduction

A retraction is intended to remove a paper from active use. Once a paper is withdrawn, citations
to it are expected to stop, downstream reviews and meta-analyses are expected to be corrected,
and the error it introduced is expected to be contained. In practice the process is much less
clean. Retraction is often slow, it varies in frequency and speed across fields and countries,
and it is incomplete, because withdrawn work continues to be cited for years and the notices
that are meant to explain the reason for retraction are frequently short, ambiguous, or behind a
paywall [@TeixeiraDaSilva2025; @RetractionWatchDB]. Studying the pattern of retractions across
many papers, rather than any single case, is therefore one of the few empirical ways to assess
how well the self-correcting mechanisms of science actually work.

Most analyses of the retraction record take one of two approaches. They either pool retractions
across all of science, which mixes together fields with very different research cultures, or
they present a fixed set of summary figures that the reader cannot interrogate. Searchable
retraction dashboards have started to address the second limitation, including platforms that
map global trends by reason, journal, and country [@Singh2026] and trackers built around
post-retraction citation [@XeraRetractionTracker]. What is less common is a field-comparative
analysis that asks whether research areas sharing a methodological character, in this case a
heavy reliance on quantitative data and on imaging, show similar retraction patterns, and
whether the speed of retraction is governed more by where the work came from or by what was
wrong with it.

This article addresses that question for four such fields, and it does so in an interactive
form. It is written as a wired paper [@Bienvenu2026; @NeuroLibre], meaning that the figures are
produced by live code running in the reader's browser rather than saved as static images. The
same figure that supports a statement in the text can be re-filtered to check whether the
statement still holds in a subset. The complete analysis is contained in the dashboard below,
and every figure in the Results section is a view of one tab of that dashboard. Changing a
filter in one figure updates the others.

### The interactive analysis

The dashboard below is the main artifact of this paper. The controls at the top filter every tab
at once by subject area, retraction-year range, reason, country, author count, collaboration
type, and whether the retraction notice is open or paywalled. The tabs move between counts,
timing, reasons, geography, venues, and the two citation views. Everything is computed in the
browser from a small versioned data file, so there is nothing to install.

```{iframe} https://sebrm2.github.io/retraction-analysis/?app=1&v=15
:width: 100%
:class: dash-embed
:label: dashboard
```

Every figure in the Results section is a single tab of this dashboard, and all of them share the
same filter state. Setting the subject to neuroscience in the dashboard, for example, updates
each figure below to match, and the reverse also holds.

:::{note} Prefer a full window?
The dashboard also runs as a standalone page:
[**Open the dashboard in a new tab →**](https://sebrm2.github.io/retraction-analysis/?v=15)
:::

## Methods

### Data source and scope

I used records from the Retraction Watch Database, maintained by The Center for Scientific
Integrity and distributed through Crossref [@RetractionWatchDB]. I kept only notices whose nature
is a retraction, excluding corrections, expressions of concern, and reinstatements, and I
restricted the set to four subject areas as tagged by Retraction Watch: neuroscience,
biostatistics and epidemiology, radiology and imaging, and nanotechnology. A paper was included
if it carried any of these tags, so a paper tagged with more than one field can appear under
each of them. The figures that break results down by field account for this rather than forcing
each paper into a single category.

### Cleaning and derived variables

Publication and retraction dates were parsed to the year and used to compute time to retraction
in years. Retraction Watch records reasons as a controlled vocabulary of roughly ninety codes,
which I collapsed into thirteen interpretable categories, for example Data and Results Issues,
Peer Review and Editorial Issues, and Plagiarism and Duplication, so that the reason profile is
readable without losing the distinctions that matter for interpretation. A paper usually carries
several reason codes, and in the reason figure it is counted once under each category it bears.
Per-paper summaries that require a single reason use the first listed one. Author counts were
derived from the author field, and a paper's country from its listed affiliations, with the
paper attributed to each distinct country it involves. Because the current calendar year is
always incomplete at the time of analysis, it was dropped from every time series to avoid a
spurious drop at the end of the record.

### Citation enrichment

Where a paper could be matched, I attached a citation count and, when available, the NIH
Relative Citation Ratio from iCite via its PubMed identifier [@Hutchins2016], and a citation
count with a per-year citation history from OpenAlex via its DOI [@Priem2022]. The per-year
history is what makes a before-and-after comparison possible around the retraction date. This
matching is deliberately conservative, with DOIs sent to OpenAlex in a single correctly encoded
batched query, and it is incomplete. Coverage is better for indexed, English-language journals,
so the citation views describe the matched subset rather than a complete census, a point I
return to in the limitations.

### Reproducibility and the interactive format

All computation is performed in one small, versioned data file produced by an open pipeline, and
every figure is rendered in the browser from that file. Because the article is a thin client
over precomputed results, correcting the underlying data or code propagates to every figure
without rewriting the text, which is the main practical advantage of the wired-paper format over
static images [@Bienvenu2026]. The versioned snapshot also makes the analysis reproducible in a
way that live queries against a continuously updated database are not, since the figures refer to
a fixed extract even as Retraction Watch itself keeps growing.

## Results

The embedded dashboard is the full results artifact, and the subsections below walk through it.
Because every figure re-computes with the reader's filter selections, the specific numbers quoted
below describe the default view, which is all four fields, the full year range, and no other
filter applied. These numbers change as soon as a filter is set.

### Scale and field comparison

Across the four fields the extract contains approximately five thousand retracted papers, and the
annual count rises over the study period, with a marked increase in the most recent years
(Figure 1). This likely reflects a combination of two things that the data cannot separate: a
genuine increase in retractions and an improvement in the community's ability to detect and act
on problems. The four fields differ in volume and in tempo, and the by-field panels show that
the median time to retraction is not the same across them. This is the first indication that
what a field tends to get wrong, more than the field label itself, drives how quickly it is
corrected.

```{iframe} https://sebrm2.github.io/retraction-analysis/?fig=overview&v=15
:width: 100%
:class: fig-embed fig-overview
:label: fig-overview
```

**Figure 1.** Scale and field comparison: headline counts, annual retractions, and the count and
median time to retraction for each of the four fields. Interactive and synced to the dashboard
above.

### Timing and authorship

The time-to-retraction distribution is strongly right-skewed (Figure 2). Most retracted papers
leave the record within a couple of years, but a long tail remains for a decade or longer, and
this tail is the part that does lasting damage to downstream work. Breaking the same papers down
by number of authors shows that retractions are not concentrated in small or large teams. The
count rises and falls with the ordinary authorship distribution of the fields, and the median
time to retraction is fairly flat across team sizes, which gives little support to the idea that
collaboration scale by itself predicts how quickly a problem is found.

```{iframe} https://sebrm2.github.io/retraction-analysis/?fig=time&v=15
:width: 100%
:class: fig-embed fig-time
:label: fig-time
```

**Figure 2.** Timing and authorship: the distribution of time to retraction, the number of
retractions by author-count group, and the median time to retraction within each group.

### Reasons for retraction

Problems with the data and results themselves, together with the findings of formal
investigations, dominate the reason profile, and peer-review and editorial problems and
plagiarism are also common (Figure 3). The exact ordering shifts when the fields are filtered one
at a time, but the top of the list is stable. These are fields in which the integrity of
quantitative and image data is the thing most often found wanting. The reason mix turns out to be
the most useful single variable for interpreting retraction speed, which is why it reappears in
the geography and citation sections below.

```{iframe} https://sebrm2.github.io/retraction-analysis/?fig=reasons&v=15
:width: 100%
:class: fig-embed fig-reasons
:label: fig-reasons
```

**Figure 3.** Reasons for retraction, shown as counts or as a share of papers. A paper may carry
several reasons and is counted once under each.

### Geography

Author affiliations span many countries (Figure 4). The map and the companion table are counts,
not rates, so they are dominated by the countries that publish the most biomedical research and
should be read accordingly. A high position reflects research output as much as conduct.
Normalising by national publication volume, which the raw Retraction Watch extract does not
support directly, would be needed before any country could fairly be called an outlier, so I do
not make that comparison here.

```{iframe} https://sebrm2.github.io/retraction-analysis/?fig=map&v=15
:width: 100%
:class: fig-embed fig-map
:label: fig-map
```

**Figure 4.** Retractions by country of author affiliation, with a ranked table. These are
counts, not per-capita or per-paper rates.

### Journals, publishers, and national timing

Retractions concentrate in a recognisable set of journals and publishers (Figure 5), several of
which have been the subject of large, publicised integrity actions, so their prominence here is
expected. The third panel is the most informative one. The median time to retraction for the
fastest and slowest countries differs by years, not months. Read together with the reasons
figure, this spread is better explained by what dominates in each country than by the country
itself. Countries where editorial and peer-review problems make up a large share resolve
quickly, and countries where data-integrity problems dominate are slow, because those problems
are slow to resolve everywhere.

```{iframe} https://sebrm2.github.io/retraction-analysis/?fig=venues&v=15
:width: 100%
:class: fig-embed fig-venues
:label: fig-venues
```

**Figure 5.** Journals and publishers with the most retractions in the selection, and the
fastest and slowest countries by median time to retraction.

### Citation profile and retraction speed

For the subset of papers I could match to citation data, prominence and correction speed move
together in a direction worth noting: more heavily cited papers tend to take longer to retract,
not shorter (Figure 6). The pattern is visible both in the scatter of citations against time to
retraction, with its smoothed trend, and in the velocity view, which normalises for how long a
paper has been in circulation. One interpretation is that the papers doing the most to shape a
field are also the ones the field is slowest to withdraw.

```{iframe} https://sebrm2.github.io/retraction-analysis/?fig=citations&v=15
:width: 100%
:class: fig-embed fig-citations
:label: fig-citations
```

**Figure 6.** Citations versus time to retraction, and citation velocity versus time to
retraction, for papers matched to citation data.

### Post-retraction citation and impact

Splitting the matched papers at the median citation count makes the same point more directly. The
more-cited half shows a substantially higher median time to retraction than the less-cited half
(Figure 7). The second panel tracks what happens after the notice appears. Many papers sit near
or above the diagonal, meaning they continued to be cited about as heavily, or more heavily,
after retraction as before. This persistence of post-retraction citation has been described as a
direct threat to the integrity of downstream work [@TeixeiraDaSilva2025].

```{iframe} https://sebrm2.github.io/retraction-analysis/?fig=impact&v=15
:width: 100%
:class: fig-embed fig-impact
:label: fig-impact
```

**Figure 7.** Time to retraction for low- versus high-citation papers, and citations received
before versus after the retraction notice.

## Discussion

Taken together, the four fields give a fairly consistent picture. The reason a paper is retracted
is the best single predictor of how quickly the record is corrected. Problems that an editor or
reviewer can adjudicate are handled in months, while problems that require re-examining the
underlying data or image evidence take years, and this holds across national settings rather than
being a property of any one country. The apparent differences between countries in retraction
speed largely disappear once the reason mix is taken into account. I make this point
descriptively, from the figures, rather than from a fitted model, and the embedded tools let
readers check it field by field and country by country.

The citation findings have the clearest practical implication. The fact that more heavily cited
papers are slower to retract, and that retracted papers keep being cited afterwards, together
describe a literature that is least effective at correcting exactly the work that has spread the
furthest. This is consistent with the broader concern that uncorrected citation of retracted work
propagates error through the citing network long after the formal notice [@TeixeiraDaSilva2025],
and it suggests that faster, clearer, and openly accessible retraction notices matter most for
high-impact papers. The share of notices that are themselves paywalled, which readers can isolate
with the notice-access filter, is relevant here, because a notice behind a paywall is one that
many citing authors will not see.

It is important to be clear about what these results are and are not. They are associations in a
set of papers that were detected and acted upon, not estimates of the true rate or the true
causes of flawed work, and none of the analyses identifies a mechanism. The interactive format is
part of the argument rather than decoration. Because any reader can re-slice the data, the
statements above are offered as ones that should survive reasonable re-filtering, and they are
easy to disprove if they do not.

### Limitations

Several limitations apply. The Retraction Watch Database leans toward English-language, indexed
literature, so retractions in non-anglophone and less-indexed venues are likely undercounted, and
the dataset as a whole reflects detection and action rather than the underlying prevalence of
flawed work. The geographic figures are raw counts and are dominated by the largest producers of
research, so without normalisation by national output they cannot be read as rates. Citation
matching is incomplete and biased toward prominent, well-indexed journals, so the citation and
post-retraction views describe the matched subset and probably understate citation to
less-visible retracted work. Collapsing roughly ninety reason codes into thirteen categories
trades some detail for readability, and per-paper analyses that need a single reason use the
first listed one, which can under-represent secondary causes. Finally, time to retraction is
measured to the formal notice date, which lags the point at which a problem was first identified,
sometimes by years, so the timing results describe the speed of the public correction rather than
of the investigation behind it.

## Conclusion

Treating four quantitative, imaging-heavy biomedical fields as a comparison set, I find that the
reason for retraction, more than the country of origin, governs how quickly the record is
corrected, and that citation prominence is associated with slower retraction and with continued
citation after the fact. Presenting the analysis as a wired paper lets the reader test each of
these statements against the part of the data they care about, rather than relying on a fixed
figure. Both the dashboard and the analysis pipeline behind it are openly available.

+++ {"part": "acknowledgments"}

This article uses the Retraction Watch Database, made available by The Center for Scientific
Integrity through Crossref, with citation data from iCite and OpenAlex. The wired-paper format
and template are the work of Morane Bienvenu and the NeuroLibre project.

+++

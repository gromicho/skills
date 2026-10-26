---
name: amsterdam-abs-journal-points
description: Assess journal categories, publication points and journal targets under Amsterdam Business School research criteria. Use for UvA ABS journal lists, A*/A/M/B points, non-core JCR classification or research-output norms; distinguish these from the British Chartered ABS Academic Journal Guide.
---

# Amsterdam Business School journal points

For Amsterdam/UvA research context, distinguish Amsterdam Business School from Chartered ABS/AJG before grading. If the request is ambiguous, clarify the institution. AJG1–4* grades and Scopus/SJR quartiles do not determine Amsterdam ABS points.

## Sources and currency

Use the [official ABS research-policy page](https://abs.uva.nl/research/research-policy-ethics--integrity/research-policy-ethics--integrity.html) to obtain the applicable criteria and journal list. The2026 policy/list formed the initial reference for these instructions. See [source notes](references/sources.md). This is independent guidance, not an official UvA policy or eligibility determination.

No journal workbook or email attachment is distributed here. Obtain the official list yourself, keep it local, and supply its path to the lookup helper. Check currency for current/future decisions and state the actual version used. Official documents prevail over this workflow or a supplied summary. Do not extrapolate2026 rules to future years.

## Listed journals

Search the locally supplied official workbook directly. The stdlib-only helper searches journal titles and returns exact source rows:

    python scripts/lookup_journal.py "European Journal of Operational Research" --list /path/to/abs-journal-list-2026-1.xlsx

Use the returned exact journal title and category; verify ambiguities, renamed journals and ISSNs against available evidence. A missing search hit means unlisted/unresolved, not automatically zero. The list's category controls without substituting citation metrics:

| Category | Full-length research article points |
|---|---:|
| A* |200|
| A |100|
| M |100|
| B |50|

The list uses "Journal on Computing" for INFORMS Journal on Computing. Do not confuse it with similarly named computing journals. Explain journal prestige/fit separately from institutional points: EJOR, Computers & Operations Research and Journal on Computing are all A in the inspected2026-1 list, so the points system alone does not rank those targets.

## Unlisted journals

Do not grade from two-year JIF, quartiles, CiteScore, SJR, AIS or AJG. Under the supplied explanation, obtain the applicable JCR year's **five-year JIF rank** and full ranked denominator for every subject category. Use rank/number of journals with five-year JIF, then apply the institution's category-combination rule. The supplied2026 working explanation uses an unweighted average across categories; the official wording says combined categories without detailing that arithmetic, so verify this interpretation for formal assessments. Retain the year, categories, ranks, denominators and calculation. Do not infer this rank merely from the five-year JIF value.

- For unlisted journals outside business/management/finance: average position <=10% gives non-core A*200; <=20% A100; <=60% B50; otherwise0, subject to applicable official policy.
- For unlisted journals in JCR Business, Management or Business, Finance: the explanation's special route gives **core A100 only at top20%**; it does not yield A* or B. Check all actual categories before choosing a route. Do not assume an OR title is outside Management.
- ITOR is absent from the inspected2026-1 list and has been reported in Management as well as OR&MS. Its points remain unresolved until the applicable categories and five-year ranks are verified. Its Q1/SJR or Q2/JCR standing is insufficient.
- If JCR access/ranks are unavailable, report "not established" and the exact missing evidence. Do not invent a rank, assign zero solely because the journal is absent, or substitute a ranking system.

The2026 official criteria tie assessment to February after official print/issue publication and the applicable JCR data year, with2026 print ordinarily mapped to JCR2025 in the supplied workflow; confirm the edition actually used by the annual report. Online-first alone does not select the print year. Verify official policy for boundary cases and future-year assessments.

## Publication and portfolio assessment

Read the applicable official criteria and any supplied explanation for staff norms, conference exceptions, affiliation and exceptions; do not apply staff research-time rules to students or other appointment types by default. For full papers, the supplied note says points do not depend on author position/count. Non-research items and disputed cases need institutional determination, not an invented automatic rule.

For the note's50% research-time norm:400 total points over five years, including300 from A*/A/M, with A/M not all from one journal. B contributes to total but not that quality subtotal. Keep productivity and quality separate; apply appointment scaling/exceptions only with supporting facts.

Answer with journal, source-list version, category, points and verification status. For target recommendations, distinguish scientific fit and demonstrated contribution from points, and distinguish established evidence from aspirational journal placement. Cite source files/rows and any official policy/JCR evidence actually consulted. Reading/classifying does not authorize email, uploads or submissions.

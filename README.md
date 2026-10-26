# Skills for Codex and Claude

Reusable agent skills maintained by [Joaquim Gromicho](https://github.com/gromicho).

## Available skills

| Skill | Purpose |
|---|---|
| [amsterdam-abs-journal-points](skills/amsterdam-abs-journal-points/SKILL.md) | Assess Amsterdam Business School journal categories and publication points, without confusing them with British Chartered ABS/AJG ratings. |

## Install

Copy an individual skill directory, including its supporting files, into:

- Codex: `~/.codex/skills/`
- Claude Code: `~/.claude/skills/`

For the first skill, the installed directory should be named `amsterdam-abs-journal-points`. Invoke by name or ask about Amsterdam Business School journal points. Discovery depends on your client/session.

The same `SKILL.md` works in both clients. The lookup helper uses Python3 standard-library modules only. Obtain the official journal workbook separately:

```sh
python scripts/lookup_journal.py "European Journal of Operational Research" --list /path/to/abs-journal-list-2026-1.xlsx
```

This repository contains independent guidance and code, not official institutional policy. Check the applicable sources and publication year. Third-party documents and private local references are not bundled and are not covered by this repository's MIT license.

## Contributing

Keep skills focused and portable. Cite official sources, distinguish verified facts from interpretations, and exclude credentials, personal data and institution-provided attachments. Include meaningful checks for executable helpers.

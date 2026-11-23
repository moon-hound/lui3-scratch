<!-- page details (read by the checker; hidden when reading)
id: log
title: Guide change log
layer: meta
type: reference
status: draft
covers: []
covers_hash: null
verified_on: null
verified_by: null
sources: []
-->

# Guide change log

Append only. One line per change: date, page, what changed, why (command-log row).

| Date | Page | What | Source |
|---|---|---|---|
| 2026-11-22 | [[README]], [[index]], [[log]], template | Batch 0 skeleton created | log #174 |
| 2026-11-22 | [[part-b-github-locks]], [[c7-locked-paths]], [[c8-test-vm]], [[test-vm-will-not-start]], glossary pages | Trial pages written (draft) | log #174 |
| 2026-11-22 | [[glossary]], [[test-vm]], [[pf]], [[checkrunner]], [[builder]], [[acl]], [[main-branch]], [[pull-request]] | Glossary pages created (named here so every page appears in this log) | log #174 |
| 2026-11-22 | [[watchdog]], [[colima-lima]], [[loopback]], [[snapshot]] | Glossary pages created | log #175 |
| 2026-11-22 | [[part-b-github-locks]], [[c7-locked-paths]], [[c8-test-vm]], [[test-vm-will-not-start]], [[README]], glossary | 24 reviewer fixes; troubleshooting rebuilt from the watchdog's real messages; 4 new glossary words | log #175 |
| 2026-11-22 | all pages | Page details moved into a hidden comment so viewers show the title, not the details | log #176 |
| 2026-11-22 | [[c7-locked-paths]], [[test-vm-will-not-start]], [[c8-test-vm]] | Second review fixes; C8 picture redrawn as a Mermaid diagram (sample) | log #177 |
| 2026-11-22 | [[README]], [[part-b-github-locks]], [[c7-locked-paths]], [[test-vm-will-not-start]], template | All pictures redrawn as Mermaid diagrams (Jax: "looks good" on the C8 sample) | log #178 |
| 2026-11-22 | [[c8-test-vm]], [[c7-locked-paths]], [[part-b-github-locks]], template | "Exact details (for agents)" table added; checker now requires it on build pages | log #179 |
| 2026-11-22 | [[c8-test-vm]], [[c7-locked-paths]], [[part-b-github-locks]] | Fact-check fixes to the agent tables (missing paths, logs, fingerprints, token expiry) | log #180 |
| 2026-11-22 | [[c7-locked-paths]], [[c8-test-vm]], [[part-b-github-locks]], [[test-vm-will-not-start]], [[README]], template | All technical parts grouped in one last section "For agents: technical details" | log #182 |
| 2026-11-22 | all content pages, [[README]] | Same last section with the table first on every content page (glossary and troubleshooting added); checker enforces the position | log #183 |
| 2026-11-22 | all pages, [[README]] | Rules audit: `AGENTS.md` added as the one rules file; stronger checker (order, Mermaid, STOP, sources, labels, log, covers_hash); every page stamped | log #184 |
| 2026-11-22 | [[README]] | Guide gate live: Git hook refuses a guide commit with problems; rules file, checker, template, hook and git config locked | log #186 |
| 2026-11-22 | [[snapshot]], [[main-branch]], [[checkrunner]], [[part-b-github-locks]] | Sources made exact (file names) for the stricter checker | log #190 |

## How it connects
- part_of [[index]]

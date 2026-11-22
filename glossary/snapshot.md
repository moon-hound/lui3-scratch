<!-- page details (read by the checker; hidden when reading)
id: snapshot
title: "snapshot (APFS snapshot)"
layer: glossary
type: reference
status: draft
covers: []
covers_hash: null
verified_on: null
verified_by: null
sources: [CLAUDE.md rule 7]
-->

# snapshot (APFS snapshot)

## In plain words
A frozen copy of the Mac Studio's disk at one moment, taken before each risky step, so the Mac can be put back exactly as it was if something goes wrong.

## How it connects
- used_in [[c7-locked-paths]]
- part_of [[glossary]]

## For agents: technical details
*Everything from here down is for agents and for checking facts. You can stop reading here.*

### Exact details (for agents)
| What | Value | Source |
|---|---|---|
| Command | Jax runs `sudo tmutil localsnapshot` on the Studio before each part (STOP: `sudo`) | log #147, `CLAUDE.md` rule 7 |
| Names | date and time, for example `2026-11-21-163616` | log #147 |

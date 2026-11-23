<!-- page details (read by the checker; hidden when reading)
id: pull-request
title: "pull request"
layer: glossary
type: reference
status: draft
covers: []
covers_hash: null
verified_on: null
verified_by: null
sources: [lui3-stage-0-part-b-check-2026-11-17.md]
-->

# pull request

## In plain words
A proposal on GitHub to add a set of changes to the main branch. It shows exactly what would change, runs the automatic checks, and waits for the owner's approval.

## How it connects
- used_in [[part-b-github-locks]]
- part_of [[glossary]]

## For agents: technical details
*Everything from here down is for agents and for checking facts. You can stop reading here.*

### Exact details (for agents)
| What | Value | Source |
|---|---|---|
| Needed for | every change to `main` of `moon-hound/lui3` | log #47 |
| Must have | a passing `gate` check from GitHub Actions and Jax's approval as code owner | log #47, #56 |

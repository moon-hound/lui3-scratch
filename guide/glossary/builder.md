<!-- page details (read by the checker; hidden when reading)
id: builder
title: "builder account"
layer: glossary
type: reference
status: draft
covers: []
covers_hash: null
verified_on: null
verified_by: null
sources: [stage0-command-log.md#88, stage0-command-log.md#93, stage0-command-log.md#113]
-->

# builder account

## In plain words
The user account on the Mac Studio where the AI builder works. It has no administrator rights and can write only where its current job allows; the Studio signs in to it automatically.

## How it connects
- used_in [[c7-locked-paths]]
- used_in [[c8-test-vm]]
- part_of [[glossary]]

## For agents: technical details
*Everything from here down is for agents and for checking facts. You can stop reading here.*

### Exact details (for agents)
| What | Value | Source |
|---|---|---|
| Account | `builder`, UID 502, group staff (20), not an admin, home folder mode 700 | log #88 |
| Sign-in | the Studio signs in to it automatically at boot (J1) | log #93 |
| Write access | only its profile folders in root-owned workspaces, through ACLs | log #113 |

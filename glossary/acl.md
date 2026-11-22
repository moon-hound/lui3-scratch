<!-- page details (read by the checker; hidden when reading)
id: acl
title: "ACL (access control list)"
layer: glossary
type: reference
status: draft
covers: []
verified_on: null
verified_by: null
sources: [stage0-command-log.md#112-#113]
-->

# ACL (access control list)

## In plain words
An extra permission attached to a file or folder that says exactly who may do what with it. C7 uses them to let the builder write into only the folders its job needs.

## How it connects
- used_in [[c7-locked-paths]]
- part_of [[glossary]]

## For agents: technical details
*Everything from here down is for agents and for checking facts. You can stop reading here.*

### Exact details (for agents)
| What | Value | Source |
|---|---|---|
| Used by | `/Library/Lui3/bin/lui3-lock-workspace` on workspaces under `/Library/Lui3/work` | log #113 |
| Profiles | `/Library/Lui3/profiles/` (`drill.txt` today) | `c7/install.sh` |

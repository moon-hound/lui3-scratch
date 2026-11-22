<!-- page details (read by the checker; hidden when reading)
id: test-vm
title: "Test VM"
layer: glossary
type: reference
status: draft
covers: []
verified_on: null
verified_by: null
sources: [stage0-command-log.md#115-#147]
-->

# Test VM

## In plain words
A small Linux computer that runs inside the Mac Studio as a program. The builder's code will be tested there (from C9 on), sealed off from the internet, the home network and the Mac itself.

## How it connects
- used_in [[c8-test-vm]]
- used_in [[test-vm-will-not-start]]
- part_of [[glossary]]

## For agents: technical details
*Everything from here down is for agents and for checking facts. You can stop reading here.*

### Exact details (for agents)
| What | Value | Source |
|---|---|---|
| What it is here | Linux VM run by Colima 0.10.3 on Lima 2.3.0 with Apple Virtualization (VZ); 4 CPU, 8 GiB, no shared folders | progress file, C8 block |
| Owner | `checkrunner` (UID 503) | log #88, C8 |
| Built in | C8, log #115 to #147 | progress file |

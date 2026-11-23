<!-- page details (read by the checker; hidden when reading)
id: pf
title: "pf (packet filter)"
layer: glossary
type: reference
status: draft
covers: []
covers_hash: null
verified_on: null
verified_by: null
sources: [stage0-command-log.md#120-#137]
-->

# pf (packet filter)

## In plain words
The firewall built into macOS. It decides which network traffic is allowed in or out. Our rules say, for example, that the checkrunner account may talk only to its test VM.

## How it connects
- used_in [[c8-test-vm]]
- part_of [[glossary]]

## For agents: technical details
*Everything from here down is for agents and for checking facts. You can stop reading here.*

### Exact details (for agents)
| What | Value | Source |
|---|---|---|
| What it is here | the packet filter built into macOS | DOC, `man pf.conf` on the Studio (#121) |
| Lui3 rules | anchor `com.apple/lui3-vm` (C8 test VM lock, rule file `/etc/pf.anchors/lui3-vm`); anchor `com.apple/lui3-model` (M2, model ports) | `c8/lui3-vm.pf`, log #121 |
| Loaded at boot by | startup jobs `lu.spacedog.lui3.pf-vm` (C8) and `lu.spacedog.lui3.pf-model` (M2) | log #121, #123 |

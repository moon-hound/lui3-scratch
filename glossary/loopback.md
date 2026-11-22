<!-- page details (read by the checker; hidden when reading)
id: loopback
title: "loopback"
layer: glossary
type: reference
status: draft
covers: []
verified_on: null
verified_by: null
sources: [stage0-command-log.md#125, stage0-command-log.md#127]
-->

# loopback

## In plain words
A computer's network connection to itself (the address 127.0.0.1). Programs on the same machine use it to talk to each other without the traffic ever leaving the machine.

## How it connects
- used_in [[c8-test-vm]]
- part_of [[glossary]]

## For agents: technical details
*Everything from here down is for agents and for checking facts. You can stop reading here.*

### Exact details (for agents)
| What | Value | Source |
|---|---|---|
| Address | 127.0.0.1 (IPv6 ::1) | DOC, general |
| Lui3 use | the VM's ssh port 41022 on loopback is the only place `checkrunner` may reach | `c8/lui3-vm.pf`, log #122 |

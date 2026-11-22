<!-- page details (read by the checker; hidden when reading)
id: colima-lima
title: "Colima and Lima"
layer: glossary
type: reference
status: draft
covers: []
verified_on: null
verified_by: null
sources: [stage0-command-log.md#95-#107, c5/versions.env]
-->

# Colima and Lima

## In plain words
Two free tools that run a Linux computer inside a Mac. Lima does the work of running the VM; Colima sits on top of it and sets it up for running containers. We use Colima 0.10.3 and Lima 2.3.0.

## How it connects
- used_in [[c8-test-vm]]
- part_of [[glossary]]

## For agents: technical details
*Everything from here down is for agents and for checking facts. You can stop reading here.*

### Exact details (for agents)
| What | Value | Source |
|---|---|---|
| Versions | Colima 0.10.3, Lima 2.3.0 (locked) | `c5/versions.env` |
| Installed by | C5, root-owned (check 46/0); Lima's tool `/usr/local/bin/limactl` | log #107, #121 |
| Rule | never run Lima as root; never `colima start` by hand (the startup job does it) | progress file, `c8/vm-boot.sh` |

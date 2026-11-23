<!-- page details (read by the checker; hidden when reading)
id: watchdog
title: "watchdog (startup job)"
layer: glossary
type: reference
status: draft
covers: []
covers_hash: null
verified_on: null
verified_by: null
sources: [stage0-command-log.md#139-#147, c8/vm-boot.sh]
-->

# watchdog (startup job)

## In plain words
A small program the Mac starts by itself at boot. It starts the test VM only when the safety lock is in place, then checks every 5 seconds and stops the VM at once if the lock disappears. It writes down why in its log.

## How it connects
- used_in [[c8-test-vm]]
- used_in [[test-vm-will-not-start]]
- part_of [[glossary]]

## For agents: technical details
*Everything from here down is for agents and for checking facts. You can stop reading here.*

### Exact details (for agents)
| What | Value | Source |
|---|---|---|
| Startup job | `lu.spacedog.lui3.vm` (launchd, runs as root) | `c8/lu.spacedog.lui3.vm.plist` |
| Script | `/Library/Lui3/c8/vm-boot.sh`; checks every 5 s | log #139 |
| Log | `/var/log/lui3-vm.log` | `c8/vm-boot.sh` |

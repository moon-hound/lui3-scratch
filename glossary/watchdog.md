<!-- page details (read by the checker; hidden when reading)
id: watchdog
title: "watchdog (startup job)"
layer: glossary
type: reference
status: draft
covers: []
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

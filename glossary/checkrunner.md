<!-- page details (read by the checker; hidden when reading)
id: checkrunner
title: "checkrunner account"
layer: glossary
type: reference
status: draft
covers: []
verified_on: null
verified_by: null
sources: [stage0-command-log.md#88, stage0-command-log.md#120, stage0-command-log.md#122-#147]
-->

# checkrunner account

## In plain words
A separate user account on the Mac Studio with no administrator rights and no network of its own (decision D1, log #120; enforced by the C8 lock, #122 to #147). It owns the test VM. Planned (C9, not built yet): it runs the tests, so the builder never runs them itself.

## How it connects
- used_in [[c8-test-vm]]
- part_of [[glossary]]

---
id: test-vm-will-not-start
title: The test VM will not start
layer: troubleshooting
type: how-to
status: draft
covers: [c8/vm-boot.sh, c8/boot-install.sh, c8/boot-uninstall.sh]
verified_on: null
verified_by: null
sources: [stage0-command-log.md#141-#147, lui3-stage-0-progress.md]
---

# The test VM will not start

## In plain words
The [[test-vm]] is started and watched by a startup job. When it does not run, the job almost always says why in its log, and the reason is usually a safety check doing its job. Read the log first and change nothing until you know which case you are in.

## Picture
```
 VM not running
     |
     v
 read /var/log/lui3-vm.log  (reads only)
     |
     +-- "lock not in force"            -> case 1
     +-- "settings files differ"        -> case 2
     +-- waits at "boot scripts"         -> case 3
     `-- nothing new in the log         -> case 4
```

## If this breaks
- **First safe step (always):** on the Studio, as `lui`, read the last lines of the watchdog log: `sudo tail -n 40 /var/log/lui3-vm.log`. This only reads. Jax types it.
- **Never:** start the VM by hand with `colima start`, or run Lima as root (it refuses, and it bypasses the job's checks).

| Case | What the log says | What it means | Safe next step |
|---|---|---|---|
| 1 | the lock is not in force | the [[pf]] rule is missing, so the watchdog stopped the VM on purpose | find out why the firewall rule is missing (after a macOS update, re-run the checks); do not switch the watchdog off |
| 2 | the VM's settings files differ from the ones pinned at install | a VM setting changed since install; the job refuses to start it | compare before re-pinning; re-pin only through `boot-uninstall.sh` then `boot-install.sh` (both STOP) |
| 3 | stuck at "( 5/5) Boot scripts to be finished" | something inside the VM is waiting for the internet, which the lock blocks | the known cause (Lima's package install) is already switched off; read [[c8-test-vm]] History |
| 4 | nothing new | the job itself is not running | ask the panel to check the job's state read-only |

## How it connects
- depends_on [[c8-test-vm]]
- part_of [[index]]

## Technical facts
- Case 2 happened on 2026-11-21: Colima rewrites `colima.yaml` at every start, so it is now pinned by its values, not its fingerprint (DOC, log #141, #142, #145).
- Case 3 happened on 2026-11-21: Lima's boot script ran `apt-get update`, which the lock blocks; fixed with `skipDefaultDependencyResolution` (DOC, #144, #145).
- After any change to `common.sh`, `vm-boot.sh`, `override.yaml` or the startup plist: `boot-uninstall.sh` then `boot-install.sh` (progress file, C8 run order).

## History (not current instructions)
- Both cases 2 and 3 were found during the first restarts from the startup job (#141 to #145).

## Not verified
- Case 4 has never happened; the steps for it are a plan, not a tested routine.
- The exact log wording for case 1 is taken from the C8 drills, not from a real failure.

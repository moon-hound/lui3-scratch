---
id: c7-locked-paths
title: "C7: locked paths on the Mac Studio"
layer: build
type: explanation
status: draft
covers: [c7/lui3-lock-workspace.sh, c7/profiles/drill.txt, c7/common.sh, c7/install.sh, c7/check.sh, c7/uninstall.sh, lui3-part-c-c7-locked-paths-2026-11-19.md]
verified_on: null
verified_by: null
sources: [lui3-part-c-c7-locked-paths-2026-11-19.md, lui3-stage-0-progress.md, stage0-command-log.md#112, stage0-command-log.md#113]
---

# C7: locked paths on the Mac Studio

## In plain words
The [[builder]] account writes code on the Mac Studio, but some files must be off-limits to it: the rules it follows, the tests that judge its work, and the scripts that check it. C7 makes every workspace owned by the administrator (root) and gives the builder write access only to the folders its current job needs, using [[acl]] permissions. Anything not handed out is locked by default. The test: the builder tried to change 15 locked files and 13 locked folders in every way it could, and every try failed.

## Picture
```
 /Library/Lui3/work/<workspace>     owned by root
   |-- src/        builder may write here (granted by its profile)
   |-- tests/      locked: builder can read, not change
   |-- ci/         locked
   |-- CLAUDE.md   locked
   `-- ...         locked unless the profile grants it

 lock script  /Library/Lui3/bin/lui3-lock-workspace  (root only)
   reads a profile -> grants exactly those folders -> nothing else
```

## If this breaks
- **You notice:** the builder changed a test, a rule file or a check script.
- **First safe step:** stop the builder's session. Do not run anything inside the builder's workspace as root (see the lesson under History).
- **Read next:** `lui3-part-c-c7-locked-paths-2026-11-19.md`, then re-run `c7/check.sh` on the Studio (Jax runs it).

## How it connects
- protects [[builder]]
- part_of [[index]]
- related [[part-b-github-locks]]
- related [[c8-test-vm]]

## Technical facts
- Workspaces are root-owned under `/Library/Lui3/work`; the builder writes only in its profile's folders through ACLs, so every locked path of record row 17.2 is locked by default (DOC, log #112, #113).
- Lock script `/Library/Lui3/bin/lui3-lock-workspace` and `profiles/drill.txt` are root-owned; install record `/var/db/lui3-c7-installed.txt` (DOC, #113).
- Drills on a stand-in workspace: 15 locked files and 13 locked folders could not be written, touched, re-permissioned, given a new ACL or flag, renamed, deleted or added to; the builder's own work and Git commits still worked. Red run 75 pass / 6 fail, then green 81 / 0 (DOC, #112, #113).
- Snapshot before the run: `2026-11-19-175145`. Undo: `c7/uninstall.sh` (deleting class: STOP).
- Rule from C7.1b: nothing privileged reads from `/Users/Shared` or `/tmp` (MINE, from the shared-places check, #113).

## History (not current instructions)
- During the red run, macOS let the builder hard-link root-owned files (even `/private/etc/hosts`) into its `src/` folder (DOC, #113). Lesson: **no privileged tool ever changes owner, rights or flags inside a builder-writable folder**, because it could be acting on a planted link.

## Not verified
- A low-level Git route around the lock is known and accepted (record row 17.7).
- Whether the builder can add a *new* ACL right to a root-owned file in a granted folder (expected no; a later drill, C13).
- The real profiles (interview, test writer, build, proof writer) are written in C10.

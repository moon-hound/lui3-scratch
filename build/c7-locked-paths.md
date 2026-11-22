<!-- page details (read by the checker; hidden when reading)
id: c7-locked-paths
title: "C7: locked paths on the Mac Studio"
layer: build
type: explanation
status: draft
covers: [c7/lui3-lock-workspace.sh, c7/profiles/drill.txt, c7/common.sh, c7/install.sh, c7/check.sh, c7/uninstall.sh, lui3-part-c-c7-locked-paths-2026-11-19.md]
verified_on: null
verified_by: null
sources: [lui3-part-c-c7-locked-paths-2026-11-19.md, lui3-stage-0-progress.md, stage0-command-log.md#112, stage0-command-log.md#113]
-->

# C7: locked paths on the Mac Studio

## In plain words
The [[builder]] account writes code on the Mac Studio, but some files must be off-limits to it: the rules it follows, the tests that judge its work, and the scripts that check it. C7 makes every workspace owned by the administrator (root) and gives the builder write access only to the folders its current job needs, using [[acl]] permissions. Anything not handed out is locked by default. The test: on a stand-in workspace, the builder tried to change 15 locked files and 13 locked folders in every way the drills tried, and every try failed (log #113). One low-level Git route around the lock is known and accepted (record row 17.7).

## Picture
```mermaid
flowchart TD
  LS["Lock script<br/>(root only)"] -- "reads the job's profile,<br/>grants only those folders" --> WS
  subgraph WS["Workspace /Library/Lui3/work/... (owned by root)"]
    SRC["src/<br/>builder may write"]
    GIT[".git/<br/>builder may write<br/>(needed to commit)"]
    TESTS["tests/<br/>locked"]
    CI["ci/<br/>locked"]
    RULES["CLAUDE.md and rules<br/>locked"]
  end
  classDef open fill:#e3f4e1,stroke:#2e7d32,color:#1b5e20
  classDef locked fill:#fde2e2,stroke:#c0392b,color:#7b241c
  class SRC,GIT open
  class TESTS,CI,RULES locked
```

## If this breaks
- **You notice:** the builder changed a test, a rule file or a check script.
- **First safe step:** stop the builder's session. Do not run anything inside the builder's workspace as root (rule under Technical facts).
- **Read next:** `lui3-part-c-c7-locked-paths-2026-11-19.md`; then re-run the checks on the Studio with `sudo sh check.sh` in green mode only, never `red` (STOP label: `sudo`; it creates and removes files in the stand-in workspace, and red mode weakens a lock on purpose).

## How it connects
- protects [[builder]]
- part_of [[index]]
- related [[part-b-github-locks]]
- related [[c8-test-vm]]

## Technical facts
- Workspaces are root-owned under `/Library/Lui3/work`; the builder writes only in its profile's folders (in the drill profile: `src/` and `.git/`) through ACLs, so every locked path of record row 17.2 is locked by default (DOC, log #112, #113).
- Lock script `/Library/Lui3/bin/lui3-lock-workspace` and `profiles/drill.txt` are root-owned; install record `/var/db/lui3-c7-installed.txt` (DOC, #113).
- Drills on the stand-in: 15 locked files and 13 locked folders could not be written, touched, re-permissioned, given a new ACL or flag, renamed, deleted or added to; the builder's own work and Git commits still worked. Red run 75 pass / 6 fail, then green 81 / 0 (DOC, #112, #113).
- **Standing rule (current): no privileged tool ever changes owner, rights or flags inside a builder-writable folder**, because the builder can plant links there (DOC, #113).
- Rule from C7.1b: nothing privileged reads from `/Users/Shared` or `/tmp` (MINE, from the shared-places check, #113).
- [[snapshot]] before the run: `2026-11-19-175145`. Undo: `c7/uninstall.sh` (deleting class: STOP).

## History (not current instructions)
- The C7 run (#113) showed the builder could plant links to root-owned files inside its writable folder (#113); that finding produced the standing rule above.

## Not verified
- Whether the builder can add a *new* ACL right to a root-owned file in a granted folder (expected no; a later drill, C13).
- The real profiles (interview, test writer, build, proof writer) are written in C10.

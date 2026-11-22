<!-- page details (read by the checker; hidden when reading)
id: page-id-same-as-file-name
title: Page title in plain words
layer: build | component | troubleshooting | glossary | why | meta
type: explanation | reference | how-to | tutorial
status: draft
covers: [path/to/the/file/it/describes]
verified_on: null
verified_by: null
sources: [stage0-command-log.md#NNN, path/to/paper.md]
-->

# Page title

## In plain words
Three to five sentences, no jargon. Link every new word to the glossary: [[glossary-word]].

## Picture
```mermaid
flowchart LR
  A["Thing one"] -- "what happens" --> B["Thing two"]
```

## If this breaks
- **You notice:** ...
- **First safe step:** ... (reads only; changes nothing)
- **Read next:** [[page]]

## How it connects
- depends_on [[page]]
- protects [[page]]
- built_in [[page]]
- why [[page]]
- replaced_by [[page]]

## For agents: technical details
*Everything from here down is for agents and for checking facts. You can stop reading here.*

### Exact details (for agents)
| What | Value | Source |
|---|---|---|
| Runs on | machine and address | |
| Accounts | which account runs or owns it | |
| Files and folders | exact installed paths | |
| Logs | exact log paths | |
| Versions | exact versions | |
| Health check | exact check, where to run it, what a good result looks like, its label | |
| Start / stop / undo | exact commands, each with its STOP label | |

### Technical facts

- Fact (DOC, log #NNN).

### History (not current instructions)
- What we tried, what happened, why we changed it (log #NNN).

### Not verified
- What nobody has checked yet.

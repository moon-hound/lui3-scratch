#!/usr/bin/env python3
"""Guide checker. Enforces the [CHECKED] rules of guide/AGENTS.md. Standard library only.

Usage (from ~/projects/lui3-main):
  python3 guide/_tools/check.py [guide-folder]      check; prints one line per problem; exit 1 if any
  python3 guide/_tools/check.py --stamp <page-id>   write the current covers_hash into that page
                                                   (only after the page was checked against its covered files)
"""
import hashlib
import pathlib
import re
import sys

REQUIRED = ['id', 'title', 'layer', 'type', 'status', 'covers', 'covers_hash', 'verified_on', 'verified_by', 'sources']
STATUSES = {'draft', 'verified', 'stale'}
OPEN = '<!-- page details'
AGENT_SECTION = 'For agents: technical details'
TABLE = 'Exact details (for agents)'
ORDER = {
    'build': ['In plain words', 'Picture', 'If this breaks', 'How it connects', AGENT_SECTION],
    'component': ['In plain words', 'Picture', 'If this breaks', 'How it connects', AGENT_SECTION],
    'troubleshooting': ['In plain words', 'Picture', 'If this breaks', 'How it connects', AGENT_SECTION],
    'why': ['In plain words', 'Picture', 'If this breaks', 'How it connects', AGENT_SECTION],
    'glossary': ['In plain words', 'How it connects', AGENT_SECTION],
}
NOT_PAGES = {'AGENTS.md'}          # the rules file is not a page
LIST_PAGES = {'glossary'}           # list pages: shape rules do not apply
SECRETS = [r'ghp_[A-Za-z0-9]{20,}', r'github_pat_[A-Za-z0-9_]{20,}', r'-----BEGIN [A-Z ]*PRIVATE KEY-----',
           r'\bsk-[A-Za-z0-9]{20,}', r'xox[abp]-[A-Za-z0-9-]{10,}', r'AKIA[0-9A-Z]{16}']
LINK = re.compile(r'\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]')
SUDO_CMD = re.compile(r'\bsudo\s+[a-z]')
FACT_LABEL = re.compile(r'\b(DOC|MINE|3RD|VENDOR|NOT CHECKED|YOU)\b|#\d+|`[^`]+\.(md|sh|txt|yaml|plist|pf|env|py|json)`|progress file')


def front_matter(text):
    if not text.startswith(OPEN):
        return None, None
    start = text.find('\n') + 1
    end = text.find('\n-->', start)
    if end < 0:
        return None, None
    fm = {}
    for line in text[start:end].split('\n'):
        if ':' in line:
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip()
    return fm, (start, end)


def as_list(v):
    v = (v or '').strip()
    if v.startswith('[') and v.endswith(']'):
        return [x.strip() for x in v[1:-1].split(',') if x.strip()]
    return [v] if v and v != 'null' else []


def strip_code(text):
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    return re.sub(r'`[^`\n]*`', '', text)


def covers_hash(root, covers):
    h = hashlib.sha256()
    for c in sorted(covers):
        f = root / c
        h.update(c.encode() + b'\0' + (f.read_bytes() if f.is_file() else b'<missing>') + b'\0')
    return h.hexdigest()[:16]


def section(text, name, level='##'):
    m = re.search(r'^' + level + ' ' + re.escape(name) + r'\s*$', text, re.M)
    if not m:
        return ''
    nxt = re.search(r'^' + level + ' ', text[m.end():], re.M)
    return text[m.end(): m.end() + nxt.start()] if nxt else text[m.end():]


def pages_of(guide):
    return [p for p in guide.rglob('*.md')
            if not any(part.startswith('_') for part in p.relative_to(guide).parts) and p.name not in NOT_PAGES]


def stamp(guide, pid):
    root = guide.parent
    for p in pages_of(guide):
        text = p.read_text(encoding='utf-8')
        fm, span = front_matter(text)
        if fm and fm.get('id') == pid:
            new = covers_hash(root, as_list(fm.get('covers')))
            head = re.sub(r'^covers_hash:.*$', 'covers_hash: ' + new, text[:span[1]], flags=re.M)
            if 'covers_hash:' not in head:
                head = head.replace('\ncovers:', '\ncovers_hash: ' + new + '\ncovers:', 1) if '\ncovers:' in head else head
            p.write_text(head + text[span[1]:], encoding='utf-8')
            print(f'stamped {pid}: covers_hash {new}')
            return 0
    print(f'no page with id {pid}')
    return 1


def check(guide):
    root = guide.parent
    pages = pages_of(guide)
    problems, ids, links_to = [], {}, {}
    if not (guide / 'AGENTS.md').is_file():
        problems.append('guide/AGENTS.md (the rules file) is missing')
    log_text = (guide / 'log.md').read_text(encoding='utf-8') if (guide / 'log.md').is_file() else ''
    for p in pages:
        rel = p.relative_to(root)
        text = p.read_text(encoding='utf-8')
        fm, _ = front_matter(text)
        if fm is None:
            problems.append(f'{rel}: no page details comment at the top')
            continue
        for k in REQUIRED:
            if k not in fm:
                problems.append(f'{rel}: page details have no "{k}"')
        pid = fm.get('id', '')
        if pid != p.stem:
            problems.append(f'{rel}: id "{pid}" is not the file name "{p.stem}"')
        if pid in ids:
            problems.append(f'{rel}: id "{pid}" also used by {ids[pid]}')
        ids[pid] = rel
        if fm.get('status') not in STATUSES:
            problems.append(f'{rel}: status "{fm.get("status")}" is not one of {sorted(STATUSES)}')
        if fm.get('status') == 'verified' and (fm.get('verified_on') in (None, '', 'null') or fm.get('verified_by') in (None, '', 'null')):
            problems.append(f'{rel}: marked verified but verified_on or verified_by is empty')
        covers = as_list(fm.get('covers'))
        for c in covers:
            if not (root / c).exists():
                problems.append(f'{rel}: covers "{c}", which does not exist')
        if covers and fm.get('covers_hash', 'null') not in ('null', '') and fm.get('covers_hash') != covers_hash(root, covers):
            problems.append(f'{rel}: a covered file changed since this page was stamped; check the page against it, update it, then run --stamp {pid}')
        if covers and fm.get('covers_hash', 'null') in ('null', ''):
            problems.append(f'{rel}: covers files but has no covers_hash; run --stamp {pid} after checking the page')
        for pat in SECRETS:
            if re.search(pat, text):
                problems.append(f'{rel}: text looks like a secret (pattern {pat})')
        for n, line in enumerate(text.split('\n'), 1):
            if SUDO_CMD.search(line) and 'STOP' not in line:
                problems.append(f'{rel}:{n}: a sudo command without a STOP label on the same line')
        layer = fm.get('layer')
        if layer in ORDER and pid not in LIST_PAGES:
            h2 = re.findall(r'^## (.+?)\s*$', text, re.M)
            if [h for h in h2 if h in ORDER[layer]] != ORDER[layer] or h2[-1] != AGENT_SECTION:
                problems.append(f'{rel}: sections must be, in order: {", ".join(ORDER[layer])} (agent section last); found: {", ".join(h2)}')
            agent = section(text, AGENT_SECTION)
            h3 = re.findall(r'^### (.+?)\s*$', agent, re.M)
            if not h3 or h3[0] != TABLE:
                problems.append(f'{rel}: "## {AGENT_SECTION}" does not start with "### {TABLE}"')
            else:
                tbl = section(agent, TABLE, '###')
                rows = [r for r in tbl.split('\n') if r.startswith('|')]
                if len(rows) < 3 or [c.strip() for c in rows[0].strip('|').split('|')] != ['What', 'Value', 'Source']:
                    problems.append(f'{rel}: the exact-details table must have the columns What | Value | Source and at least one row')
                for r in rows[2:]:
                    cells = [c.strip() for c in r.strip().strip('|').split('|')]
                    if len(cells) < 3 or not cells[2]:
                        problems.append(f'{rel}: exact-details row "{cells[0] if cells else r}" has no source')
            for line in section(agent, 'Technical facts', '###').split('\n'):
                if re.match(r'\s*- ', line) and not FACT_LABEL.search(line):
                    problems.append(f'{rel}: technical fact without a label or source: {line.strip()[:70]}')
            if 'Picture' in ORDER[layer] and '```mermaid' not in section(text, 'Picture'):
                problems.append(f'{rel}: "## Picture" must hold a Mermaid diagram (```mermaid)')
        if pid not in ('log',) and f'[[{pid}]]' not in log_text:
            problems.append(f'{rel}: not mentioned in log.md as [[{pid}]]')
        links_to[pid] = {m.group(1).strip() for m in LINK.finditer(strip_code(text))}
    for pid, targets in links_to.items():
        for t in sorted(targets):
            if t not in ids:
                problems.append(f'{ids[pid]}: link [[{t}]] points to no page')
    linked = {t for src, ts in links_to.items() for t in ts if t != src}
    for pid, rel in ids.items():
        if pid != 'README' and pid not in linked:
            problems.append(f'{rel}: orphan, no other page links to it')
    for line in problems:
        print('PROBLEM', line)
    print(f'== {len(pages)} pages, {len(problems)} problems')
    return 1 if problems else 0


def main():
    here = pathlib.Path(__file__).resolve().parent.parent
    args = sys.argv[1:]
    if args[:1] == ['--stamp'] and len(args) == 2:
        return stamp(here, args[1])
    return check(pathlib.Path(args[0]) if args else here)


if __name__ == '__main__':
    sys.exit(main())

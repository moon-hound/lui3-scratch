#!/usr/bin/env python3
"""Guide checker: front matter, [[links]], orphans, covers paths, secret-looking text.
Usage: python3 guide/_tools/check.py [guide-folder]   (default: the guide folder this file sits in)
Prints one line per problem and exits 1 if there are any. Standard library only."""
import pathlib
import re
import sys

REQUIRED = ['id', 'title', 'layer', 'type', 'status', 'covers', 'verified_on', 'verified_by', 'sources']
STATUSES = {'draft', 'verified', 'stale'}
SECRETS = [r'ghp_[A-Za-z0-9]{20,}', r'github_pat_[A-Za-z0-9_]{20,}', r'-----BEGIN [A-Z ]*PRIVATE KEY-----',
           r'\bsk-[A-Za-z0-9]{20,}', r'xox[abp]-[A-Za-z0-9-]{10,}', r'AKIA[0-9A-Z]{16}']
LINK = re.compile(r'\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]')


OPEN = '<!-- page details'


def front_matter(text):
    # Page details sit in a hidden HTML comment at the top, so viewers without front-matter support do not show them.
    if not text.startswith(OPEN):
        return None
    start = text.find('\n') + 1
    end = text.find('\n-->', start)
    if end < 0:
        return None
    fm = {}
    for line in text[start:end].split('\n'):
        if ':' in line:
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip()
    return fm


def as_list(v):
    v = (v or '').strip()
    if v.startswith('[') and v.endswith(']'):
        return [x.strip() for x in v[1:-1].split(',') if x.strip()]
    return [v] if v and v != 'null' else []


def strip_code(text):
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    return re.sub(r'`[^`\n]*`', '', text)


def main():
    guide = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent)
    root = guide.parent
    pages = [p for p in guide.rglob('*.md') if not any(part.startswith('_') for part in p.relative_to(guide).parts)]
    problems, ids, links_to = [], {}, {}
    for p in pages:
        rel = p.relative_to(root)
        text = p.read_text(encoding='utf-8')
        fm = front_matter(text)
        if fm is None:
            problems.append(f'{rel}: no front matter')
            continue
        for k in REQUIRED:
            if k not in fm:
                problems.append(f'{rel}: front matter has no "{k}"')
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
        for c in as_list(fm.get('covers')):
            if not (root / c).exists():
                problems.append(f'{rel}: covers "{c}", which does not exist')
        for pat in SECRETS:
            if re.search(pat, text):
                problems.append(f'{rel}: text looks like a secret (pattern {pat})')
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


if __name__ == '__main__':
    sys.exit(main())

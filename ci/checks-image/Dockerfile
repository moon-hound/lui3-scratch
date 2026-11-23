# Test image for lui3-scratch: the checks run in it with no network (CI gate and the Studio's lui3-check).
# requirements-ci.txt is empty on purpose: the scratch tests use only Python's standard library. When packages
# are added, each one is pinned with --require-hashes and installed here.
# Base pinned by index digest (log #161, #162): python:3.12-slim-trixie, pushed 2026-11-08.
FROM python:3.12-slim-trixie@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b
COPY requirements-ci.txt /opt/lui3/requirements-ci.txt

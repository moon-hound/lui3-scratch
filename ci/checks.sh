#!/bin/sh
# The one check script. CI's gate and the Studio's lui3-check both run exactly this file, taken from main.
# Runs with no network, as a non-root user, in the test image (python:3.12-slim-trixie, pinned by digest).
set -eu
export PYTHONDONTWRITEBYTECODE=1
python3 -m unittest discover -s tests -t . -v
echo "CHECKS-OK"

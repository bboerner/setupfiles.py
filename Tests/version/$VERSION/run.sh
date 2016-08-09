#!/usr/bin/env bash
{ set +x; } 2>/dev/null

{ set -x; cd "${BASH_SOURCE[0]%/*}"; { set +x; } 2>/dev/null; }

VERSION="0.0.42"
{ set -x; export VERSION="$VERSION"; { set +x; } 2>/dev/null; }
version="$(python .setup.py --version)"
[[ $VERSION == $version ]] && exit 0

echo "ERROR: version=$version" && exit 1

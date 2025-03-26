#!/usr/bin/env bash

set -e

file="README_encrypted.md"

# ensure file exists
if [ ! -f "$file" ]; then
    echo "File not found!"
    exit 1
fi

ansible-vault view "$file"

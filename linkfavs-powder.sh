#!/usr/bin/env bash

set -e
# set -x

# Files to link (just filenames)
IMAGES_TO_LINK=(
    "1.png"
    "2.png"
    "3.png"
)

. ./common.sh
main

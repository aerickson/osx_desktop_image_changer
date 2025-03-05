#!/usr/bin/env bash

set -e

IMAGE_ROOT="$HOME/Downloads/macOS Wallpapers"

IMAGES_TO_LINK=(
    "Lines Graphite.jpg"
    "Lines Moss.jpg"
    "Lines Plum.jpg"
    "Lines Blue.jpg"
)

. ./common.sh
main

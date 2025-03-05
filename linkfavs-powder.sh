#!/usr/bin/env bash

set -e

IMAGE_ROOT="$HOME/Downloads/macOS Wallpapers"

IMAGES_TO_LINK=(
    "3.png"
    "2.png"
    "1.png"
)

. ./common.sh
main

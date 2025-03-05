#!/usr/bin/env bash

set -e

IMAGE_ROOT="$HOME/Downloads/macOS Wallpapers"

IMAGES_TO_LINK=(
    "10-0_10.1.png"
    "10-2.png"
    "10-3.png"
    "10-4.png"
)

. ./common.sh
main

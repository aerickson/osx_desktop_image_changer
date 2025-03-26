#!/usr/bin/env bash

set -e

IMAGE_ROOT="$HOME/Downloads/macOS Wallpapers"

IMAGES_TO_LINK=(
    "Radial Green.heic"
    "Radial Purple.heic"
    "Radial Yellow.heic"
    "Radial Blue.heic"
)

. ./common.sh
main

#!/usr/bin/env bash

set -e

IMAGE_ROOT="$HOME/Downloads/macOS Wallpapers"

IMAGES_TO_LINK=(
    "Light Stream Green.JPG"
    "Light Stream Pink.JPG"
    "Light Stream Green.heic"
    "Light Stream Pink.heic"
)

. ./common.sh
main

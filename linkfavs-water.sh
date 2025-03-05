#!/usr/bin/env bash

set -e

IMAGE_ROOT="$HOME/Downloads/macOS Wallpapers"

IMAGES_TO_LINK=(
    "rolling-waves.jpg"
    "osx_hero_2x.jpg"
    "Tranquil Surface.jpg"
    "Water.jpg"
)

. ./common.sh
main

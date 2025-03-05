#!/usr/bin/env bash

set -e

IMAGE_ROOT="$HOME/Downloads/macOS Wallpapers"

IMAGES_TO_LINK=(
    "Reflection 1.jpg"
    "Reflection 2.jpg"
    "Reflection 3.jpg"
    "Reflection 4.jpg"
)

. ./common.sh
main

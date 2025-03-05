#!/usr/bin/env bash

set -e

IMAGE_ROOT="$HOME/Downloads/macOS Wallpapers"

IMAGES_TO_LINK=(
    "DefaultDesktop.jpg"
    "Aurora (Server).jpg"
    "Aurora.jpg"
)

. ./common.sh
main

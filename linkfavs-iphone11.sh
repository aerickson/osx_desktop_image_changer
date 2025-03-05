#!/usr/bin/env bash

set -e

IMAGE_ROOT="$HOME/Downloads/iOS Wallpapers"

IMAGES_TO_LINK=(
    "Red-Light.jpg"
    "Yellow-Light.jpg"
    "White-Light.jpg"
    "Purple-Light.jpg"
    "Mint-Light.jpg"
    "Black-Light.jpg"
)

. ./common.sh
main

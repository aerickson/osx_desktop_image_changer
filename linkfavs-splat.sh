#!/usr/bin/env bash

set -e

IMAGE_ROOT="$HOME/Downloads/iOS Wallpapers"

IMAGES_TO_LINK=(
    "Spash4-potassium-1024w-1366h@2x~ipad.jpg"
    "Spash3-potassium-1024w-1366h@2x~ipad.jpg"
    "Spash1-potassium-1024w-1366h@2x~ipad.jpg"
    "Spash2-potassium-1024w-1366h@2x~ipad.jpg"
)

. ./common.sh
main

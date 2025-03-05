#!/usr/bin/env bash

set -e

IMAGE_ROOT="$HOME/Downloads/iOS Wallpapers"

IMAGES_TO_LINK=(
    "WWDC_2019_Dark-1024w-1366h@2x~ipad.png"
    "WWDC_2019_Light-1024w-1366h@2x~ipad.png"
    "WWDC_2019_Dark-1024w-1366h@2x~ipad.png"
    "WWDC_2019_Light-1024w-1366h@2x~ipad.png"
    "WWDC_2019_Dark-1024w-1366h@2x~ipad.png"
    "WWDC_2019_Light-1024w-1366h@2x~ipad.png"
)

. ./common.sh
main

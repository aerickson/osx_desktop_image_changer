#!/usr/bin/env bash

set -e

IMAGE_ROOT="$HOME/Downloads/iOS Wallpapers"

IMAGES_TO_LINK=(
    "1242.WWDC_2019_Dark-1024w-1366h@2x~ipad.png"
    "1241.WWDC_2019_Light-1024w-1366h@2x~ipad.png"
    "1232.WWDC_2019_Dark-1024w-1366h@2x~ipad.png"
    "1222.WWDC_2019_Dark-1024w-1366h@2x~ipad.png"
    "1221.WWDC_2019_Light-1024w-1366h@2x~ipad.png"
    "1211.WWDC_2019_Light-1024w-1366h@2x~ipad.png"
    "1212.WWDC_2019_Dark-1024w-1366h@2x~ipad.png"
    "1231.WWDC_2019_Light-1024w-1366h@2x~ipad.png"
)

. ./common.sh
main

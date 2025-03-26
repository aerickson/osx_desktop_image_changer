#!/usr/bin/env bash

set -e

IMAGE_ROOT="/Users/aje/Downloads/_aje_osx_desktop_backup"

IMAGES_TO_LINK=(
    "iMac Blue.heic"
    "iMac Green.heic"
    "iMac Orange.heic"
    "iMac Pink.heic"
    "iMac Purple.heic"
    "iMac Silver.heic"
    "iMac Yellow.heic"
)

. ./common.sh
main

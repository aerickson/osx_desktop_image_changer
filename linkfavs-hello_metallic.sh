#!/usr/bin/env bash

set -e

IMAGE_ROOT="/Users/aje/Downloads/_aje_osx_desktop_backup"

IMAGES_TO_LINK=(
    "Hello Metallic Blue.heic"
    "Hello Metallic Green.heic"
    "Hello Metallic Orange.heic"
    "Hello Metallic Pink.heic"
    "Hello Metallic Purple.heic"
    "Hello Metallic Silver.heic"
    "Hello Metallic Yellow.heic"
)

. ./common.sh
main

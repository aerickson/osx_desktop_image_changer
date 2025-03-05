#!/usr/bin/env bash

set -e
set -x

IMAGE_ROOT="$HOME/Downloads/macOS Wallpapers"

SYMLINK_TREE_ROOT="$HOME/Downloads/desktop-favorites"
# base the symlimk tree dir's name on this script's name (remove the .sh)
SYMLINK_TREE_DEST="${SYMLINK_TREE_ROOT}/$(basename $0 | sed 's/\.sh$//g')"

set -x

mkdir -p ${SYMLINK_TREE_ROOT}
mkdir -p ${SYMLINK_TREE_DEST}

ln -sf "$IMAGE_ROOT/3.png" "$IMAGE_ROOT/2.png" "$IMAGE_ROOT/1.png" $SYMLINK_TREE_DEST/

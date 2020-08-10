#!/usr/bin/env bash

set -x
set -e

# || true because we want to continue running the script if sys prefs wasn't running
killall System\ Preferences > /dev/null 2>&1 || true

rm ~/Library/Application\ Support/Dock/desktoppicture.db

killall Dock

#!/usr/bin/env bash

set -e

killall System\ Preferences > /dev/null 2>&1 && rm ~/Library/Application\ Support/Dock/desktoppicture.db && killall Dock

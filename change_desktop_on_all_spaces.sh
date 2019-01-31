#!/bin/sh

# if the Dock won't start, remove the desktoppickture.db file referenced below and debug

if [ -z "$1" ]; then
    echo "Usage $0 [filename]"
      exit 1
    fi

    echo "UPDATE data SET value='$1';" | sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db
    killall Dock

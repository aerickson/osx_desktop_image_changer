#!/usr/bin/env bash

set -e
set -x

 sqlite3  "$HOME/Library/Application Support/Dock/desktoppicture.db" ".dump"

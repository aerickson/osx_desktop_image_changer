#!/usr/bin/env bash

set -e

sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db '.dump'

#!/usr/bin/env bash

set -e

date_str=`date +"%Y%m%d_%H%M%S"`
sqlite3 "$HOME/Library/Application Support/Dock/desktoppicture.db" ".dump" > backup_$date_str.txt

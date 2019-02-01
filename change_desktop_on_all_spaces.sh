#!/usr/bin/env bash

set -e
# set -x

# TROUBLESHOOTING:
# - if the Dock won't start, remove the desktoppickture.db file referenced below and debug

# NOTES:
# based on https://stackoverflow.com/questions/33533304/change-scaling-for-all-desktop-backgrounds-on-mac-via-a-script
#
# preferences: there are 2 entries per space + 2 additional (not sure why)

# TODO: for number of entries in preferences table, count rows in spaces and
#       add 2.
# TODO: the limit for spaces is 16... create some more entries below.

image_already_set() {
    current_path=$(sqlite3 -noheader -batch ${HOME}/Library/Application\ Support/Dock/desktoppicture.db 'select value from data limit 1')
    echo "cp: $current_path"
    if [[ "$current_path" != "$1" ]]; then
      echo 0
      return
    fi
    echo 1
}

change_desktop_old() {
    current_path=$(sqlite3 -noheader -batch ${HOME}/Library/Application\ Support/Dock/desktoppicture.db 'select value from data limit 1')
    if [[ "$current_path" != "$1" ]]; then
        sqlite3 ${HOME}/Library/Application\ Support/Dock/desktoppicture.db "update data set value = '${1}'" && killall Dock
    fi
}

change_desktop_new() {
    # current_path=$(sqlite3 -noheader -batch ${HOME}/Library/Application\ Support/Dock/desktoppicture.db 'select value from data limit 1')
    # if [[ "$current_path" != "$1" ]]; then
      sqlite3 "${HOME}/Library/Application Support/Dock/desktoppicture.db" " \
          DELETE FROM data; \
          DELETE FROM preferences; \
          INSERT INTO data (value) VALUES ('$1'); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 1); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 2); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 3); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 4); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 5); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 6); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 7); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 8); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 9); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 10); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 11); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 12); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 13); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 14); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 15); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 16); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 17); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 18); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 19); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 20); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 21); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 22); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 23); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 24); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 25); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 26); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 27); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 28); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 29); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 30); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 31); \
          INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 32);
      " && killall Dock
    # fi
}

IMG_FILE=$1
echo $IMG_FILE
echo $(image_already_set $IMG_FILE)
# exit
OSX_VERSION=$(sw_vers -productVersion | cut -d '.' -f 2)
if (( $OSX_VERSION <= 12 )); then
    change_desktop_old "$IMG_FILE"
else
    change_desktop_new "$IMG_FILE"
fi
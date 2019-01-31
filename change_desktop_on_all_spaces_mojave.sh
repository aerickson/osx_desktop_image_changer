#!/usr/bin/env bash

set -e

# based on https://stackoverflow.com/questions/33533304/change-scaling-for-all-desktop-backgrounds-on-mac-via-a-script

# preferences: there are 2 entries per space + 2 additional (not sure why)

# TODO: for number of entries in preferences table, count rows in spaces and
#       add 2.
# TODO: the limit for spaces is 16... create some more entries below.

sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db " \
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
    INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 22);
" && killall Dock

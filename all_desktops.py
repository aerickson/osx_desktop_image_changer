#!/usr/bin/env python3

from os.path import expanduser
import re



# image_already_set() {
#     current_path=$(sqlite3 -noheader -batch ${HOME}/Library/Application\ Support/Dock/desktoppicture.db 'select value from data limit 1')
#     echo "cp: $current_path"
#     if [[ "$current_path" != "$1" ]]; then
#       echo 0
#       return
#     fi
#     echo 1
# }

# change_desktop_old() {
#     current_path=$(sqlite3 -noheader -batch ${HOME}/Library/Application\ Support/Dock/desktoppicture.db 'select value from data limit 1')
#     if [[ "$current_path" != "$1" ]]; then
#         sqlite3 ${HOME}/Library/Application\ Support/Dock/desktoppicture.db "update data set value = '${1}'" && killall Dock
#     fi
# }

# change_desktop_new() {
#     current_path=$(sqlite3 -noheader -batch ${HOME}/Library/Application\ Support/Dock/desktoppicture.db 'select value from data limit 1')
# #    if [[ "$current_path" != "$1" ]]; then
#       sqlite3 "${HOME}/Library/Application Support/Dock/desktoppicture.db" " \
#           DELETE FROM data; \
#           DELETE FROM preferences; \
#           INSERT INTO data (value) VALUES ('$1'); \
#           INSERT INTO data (value) VALUES ('$2'); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 1); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 2); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 3); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 4); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 5); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 6); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 7); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 8); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 9); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 10); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 11); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 12); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 13); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 2, 14); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 2, 15); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 16); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 17); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 18); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 19); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 20); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 21); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 22); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 23); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 24); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 25); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 26); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 27); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 28); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 29); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 30); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 31); \
#           INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 32);
#       " && killall Dock
# #    fi
# }

# IMG_FILE=$1
# # echo $IMG_FILE
# # echo $(image_already_set $IMG_FILE)
# # exit
# OSX_VERSION=$(sw_vers -productVersion | cut -d '.' -f 2)
# if (( $OSX_VERSION <= 12 )); then
#     change_desktop_old "$IMG_FILE"
# else
#     change_desktop_new "$IMG_FILE"
# fi

import subprocess
import sys

def run_command(command):
    # c = subprocess.call(["ls", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # print(c.stdout.decode('utf-8'))
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    return output.decode('utf-8')

def change_desktop_new(file):
    home = expanduser("~")
    d = {'home': home, 'file': file}

    command = '''
        sqlite3 "{home}/Library/Application Support/Dock/desktoppicture.db" " \
            DELETE FROM data; \
            DELETE FROM preferences; \
            INSERT INTO data (value) VALUES ('{file}'); \
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
            INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 32); \
        " && killall Dock
'''
    command = command.format(**d).strip()
    command = re.sub(' +', ' ', command)
    print(command)
    return run_command(command)

def change_desktop_old(file):
    home = expanduser("~")
    d = {'home': home, 'file': file}

    command = '''
        sqlite3 "{home}/Library/Application Support/Dock/desktoppicture.db" " \
            update data set value = '${file}' \
        " && killall Dock
'''
    command = command.format(**d).strip()
    command = re.sub(' +', ' ', command)
    print(command)
    # return run_command(command)

if __name__ == "__main__":
    
    # print(run_command('ls -l'))
    # print( len(sys.argv))

    OSX_VERSION = run_command("sw_vers -productVersion | cut -d '.' -f 2").strip()
    print(OSX_VERSION)
    if int(OSX_VERSION) <= 12:
        file = sys.argv[1]
        change_desktop_old(file)
    else:
        if len(sys.argv) > 2:
            print("not done yet")
            pass
        else:
            file = sys.argv[1]
            change_desktop_new(file)
    
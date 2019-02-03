#!/usr/bin/env python

from os.path import expanduser
import re
import subprocess
import sys


def run_command(command):
    # c = subprocess.call(["ls", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # print(c.stdout.decode('utf-8'))
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    return output.decode('utf-8')

def image_already_set(file):
    home = expanduser("~")
    d = {'home': home, 'file': file}

    command = '''
        sqlite3 "{home}/Library/Application Support/Dock/desktoppicture.db" \
            "select value from data limit 1"
'''
    command = command.format(**d).strip()
    command = re.sub(' +', ' ', command)
    # print(command)
    output = run_command(command).strip()
    # print(output)
    if output == file:
        return True
    return False

def change_desktop_new_random(file_arr):
    home = expanduser("~")

    data_block = ""
    prefs_block = ""

    # os x limits to 16 spaces and there are 2 entries per (1-32)
    PREF_ENTRIES = 32

    for item in file_arr:
        data_block += "INSERT INTO data (value) VALUES ('%s'); " % item

    for i in range(1, PREF_ENTRIES):
        prefs_block += "INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, %s); " % i 

    d = {'home': home, 'data_block': data_block,
         'prefs_block': prefs_block}
    command = '''
        sqlite3 "{home}/Library/Application Support/Dock/desktoppicture.db" " \
            DELETE FROM data; \
            DELETE FROM preferences; \
            {data_block} \
            {prefs_block} \
        " && killall Dock
'''
    command = command.format(**d).strip()
    command = re.sub(' +', ' ', command)
    # print(command)
    return run_command(command)

def change_desktop_new(file):
    if image_already_set(file):
        return

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
    # print(command)
    return run_command(command)

def change_desktop_old(file):
    if image_already_set(file):
        return

    home = expanduser("~")
    d = {'home': home, 'file': file}

    command = '''
        sqlite3 "{home}/Library/Application Support/Dock/desktoppicture.db" " \
            update data set value = '${file}' \
        " && killall Dock
'''
    command = command.format(**d).strip()
    command = re.sub(' +', ' ', command)
    # print(command)
    return run_command(command)

if __name__ == "__main__":
    
    # print(run_command('ls -l'))
    # print( len(sys.argv))

    # file = sys.argv[1]
    # print(image_already_set(file))
    # sys.exit()

    # TODO: add -f mode (force, don't check if already set)
    # TODO: add --dry-run mode (don't do anything)
    # TODO: add --verbose mode (print command)

    if len(sys.argv) == 1:
        print("Please specify at least one image!")
        sys.exit(1)

    OSX_VERSION = run_command("sw_vers -productVersion | cut -d '.' -f 2").strip()
    # print(OSX_VERSION)
    if int(OSX_VERSION) <= 12:
        file = sys.argv[1]
        change_desktop_old(file)
    else:
        if len(sys.argv) > 2:
            # TODO: support random or alternating
            # print("not done yet")
            # args = sys.argv[1:]
            # print(args)

            # # TESTING
            # file = sys.argv[1]
            # change_desktop_new(file)
            # print("\n\n-----------------\n\n")
            # # END TESTING

            change_desktop_new_random(args)
            pass
        else:
            file = sys.argv[1]
            change_desktop_new(file)
    
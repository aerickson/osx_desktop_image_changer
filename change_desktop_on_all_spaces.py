#!/usr/bin/env python

import argparse
import itertools
from os.path import expanduser
import re
import subprocess
import sys


def run_command(command):
    # c = subprocess.call(["ls", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # print(c.stdout.decode('utf-8'))
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    return output.decode("utf-8")


def double_array(an_arr):
    new_arr = []
    for item in an_arr:
        new_arr.append(item)
        new_arr.append(item)
    return new_arr


def image_already_set(file):
    home = expanduser("~")
    d = {"home": home, "file": file}

    command = """
        sqlite3 "{home}/Library/Application Support/Dock/desktoppicture.db" \
            "select value from data limit 1"
"""
    command = command.format(**d).strip()
    command = re.sub(" +", " ", command)
    # print(command)
    output = run_command(command).strip()
    # print(output)
    if output == file:
        return True
    return False


def change_desktop_new_alternating(file_arr):
    home = expanduser("~")

    data_block = ""
    prefs_block = ""

    # desktops 1 - 16
    # 2 per screen and then one for the default screen or something
    PREF_ENTRIES = 34

    for item in file_arr:
        data_block += "INSERT INTO data (value) VALUES ('%s'); " % item

    single_arr = range(1, len(file_arr) + 1)
    double_arr = double_array(single_arr)
    my_iterator = itertools.cycle(double_arr)
    # print(len(file_arr))
    for i in range(1, PREF_ENTRIES + 1):
        element = my_iterator.next()
        # print(element)
        prefs_block += (
            "INSERT INTO preferences (key, data_id, picture_id) VALUES (1, %s, %s); "
            % (element, i)
        )

    d = {"home": home, "data_block": data_block, "prefs_block": prefs_block}
    command = """
        sqlite3 "{home}/Library/Application Support/Dock/desktoppicture.db" " \
            DELETE FROM data; \
            DELETE FROM preferences; \
            {data_block} \
            {prefs_block} \
        " && killall Dock
"""
    command = command.format(**d).strip()
    command = re.sub(" +", " ", command)
    # print(command)
    return run_command(command)


def change_desktop_new(file):
    if image_already_set(file):
        return

    home = expanduser("~")
    d = {"home": home, "file": file}

    command = """
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
            INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 33); \
            INSERT INTO preferences (key, data_id, picture_id) VALUES (1, 1, 34); \
        " && killall Dock
"""
    command = command.format(**d).strip()
    command = re.sub(" +", " ", command)
    # print(command)
    return run_command(command)


def change_desktop_old(file):
    if image_already_set(file):
        return

    home = expanduser("~")
    d = {"home": home, "file": file}

    command = """
        sqlite3 "{home}/Library/Application Support/Dock/desktoppicture.db" " \
            update data set value = '${file}' \
        " && killall Dock
"""
    command = command.format(**d).strip()
    command = re.sub(" +", " ", command)
    # print(command)
    return run_command(command)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(usage='%(prog)s [options] image [image ...]')
    parser.add_argument("images", help="an image file", nargs='+', metavar="image")
    parser.add_argument("-f", "--force", action="store_true", help="don't check if the image is already set")
    parser.add_argument("-d", "--dry-run", action="store_true", help="don't do anything")
    parser.add_argument("-v", "--verbose",
                    action="store_true", dest="verbose", default=False,
                    help="print extra information")
    #
    parser.add_argument("-s", "--single-random", action="store_true", help="set all spaces to one randomly chosen image")
    parser.add_argument("-r", "--random", action="store_true", help="set each spaces randomly using all images")
    parser.add_argument("-a", "--alternating", action="store_true", help="set all spaces in the order given (repeats)")

    args = parser.parse_args()
    # print(args)

    OSX_VERSION = run_command("sw_vers -productVersion | cut -d '.' -f 2").strip()
    # print(OSX_VERSION)
    if int(OSX_VERSION) <= 12:
        if len(args.images) == 1:
            file = args.images[0]
            change_desktop_old(file)
        else:
            print("ERROR: Only a single image is supported!")
            sys.exit(1)
    else:
        if len(args.images) >= 2:
            # TODO: possible other modes:
            #   - select one randomly, set all to it (-s)
            #   - pick a new random image per space (-r)
            #   - alternating (-a, current default)

            args = sys.argv[1:]
            change_desktop_new_alternating(args)
            pass
        else:
            file = args.images[0]
            change_desktop_new(file)

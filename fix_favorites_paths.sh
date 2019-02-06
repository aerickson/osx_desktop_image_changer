#!/usr/bin/env bash

set -e
#set -x

rpstring="s#$HOME#\$HOME#g"

# testing
#sed $rpstring $1

# for real
sed -i '.bak' $rpstring $1

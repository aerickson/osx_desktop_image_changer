#!/usr/bin/env bash

set -e
#set -x

rpstring="s#$HOME#\$HOME#g"

# testing
#sed $rpstring $1

# for real
sed -i '.bak' $rpstring $1

# cleanup if .bak is identical
set +e
_OUTPUT=`cmp --silent ${1} ${1}.bak`
RESULT=$?
set -e

if [ "$RESULT" -eq "0" ]; then
  rm ${1}.bak
fi

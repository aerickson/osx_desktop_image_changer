#!/usr/bin/env bash

set -e
#set -x

rpstring="s#$HOME#\$HOME#g"
# TODO: check that $@ isn't already on the end of the string
rpstring2='/.\/change/ s/$/ $@/g'

# testing
#sed -e "$rpstring" -e "$rpstring2" $1
#exit

# for real
sed -i '.bak' -e "$rpstring" -e "$rpstring2" $1

# cleanup if .bak is identical
set +e
_OUTPUT=`cmp --silent ${1} ${1}.bak`
RESULT=$?
set -e

if [ "$RESULT" -eq "0" ]; then
  rm ${1}.bak
fi

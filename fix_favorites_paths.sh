#!/usr/bin/env bash

set -e
set -x

# TODO: fail to run if no arg (or do all?)

# replace home path with $HOME var
rpstring="s#$HOME#\$HOME#g"
# add $@ to end of command so we can use args
# - check that $@ isn't already on the end of the string
rpstring2='/.\/change.*(?!\$@)\ $\@/ s/$/ $@/g'

WFILE=$1

# testing
#sed -e "$rpstring" -e "$rpstring2" $WFILE
#exit

# for real
sed -i '.bak' -e "$rpstring" -e "$rpstring2" $WFILE

# cleanup if .bak is identical
set +e
# can't use $1 $1.bak because xargs mucks with $1 or something...
_OUTPUT=$(cmp --silent ${WFILE}*)
RESULT=$?
set -e

if [ "$RESULT" -eq "0" ]; then
  rm ${WFILE}.bak
fi

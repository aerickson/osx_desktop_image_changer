#!/usr/bin/env bash

set -e

OUTPUT_FILE="favorites-new.sh"

if [ -e "$OUTPUT_FILE" ]; then
  echo "File already exists ($OUTPUT_FILE)!"
  exit 1
fi

VAR=$(cat <<'END_HEREDOC'
#!/usr/bin/env bash

set -e
# set -x

./change_desktop_on_all_spaces.py file1.jpg file2.jpg $@
END_HEREDOC
)


echo "$VAR" > "$OUTPUT_FILE"
chmod 755 "$OUTPUT_FILE"
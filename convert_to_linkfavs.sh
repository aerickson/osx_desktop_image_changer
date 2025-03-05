#!/usr/bin/env bash

set -e
set -x

# Loop through all favorites-*.sh files
for fav_file in favorites-*.sh; do
    # Skip if file doesn't exist
    [ -f "$fav_file" ] || continue
    
    # Create output filename
    linkfav_file="linkfavs-${fav_file#favorites-}"

    # TODO: if linkfav file exists, skip
    # TODO: hide behind a flag
    # [ -f "$linkfav_file" ] && continue

    # inspect the favorite file to determine the image root
    # if the files contain $IMAGE_ROOT_IOS, then the image root is iOS Wallpapers
    # if the files contain $IMAGE_ROOT_MAC, then the image root is macOS Wallpapers
    if grep -q "iOS" "$fav_file"; then
        image_root='IMAGE_ROOT="$HOME/Downloads/iOS Wallpapers"'
    elif grep -q "macOS" "$fav_file"; then
        image_root='IMAGE_ROOT="$HOME/Downloads/macOS Wallpapers"'
    else
        echo "Could not determine image root for $fav_file"
        exit 1
    fi

    # Extract the image filenames
    # example: ./change_desktop_on_all_spaces.py $HOME/Downloads/macOS\ Wallpapers/DefaultDesktop.jpg $HOME/Downloads/macOS\ Wallpapers/Aurora\ \(Server\).jpg $HOME/Downloads/macOS\ Wallpapers/Aurora.jpg  $@
    # should yield: "DefaultDesktop.jpg" "Aurora (Server).jpg" "Aurora.jpg"
    images = $(grep -oE "([\\\w\s]*).jpg|heic" "$fav_file")



    # images=$(grep -oE "[\\\w\s]*.(jpg|heic)" "$fav_file")


    # Create the new linkfavs file
    cat > "$linkfav_file" << EOL
#!/usr/bin/env bash

set -e

${image_root:+"$image_root"}

IMAGES_TO_LINK=(
$(echo "$images" | sed 's/^/    "/g' | sed 's/$/"/g')
)

. ./common.sh
main
EOL

    # Make the new file executable
    chmod +x "$linkfav_file"
    
    echo "Created $linkfav_file"
done
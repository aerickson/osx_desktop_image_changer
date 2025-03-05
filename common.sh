# Configuration
IMAGE_ROOT_MAC="$HOME/Downloads/macOS Wallpapers"
IMAGE_ROOT_IOS="$HOME/Downloads/iOS Wallpapers"
SYMLINK_TREE_ROOT="$HOME/Downloads/desktop-favorites"

create_symlink_dest() {
    local script_name=$(basename "$0" | sed 's/\.sh$//g')
    local dest_dir="${SYMLINK_TREE_ROOT}/${script_name}"
    
    mkdir -p "${SYMLINK_TREE_ROOT}"
    mkdir -p "${dest_dir}"
    echo "${dest_dir}"
}

create_symlinks() {
    local dest_dir="$1"
    local source_paths=()

    # Create array of full source paths
    for image in "${IMAGES_TO_LINK[@]}"; do
        source_paths+=("${IMAGE_ROOT}/${image}")
    done

    # Create symlinks
    ln -sf "${source_paths[@]}" "${dest_dir}/"
}

main() {
    local dest_dir=$(create_symlink_dest)
    create_symlinks "${dest_dir}"
    echo "Symlinks created in ${dest_dir}"
}
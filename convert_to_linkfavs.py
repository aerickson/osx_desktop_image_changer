#!/usr/bin/env python3

import os
import re
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Convert favorite scripts to linkfavs scripts.")
    parser.add_argument('-d', '--dry-run', action='store_true', help="Run the script without making any changes.")
    parser.add_argument('-o', '--overwrite', action='store_true', help="Overwrite existing linkfavs files.")
    args = parser.parse_args()

    print("Starting the script...")  # Debugging output
    # Loop through all favorites-*.sh files
    for fav_file in os.listdir('.'):
        # print(f"Inspecting file: {fav_file}")  # Debugging output
        if not fav_file.startswith('favorites-') or not fav_file.endswith('.sh'):
            continue

        # Create output filename
        linkfav_file = f"linkfavs-{fav_file[len('favorites-'):]}"
        print(f"Output file will be: {linkfav_file}")  # Debugging output
        
        # Skip if linkfav file exists and --overwrite is not set
        if os.path.exists(linkfav_file) and not args.overwrite:
            print(f"Skipping {linkfav_file}, it already exists.")  # Debugging output
            continue

        # Inspect the favorite file to determine the image root
        with open(fav_file, 'r') as file:
            content = file.read()
            if 'iOS' in content:
                image_root = 'IMAGE_ROOT="$HOME/Downloads/iOS Wallpapers"'
            elif 'macOS' in content:
                image_root = 'IMAGE_ROOT="$HOME/Downloads/macOS Wallpapers"'
            else:
                print(f"Could not determine image root for {fav_file}")
                sys.exit(1)
            print(f"Determined image root: {image_root}")  # Debugging output

        # Extract the image filenames
        images = re.findall(r'([\w\s]*\.(?:jpg|heic))', content)
        print(f"Extracted images: {images}")  # Debugging output

        if args.dry_run:
            print(f"Dry run: would create {linkfav_file} with images {images}")
            continue

        # Create the new linkfavs file
        with open(linkfav_file, 'w') as file:
            file.write(f"""#!/usr/bin/env bash

set -e

{image_root}

IMAGES_TO_LINK=(
""")
            for image in images:
                file.write(f'    "{image}"\n')
            file.write(""")
)

. ./common.sh
main
""")
        print(f"Created file: {linkfav_file}")  # Debugging output

        # Make the new file executable
        os.chmod(linkfav_file, 0o755)
        print(f"Made {linkfav_file} executable")  # Debugging output
        
        print(f"Created {linkfav_file}")

if __name__ == "__main__":
    main()

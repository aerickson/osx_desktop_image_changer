#!/usr/bin/env python3

import os
import sys
import re

def generate_token(filenames):
    """Generate a token from file names by removing variations and colors"""
    # Extract just the base filenames without extensions
    base_names = [os.path.splitext(os.path.basename(f))[0] for f in filenames]
    
    # Find common prefix across all filenames
    if not base_names:
        return "wallpaper"
        
    # Get the first part of the filename that's common across all files
    # For example, "iMac" from "iMac Blue", "iMac Green", etc.
    words_list = [name.split() for name in base_names]
    
    # Find common prefix words
    common_prefix = []
    if words_list:
        first_words = words_list[0]
        for i, word in enumerate(first_words):
            if all(i < len(words) and words[i] == word for words in words_list):
                common_prefix.append(word)
            else:
                break
    
    if common_prefix:
        token = "_".join(common_prefix).lower()
    else:
        # Fallback: use the first filename with numbers removed
        token = re.sub(r'\d+', '', base_names[0]).strip()
        token = token.replace(' ', '_').lower()
    
    # Remove any trailing or leading underscores
    token = token.strip('_')
    
    return token

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_linkfavs.py file1.jpg file2.jpg ...")
        sys.exit(1)
    
    files = sys.argv[1:]
    
    # Check if all files exist
    for file_path in files:
        if not os.path.exists(file_path):
            print(f"Error: File {file_path} does not exist")
            sys.exit(1)
    
    # Get the directories of all files
    directories = {os.path.dirname(os.path.abspath(f)) for f in files}
    
    # Check if all files are in the same directory
    if len(directories) > 1:
        print("Error: All files must be in the same directory")
        print("Files are located in these directories:")
        for directory in directories:
            print(f"  - {directory}")
        sys.exit(1)
    
    # Generate token based on file names
    token = generate_token(files)
    
    # Create the script filename
    script_filename = f"linkfavs-{token}.sh"
    
    # Check if the script already exists
    if os.path.exists(script_filename):
        print(f"Error: Script {script_filename} already exists. Choose a different name or remove the existing file.")
        sys.exit(1)
    
    # Get the directory path for IMAGE_ROOT
    image_dir = list(directories)[0]
    
    # Extract just the basenames of the files for the script
    basenames = [os.path.basename(f) for f in files]
    
    # Generate the shell script content
    script_content = f"""#!/usr/bin/env bash

set -e

IMAGE_ROOT="{image_dir}"

IMAGES_TO_LINK=(
    {"\n    ".join([f'"{filename}"' for filename in basenames])}
)

. ./common.sh
main
"""
    
    # Write the shell script
    with open(script_filename, "w") as f:
        f.write(script_content)
    
    # Make the script executable
    os.chmod(script_filename, 0o755)
    
    print(f"Created script: {script_filename}")
    
if __name__ == "__main__":
    main()

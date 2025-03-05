#!/usr/bin/env bash

set -e

# Run all linkfavs scripts
for script in linkfavs-*.sh; do
    # Skip if file doesn't exist
    [ -f "$script" ] || continue
    
    echo "Running $script..."
    ./"$script"
done

echo "All linkfavs scripts completed"
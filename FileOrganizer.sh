#!/bin/bash
# Author: Gowri Sankar
# This script is used to perform the directory organization with reading the directory as input and seprating files in to respective directories
# Usage: ./filename.sh directoryname

directory=$1
cd $directory
for file in *; do 
    if [ -f "$file" ]; then
        ext="${file##*.}"
        if [ ! -d "$ext" ]; then
            mkdir "$ext"
        fi
        mv "$file" "$ext/"
        echo "$file moved to $ext"
    fi
    done 
    echo "Files have been organized into directories based on their extension"

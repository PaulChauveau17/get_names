#!/usr/bin/env python

import argparse
import glob
import os
import sys

default_folder = "files_containing_names"

def get_basenames(path_pattern):
    """
    Takes a path pattern (can be a file, directory or a specific glob pattern) 
    and returns a list of basenames (without their extensions).
    """
    # Recursively find all files matching the pattern
    file_paths = glob.glob(path_pattern, recursive=True)

    # Filter out directories
    file_paths = [f for f in file_paths if os.path.isfile(f)]

    # Get basenames without extension
    basenames = [os.path.splitext(os.path.basename(f))[0] for f in file_paths]
    
    return basenames

def handle_path(path):
    """
    Handle absolute and relative path.
    """
    if os.path.isabs(path):
        return path
    else:
        return os.path.abspath(path)

def print_until_digit(basename):
    """
    - Split the basename (without extension) on '_'
    - Collect substrings until the first one that contains a digit
    - Then stop completely (even if later substrings are valid)
    """

    parts = basename.split('_')
    result = []
    for part in parts:
        if any(char.isdigit() for char in part):
            # One could decide to display the rest
            break
        if part:  # Skip empty parts from "__"
            result.append(part)
    print(result)

def main():
    parser = argparse.ArgumentParser(
        description="Get the first non numerical substrings from file(s), directorie(s) or glob pattern(s)",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=
        """
Special glob characters:
  *   matches any number of characters in a file or folder name (non-recursive)
  **  matches any number of directories (recursive)

Examples:

python get_names.py files_containing_names/Farida___Bekroukra_11_06_2025_11_06_2025_9dk5sqh0na3nv0l

python get_names.py files_containing_names/* # finds all files in 'files_containing_names'

python get_names.py files_containing_names/subfolder/*.txt # finds .txt files in 'files_containing_names/subfolder'

python get_names.py files_containing_names/'my folder'/* # finds all files in 'files_containing_names/my folder'
  
python get_names.py 'files_containing_names/**/*' # finds all files, recursively (on every subdirectory)
        """
      )

    parser.add_argument(
        "-v", "--verbose",
        action='store_true',
        help="Prints extra information, useful to debug"
    )

    parser.add_argument(
        "patterns",
        nargs="*",
        default=[f"{default_folder}/**/*"], # default: checks in default directory recursively
        help="Path of the input (examples: folder/file, folder/* or 'folder/**/*')"
    )

    # Collecting program arguments
    args = parser.parse_args()

    # Print them if -v option was found
    if (args.verbose):
      print(args.patterns)

    basenames = []

    for pattern in args.patterns:
      # Getting path from positional args
      path = handle_path(pattern)
      if (args.verbose):
        print(pattern, path)

      # getting just the basename without extension
      basenames += get_basenames(path)

    if not basenames:
        print("No matching files found.", file=sys.stderr)
        sys.exit(1)

    for basename in basenames:
        # print the name(s), surname(s)
        print_until_digit(basename)

if __name__ == "__main__":
    main()
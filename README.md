# Getting names from filenames

## Tutorial

```bash
python get_names.py --help # shows help message and examples
python get_names.py files_containing_names/* # finds all files in 'files_containing_names'
python get_names.py # finds all files in default_folder, recursively
```

## Edit default folder

```python
# Default folder (relative path), used if there is no args given to the program
default_folder = "files_containing_names" # Edit me (files will be recursively checked from here)
```
### Info

Tested on Ubuntu with linux style pathes: path/to/folder
Need to try on Windows

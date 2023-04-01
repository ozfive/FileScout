# FileScout
FileScout is a command-line interface utility that helps you discover files that have been created after a certain date and time.


## Installation
Clone this repository and run the filescout.py file in a Python environment.

## Usage

```shell
python filescout.py [directory] [YYYY-MM-DD HH:MM:SS]
```

## How it works

FileScout uses the `os`, `hashlib`, and `datetime` Python modules to find files that were created after the specified date and time.

First, it walks through the specified directory and its subdirectories to hash each file's content using the `hash_file()` function. It then stores the file path in two dictionaries, `files_hash` and `filenames`, based on its hash and filename, respectively.

It then finds files with duplicate content and filenames but unique content, and sorts them by their creation and modification timestamps. Finally, it prints the duplicates in a user-friendly way.

## Example
```shell
python filescout.py "~/Downloads" "2023-03-31 00:00:00"

This will search the Downloads directory for files created after midnight on March 31st, 2023.

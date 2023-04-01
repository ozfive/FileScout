import os
import time
import argparse
from datetime import datetime

def find_new_files(directory, timestamp):
    new_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.exists(file_path):
                file_mtime = os.path.getmtime(file_path)
                if file_mtime > timestamp:
                    new_files.append(file_path)
    return new_files

def main():
    parser = argparse.ArgumentParser(description='Find new files in a directory since a given timestamp.')
    parser.add_argument('directory', help='Directory to scan for new files')
    parser.add_argument('timestamp', help='Timestamp in the format "YYYY-MM-DD HH:MM:SS"')

    args = parser.parse_args()

    datetime_obj = datetime.strptime(args.timestamp, '%Y-%m-%d %H:%M:%S')
    timestamp = datetime_obj.timestamp()

    new_files = find_new_files(args.directory, timestamp)

    print(f'New files since {args.timestamp}:')
    for file in new_files:
        print(file)

if __name__ == '__main__':
    main()

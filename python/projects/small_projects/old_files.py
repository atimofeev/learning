#!/usr/bin/python3
"""Show old and new downloaded files in colors."""
import os
from datetime import datetime
from datetime import timedelta

BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
FILES_FOLDER = '/home/atimofeev/Downloads'
FILES = os.listdir(FILES_FOLDER)
DAYS_TO_EXPIRE = 30

timestamps = []

now = datetime.now()
expire_date = now - timedelta(days=DAYS_TO_EXPIRE)
expire_timestamp = expire_date.timestamp()

for item in FILES:
    full_path = os.path.join(FILES_FOLDER, item)
    timestamps.append((os.path.getatime(full_path),
                       os.path.getctime(full_path),
                       os.path.getmtime(full_path), full_path))
    # create list of tuples with timestamps and path

for timestamp in timestamps:
    filepath = timestamp[-1]
    if any(time <= expire_timestamp for time in timestamp[:-1]):
        # iterate 'time' through remaining tuples of 'timestamp'
        print(f"{BOLD}{RED}{filepath}{RESET}")
        # files older than DAYS_TO_EXPIRE will be colored red
    else:
        print(f"{BOLD}{GREEN}{filepath}{RESET}")
        # non-expired files will be shown in green

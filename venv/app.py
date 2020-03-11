""" A program to determine how many unique sender
    email addresses are included in a given file

    author: Fatih IZGI
    date: 05-Mar-2020
    version: python 3.8.1
"""

from typing import List, Set, IO

file_name: str = "mbox.txt"
emails: Set[str] = set()  # to store the emails

try:  # to open the file
    path: IO = open(file_name, "r")
except FileNotFoundError:
    print(f"File {file_name} is not found")
else:
    with path:  # close path after opening
        for line in path:
            if line.startswith("From:"):  # find specific lines
                try:
                    emails.add(line.split(" ")[1].strip("\n"))  # get only the value from the line
                except IndexError:  # if no data found
                    print("Corrupted line >> {} << is omitted".format(line.strip('\n')))  # do not include it to the average

    count: int = len(emails)  # number of emails
    print(f"The number of unique email adress(es) in {path.name} is {count}")
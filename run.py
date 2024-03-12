"""
Description:
This module contains the main function to execute the program. 

Input:
A URL from which the content will be downloaded and processed.

"""

import sys
from downloader import process_urls_from_file

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 run.py URL/File/argument")
        return

    arg = sys.argv[1]
    process_urls_from_file(arg)

if __name__ == "__main__":
    main()

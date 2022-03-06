#!/usr/bin/python3

#
# File:         mru_functions.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         20-Aug-21
# Description:  Define functions that help with code legibility and code reuse.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#

"""
The time module has the sleep() function which gives some break (0.5 to 1 second) between each part of the program.

The requests nodule allows for the exchange of HTTP requests.

The bs4 module has the BeautifulSoup which downloads data of HTML files of the website. It requires pre-installation –> pip install bs4.
"""

import time
import requests
from bs4 import BeautifulSoup as bs


# A function to draw a line break.
def line():
    print('\n-----------------------------------------------------------------------\n')
    time.sleep(1)


# A function to find all other  definitions of a  word.
def find_all_definitions(count, definition):
    for i in range(2, count + 1):
        print(f'Entry {i} of {count}', end = '')
        if i == 2:
            i = definition.find_next('span', class_='dtText')
        else:
            i = j.find_next('span', class_='dtText')
        j = i
        if ': ' not in i.get_text():
            print(': ', end = '')
        print(i.get_text())


# A function to pronounce the word.
# It returns the  URL of the .mp3 file.
def mp3(text):
    locate = text.find('contentURL')
    mp3_url = []
    for i in text[locate + 14:]:
        if i == '"':
            return mp3_url
        else:
            mp3_url.append(i)
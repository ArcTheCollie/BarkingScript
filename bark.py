__author__ = 'am004929'

import time
from random import choice

from termcolor.termcolor import colored

COLORS = ('blue', 'red', 'green', 'magenta', 'white', 'yellow')

while(1):
    print colored('Bark!', choice(COLORS))
    time.sleep(1)
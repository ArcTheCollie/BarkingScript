__author__ = 'am004929'

from termcolor import colored
import time
from random import choice

COLORS = ('blue', 'red', 'green', 'grey', 'magenta', 'white')

while(1):
    print colored('Bark!', choice(COLORS))
    time.sleep(1)
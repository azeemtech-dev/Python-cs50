import sys

from say import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

from say import goodbye

if len(sys.argv) ==2:
    goodbye(sys.argv[1])

import sys
sys.path.insert(0,"./..")

from BBextractor import extractall
from os.path import join

print("Hi")
extractall.test()

path = "/home/user/export"
fname = join(path, "test.txt")

with open(fname, "w") as f:
    f.write("hello")
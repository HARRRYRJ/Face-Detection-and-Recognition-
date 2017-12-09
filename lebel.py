#This code lebel your trainig dataset. This is only for testing purpose.
import os
import sys
path = "/home/vishal/mukesh/"
i = 1
for file1 in os.listdir(path):
    os.rename(os.path.join(path, file1), os.path.join(
        path, "mukesh" + "." + str(i) + ".jpg"))
    i = i + 1

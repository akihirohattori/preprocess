import glob
import os
import subprocess
import sys
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

home_dir = os.path.expanduser("~")
path = os.path.join(home_dir, "Documents/gra/HAY_A_AMICA_3_HAYAMICA_V1_0/data/2005*")

subprocess.call("echo --- > check01.txt",shell=True)
for di in sorted(glob.glob(path), key = natural_keys):
    subprocess.call("echo "+ di +" >> check01.txt",shell=True)
    res = subprocess.run("gethead " +di + "/*.fit IMG_NO_1 >> check01.txt", stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
    res1 = subprocess.run("gethead " +di + "/*.fit BINNING >> check01.txt", stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
    sys.stdout.buffer.write(res.stdout)
    sys.stdout.buffer.write(res1.stdout)

inputFile = "check01.txt"
outputFile = "check.txt"

containWord = []
NGWord = ["___"]

for line in open(inputFile):
    for i in NGWord:
        if i in line:
            break
    else:
        for i in containWord:
            if i not in line:
                break
        else:
            with open(outputFile,mode = 'a') as f:
                f.write(line)


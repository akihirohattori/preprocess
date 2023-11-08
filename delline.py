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
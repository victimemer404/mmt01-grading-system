FILES = ["SD-5sub.txt", "SD-10sub.txt"]
fileIndexCounter = 0

for files in FILES:
    with open(files, "r") as activeFile:
        data = activeFile.readlines()

    one = 0
    five = 0
    hundred = 0

    for line in data:
        if float(line) < 0.01:
            one += 1
        elif 0.01 <= float(line) < 0.05:
            five += 1
        else:
            hundred += 1

    if fileIndexCounter == 0:
        print("5 SUBJECTS")
    else:
        print("10 SUBJECTS")

    print("99% {} values".format(one))
    print("95% {} values".format(five))
    print("Unsafe {} values".format(hundred))

    fileIndexCounter += 1

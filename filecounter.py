FILES = ["SD-5sub.txt", "SD-10sub.txt"]
fileIndexCounter = 0

for files in FILES:
    with open(files, "r") as activeFile:
        data = activeFile.readlines()

    safe = 0
    unsafe = 0

    for line in data:
        if float(line) < 0.05:
            safe += 1
        else:
            unsafe += 1

    if fileIndexCounter == 0:
        print("5 SUBJECTS")
    else:
        print("10 SUBJECTS")

    print("Safe {} values".format(safe))
    print("Unsafe {} values".format(unsafe))

    fileIndexCounter += 1

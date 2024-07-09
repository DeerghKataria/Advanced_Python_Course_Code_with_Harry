def readFile(fileName):
    try:
        with open(fileName, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Error: The File {fileName} is not Present")


readFile("Chapter 12/Chapter 12 Practice/1.txt")
readFile("Chapter 12/Chapter 12 Practice/2.txt")
readFile("Chapter 12/Chapter 12 Practice/3.txt")
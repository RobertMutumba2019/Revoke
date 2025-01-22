try:
    f = open("demofile.txt")
except FileNotFoundError:
    print("The file 'demofilr.txt' was not found.")


f = open("demofile.txt", "r")
print(f.read())
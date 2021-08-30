import os
if os.path.exist("data.txt"):
    file=open("data.txt", "r")
    for i in file:
        print(i)
    file.close()
    os.remove("data.txt")
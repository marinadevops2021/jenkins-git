import os
if not os.path.exist("data.txt"):
    file=open("data.txt", "a")
    file.write("Marina Minasov")
    file.close()
else:
    print("File exist")
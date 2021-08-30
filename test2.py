import os
if not os.path.exist("data.txt"):
    file=open("data.txt", "a")
    file.write("Marina Minasov")
    file.close()
if os.path.exist("data.txt"):
    print("File exist")
from typing import List

def read_integers() -> List[int]:
    intline = input()
    strlist = intline.split(",")
    listm =[]
    for s in strlist:
        listm.append(int(s))
    return listm

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

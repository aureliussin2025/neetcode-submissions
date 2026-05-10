from typing import List

def read_integers() -> List[int]:
    l1 = input()
    l2 = l1.split(",")
    for i in range(len(l2)):
        l2[i] = int(l2[i])
    return l2
    pass

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

import collections

def firstUnqChar( s:str)->int:
    count = collections.Counter(s)

    for index,ch in enumerate(s):
        if count[ch] == 1:
            return index,ch
    return -1

s = "Utkarsh Bardia"
print(firstUnqChar(s))
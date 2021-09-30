def canConstruct(ransomNote:str, magzine:str) -> bool:
    s,i = sorted(ransomNote),0
    for c in sorted(magzine):
        i +=i < len(s) and s[i]==c
    return i==len(s)


ransomeNote = "aa"
magzine = "aab"

print(canConstruct(ransomeNote,magzine))
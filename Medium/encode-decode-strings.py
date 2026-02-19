from typing import List

def encode(strs: List[str]) -> str:
    # Your code here
    res = []
    for s in strs:
        res.append(str(len(s)) + "#" + s)
    return "".join(res)

def decode(s: str) -> List[str]:
    # Your code here
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        word = s[j + 1 : j + 1 + length]
        res.append(word)

        i = j + 1 + length
        
    return res

# Read input
raw = input().strip()
strs = raw.split(",") if raw else []
encoded = encode(strs)
decoded = decode(encoded)
print(','.join(decoded) if decoded else "empty")
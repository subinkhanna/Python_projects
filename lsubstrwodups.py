
inString = "abcabcbb"
l = 0
holdSubstring = []
maxlen = 0

while l <= (len(inString)-1):
    for r in range(l,len(inString)):
        print(l, r)
        if inString[r] not in holdSubstring:
            holdSubstring.append(inString[r])
            maxlen = max(maxlen, len(holdSubstring))
        else:
            break
    
    holdSubstring.clear()
    l += 1

print(maxlen)
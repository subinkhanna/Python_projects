##Similar to regular dict now since 3.7 in a way that 
## it remembers the order in which key, value pairs were inserted

from collections import defaultdict

myDefaultDict = defaultdict(str)
myDefaultDict['Jack'] = 'cheese'
myDefaultDict['Tommy'] = 'Jones'
print(myDefaultDict)
print(f"Value is {myDefaultDict['Subin']}")
# deque - double ended queue - imported from collections
# append(), appendleft()
# pop(), popleft()
# rotate()
# extend(), extendleft()
# reverse()

from collections import deque
from typing import Any

people = ['Mario', 'Luigi', 'Toad']

queue = deque(people)

queue.append('Bowser')

queue.popleft()
queue.appendleft('Daisy')
print(queue)

queue.rotate()  # -1 or -n for counter clockwise
print(queue)

queue.extend(['Subin'])
queue.extendleft(['Bob','Tom'])

print(queue)

queue.reverse()
print(queue)

d: deque[any] = deque() # for int do deque[int]
print(d)

try:
    d.pop()
except IndexError:
    print("Queue is empty")


d.extend([1,2,3,4,5,6])
d.remove(3)
print(d)

d_list = [1,2,3,4,5,6]
d_list.remove(3)
print(d_list)

##Slicing does not work on deque. Need to convert to list   list(d)

d.insert(2, 100)
print(d)

d.insert(4, 2)
print(d)

print(d.count(-1))

d.reverse()
print(d)

d.rotate()
print(d)

d.clear()
print(d)


d.extend([1,2,3,4,5,6])
print(d)

print(d.count(3))
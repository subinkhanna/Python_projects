# deque - double ended queue - imported from collections
# append(), appendleft()
# pop(), popleft()
# rotate()
# extend(), extendleft()
# reverse()

from collections import deque

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

from collections import deque

queue = deque(["danish","basit","qais"])
queue.append("owais")
queue.append("majid")
print(queue)
queue.popleft()

queue.popleft()

print(queue)

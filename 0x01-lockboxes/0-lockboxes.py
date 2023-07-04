#!/usr/bin/python3

from collections import deque

def canUnlockAll(boxes):
    n = len(boxes)
    visited = set()
    visited.add(0)  # Mark the first box as visited
    queue = deque([0])  # Initialize the queue with the first box

    while queue:
        box = queue.popleft()
        keys = boxes[box]

        for key in keys:
            if key not in visited and key < n:
                visited.add(key)
                queue.append(key)

    return len(visited) == n

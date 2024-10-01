"""
Queue may be implemented with Lists just as Stacks. But deque are preferred
because they allowed optimized accessing/deleting from both ends.

Deleting from the front of a list is O(n) as all other elements need to be shifted

Also, with deque, we can implement double-ended Queues.
"""

from collections import deque


class Queue:
    def __init__(self):
        self._data = deque()

    def is_empty(self):
        # TODO: Replace 'pass' with your code
        if self._data:
            return False
        else:
            return True

    @property
    def size(self):
        # TODO: Replace 'pass' with your code
        return len(self._data)

    def enqueue(self, item):
        # TODO: Replace 'pass' with your code
        self._data.append(item)

    def peek(self):
        # TODO: Replace 'pass' with your code
        try:
            return self._data[0]
        except IndexError:
            print("The list is empty.")
        except:
            print("Something has gone wrong.")

    def dequeue(self):
        # TODO: Replace 'pass' with your code
        try:
            # item = self._data.copy()[0]
            # self._data.remove(self._data[0])
            # return item
            return self._data.popleft()
        except IndexError:
            print("The list is empty.")
        except:
            print("Something has gone wrong.")


    def __str__(self) -> str:
        return str(self._data)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(20)
    q.enqueue(50)
    print(q)
    print("Size of Queue: ", q.size)
    print("Peek the Queue: ", q.peek())
    print("Pop from Queue: ", q.dequeue())
    print("Peek the Queue: ", q.peek())
    print("Size of Queue: ", q.size)
    print("Pop from Queue: ", q.dequeue())
    print("Size of Queue: ", q.size)
    print("Peek the Queue: ", q.peek())

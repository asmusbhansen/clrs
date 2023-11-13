import heapq as hq


class MinIndexPriorityQueue:

    _queue = []

    def push(self, key, index):

        hq.heappush(self._queue, (key, index))
        print()

    def pop(self):

        return hq.heappop(self._queue)

mipq = MinIndexPriorityQueue()


from queue import PriorityQueue


class Solution:
    def leastInterval(self, tasks, n):
        task_map = {}

        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1

        queue = PriorityQueue()

        for freq in task_map.values():
            queue.put((-freq, freq))

        cool_down = {}
        curr_time = 0

        while not queue.empty() or cool_down:
            if curr_time in cool_down:
                freq = cool_down[curr_time]
                del cool_down[curr_time]
                queue.put((-freq, freq))
            if not queue.empty():
                _, freq = queue.get()
                freq -= 1
                if freq > 0:
                    cool_down[curr_time + n + 1] = freq

            curr_time += 1

        return curr_time

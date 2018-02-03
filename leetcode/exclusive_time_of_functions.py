class Log:
    def __init__(self, log):
        self.id, self.type, self.time = log.split(":")
        self.id = int(self.id)
        self.time = int(self.time)

class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        logs = [Log(log) for log in logs]
        stack = []
        id_to_time = {}

        for log in logs:
            if log.type == "start":
                if log.id not in id_to_time:
                    id_to_time[log.id] = 0
                if stack:
                    top = stack[-1]
                    id_to_time[top.id] += log.time - top.time
                stack.append(log)
            else:
                top = stack.pop()
                id_to_time[top.id] += log.time - top.time + 1
                if stack:
                    stack[-1].time = log.time + 1

        return [id_to_time[k] for k in sorted(id_to_time.keys())]

def answer(numbers):
    s = set()
    s.add(0)
    next = numbers[0]

    start, last = 0, 0

    while next not in s:
        s.add(next)
        last = next
        next = numbers[next]

    start = next
    answer = 0

    while start is not last:
        answer += 1
        start = numbers[start]

    return answer+1


print(answer([1, 3, 0, 4, 1, 4, 4]))

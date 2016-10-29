def hotels(arrive, depart, K):
    arrive.sort()
    depart.sort()

    start, end = 0, 0
    booked = 0

    while start < len(arrive) and end < len(depart):
        while start < len(arrive) and end < len(depart) and arrive[start] < depart[end]:
            booked += 1
            if booked > K:
                return False
            start += 1
        booked -= 1
        end += 1

    return True

print(hotels(
    [ 30, 12, 15, 2, 21, 12, 1, 31, 7, 40, 29, 6, 48, 19, 23, 10, 26, 6, 20, 44, 44, 34, 44, 38 ],
    [ 36, 54, 47, 19, 66, 33, 41, 69, 23, 80, 64, 28, 93, 23, 62, 15, 49, 19, 58, 64, 60, 60, 57, 82 ],
    23
))

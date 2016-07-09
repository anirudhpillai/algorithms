N = int(input())
ratings = []

for n in range(N):
    ratings.append(int(input()))

left = [1]*N
right = [1]*N

for i in range(1, N):
    if ratings[i] > ratings[i-1]:
        left[i] = left[i - 1] + 1

for i in range(N-2, -1, -1):
    if ratings[i] > ratings[i+1]:
        right[i] = right[i+1] + 1

total = 0

for i in range(N):
    total += max(left[i], right[i])

print(total)

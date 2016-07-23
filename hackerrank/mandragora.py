T = int(input())
for _ in range(T):
    N = int(input())
    mandragoras = sorted(map(int, input().split()), reverse=True)
    P, fought = 0, 0
    for i in range(N):
        fought += mandragoras[i]
        P = max(P, fought * (N-i))
    print(P)

def list(X, Y, Z, N):
    return [[i, j, k] for i in range(0, X) for j in range(0, Y) for k in range(0, Z) if ((i + j + k) != N)]

X = int(input())
Y = int(input())
Z = int(input())
N = int(input())
print(list(X, Y, Z, N))

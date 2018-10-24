n = int(input())
for i in range(n):
    l = [int(x) for x in input().split()]
    l_1 = list(set(l))
    l_1.sort()
    print(l_1[-2])




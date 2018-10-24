if __name__ ==  '__main__':
    for _ in range(int(input())):
        l = [int(x) for x in input().split()]
        t = tuple(l)
        print(hash(t))

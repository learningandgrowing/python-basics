N = int(input())
if N&1== 1:
    print("Weird")
elif N&1==0 and (2<=N and N<=5):
    print("Not Weird")
elif N&1==0 and (6<=N and N<=20):
    print("Weird")
elif N&1==0 and (N>=20):
    print("Not Weird")
    

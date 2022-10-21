#ppsum
# cook your dish here
t = int(input())

while t!=0:
    t-=1
    
    # read input
    l = [int(x) for x in input().split()]
    s = (l[1] * (l[1]+1)) // 2

    for i  in range(l[0] - 1):
        s = (s * (s+1)) // 2

    print(s)

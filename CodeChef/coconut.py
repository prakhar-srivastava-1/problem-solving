# cook your dish here
t = int(input())

while t!=0:
    t-=1
    l = [int(x) for x in input().split()]
    print(l[2]//l[0] + l[3]//l[1])
    

import builtins
a = int(input())

b = tuple(map(int,input().split()))
print (hash(b))
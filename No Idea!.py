m, n = map(int,input().split())
sample = list(map(int,input().split()))
count = {}
for i in range(len(sample)):
    count[sample[i]] = 0
for i in range(len(sample)):
    count[sample[i]] = count[sample[i]]+1


A = set(map(int,input().split()))
B = set(map(int,input().split()))
happiness = 0
A1 = A.intersection(sample)
B1 = B.intersection(sample)

for i in A1:
    happiness += count[i]
for i in B1:
    happiness -= count[i]
print(happiness)
a = input()

count = {}
for i in range(len(a)):
    count[a[i]] = 0
for i in range(len(a)):
    count[a[i]] = count[a[i]]+1
b= dict(sorted(count.items()))
print (b)
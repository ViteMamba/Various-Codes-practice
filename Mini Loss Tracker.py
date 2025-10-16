loss = int(input())
target = float(input())
result= 0.0
for i in range(loss):
    result+=float(input())
if float(result/loss) <= target:
    print("PASS")
else:
    print("RETRY")
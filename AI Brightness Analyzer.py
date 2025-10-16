nits = list(map(int,input().split()))
result = float(sum(nits)/len(nits))
if result < 85:
    print("Dark Image")
elif result<= result and result<=170:
    print("Normal Image")
else :
    print("Bright Image")
x, min_v, max_v = map(float,(input().split()))
result =float(x-min_v)/float(max_v-min_v) 
print(f"{result:.2f}")
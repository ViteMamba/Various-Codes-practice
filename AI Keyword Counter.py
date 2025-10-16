message = list((input().split()))
keyword = ['ai', 'data', 'model', 'learn', 'train', 'neural']
counter=0
for word in message :
    if word in keyword :
        counter+=1
if counter >=2  :
    print("AI Detected")
else :
    print("Not AI Related")
message = input().split()
happymood = ['happy','joy','smile']
badmood = ['sad','cry','angry']

done=0
for word in message:
    if word in happymood:
        print("Happy Mood")
        done=1
        break
    elif word in badmood:
        print("Sad Mood") 
        done=1
        break
if done == 0:
    print("Neutral Mood")
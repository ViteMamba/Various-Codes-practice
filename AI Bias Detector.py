predictions = list((input().split()))
a = predictions.count("A")
b = predictions.count("B")
if float(float(a/len(predictions))*100) > 70 :
    print ("Biased Model")
elif float(float(b/len(predictions))*100) > 70:
    print("Biased Model")
else :
    print("Fair Model")

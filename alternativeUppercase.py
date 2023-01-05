# Test case 1: In the first sample, the given string is thakurcollege converting the odd position letter to uppercase we get tHaKuRcOlLeGe.

# Test case 3: In the third sample, the given string is shashtra converting the odd position letter to uppercase we get sHaShTrA.
n=int(input())
for i in range(3):
    a=input()
    l=len(a)
    
    for j in range(1,l,2):
        a=list(a)
        a[j]=a[j].upper()
    print("".join(a)) 
# for every number i in  range l and r , alice has to add all the min and max digit of each number

# Korosuke is confused how to solve it and asks for your help. Can you help him out?




# n=int(input())
n=12
for r in range(n):
    a,b=input().split()
    a=int(a)
    b=int(b)
    sum1=0
    
    
    for i in range(a,b+1):
        if(a>100):
            last=i%10
            rem=int(i/100)
            sum1+=(rem+last)
        else:
            last=i%10
            rem=int(i/10)
            sum1+=(rem+last)
   
     
            
    

    print(sum1)
# In this program we are trying to get number of sum of the all possible combination of a perticular number

def waysToBreakNumber( n ):
    a=0
    for i in range(n+1):
        for j in range (n+1):
            for k in range (n+1):
                if(i+j+k == n):
                    a= a+1
# 003,030,300,012,120,102,021,210,201,111 = 10          
                
    return a          
print(waysToBreakNumber( 3))
        
   
# Checks numbers from 1 to 10 for even, odd, and divisibility by 3
sum = 0

for i in range(1, 11):
    if i % 2 == 0:
        print(i,"= Even",end="") 
        sum+= 1
    else:
       print(i,"= odd",end="") 
    
    if i % 3 == 0:
       print( ", Divisible by 3")
    else:
        print()
print("Total even numbers:", sum)
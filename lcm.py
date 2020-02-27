def lcm(x,y):
    if x>y:
        greater = x
    else:
        greater = y
        
    while True:
        if(greater % x== 0) and (greater % y==0):
            lcm=greater
            break
        greater+=1
    return lcm
    
num1=int(input("Enter a no: "))
num2=int(input("Enter a no: "))
print("the lcm is: ",lcm(num1,num2))

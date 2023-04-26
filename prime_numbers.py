n1=int(input("enter the lowest range:"))
n2=int(input("enter the highest range:"))
print("the prime numbers between 'n1' and 'n2' are:")
for num in range(n1,n2+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)


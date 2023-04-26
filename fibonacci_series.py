n=int(input("enter the no of terms:"))
n1=0
n2=1
count=0
print("the fibonacci series:")
while count<n:
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
    count+=1


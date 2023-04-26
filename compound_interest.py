import math
p=float(input("enter principal amount:"))
t=float(input("enter time:"))
r=float(input("enter the rate of interest:"))
ci=p*(pow((1+r/100),t))
print("the compound interest is:",ci)


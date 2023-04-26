ch=input("enter the character:")
if(ch>='1' and ch<='9'):
    print("given character is a digit")
elif(ch>='A' and ch<='z'):
    print("the given character is in uppercase")
elif(ch>='a' and ch<='z'):
    print("given character is in lowercase")
else:
    print("given character is special character")


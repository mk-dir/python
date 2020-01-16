
pasw= str(input("Enter Password: "))

if len(pasw)<5:
    print("Password Too Short")

elif len(pasw)>15:
    print("Password to Long")

elif len(pasw)<=15:
   print("Welcome To Whatever.com")

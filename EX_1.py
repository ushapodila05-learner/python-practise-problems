a=int(input( "Enter a number: "))
print (a)
if a > 18:
    print("YES")
else:    
    print("NO")

####################
b=int(input( "Enter b number: "))
print(b)
if b%2==0:
    print("EVEN")
else:
    print("odd")
    
#######################
a=int(input( "Enter a number: "))
b=int(input( "Enter b number: "))

if a>b :
    print(" a is Maximum")
else:
    print(" b is maximum")
###############################
a=int(input( "Enter a number: "))
b=int(input( "Enter b number: "))
c=int(input("Enter c number: "))
if a>b and a>c :
    print(" a is Maximum")
elif a<b and b>c:
    print(" b is maximum")
else:
     print(" c is maximum")    
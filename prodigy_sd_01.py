print("Select the correct unit")
print("1)Calsius")
print("2)kelvin")
print("3)Fahrenheit")
y=int(input("Enter the option "))
if y==1:
    x=float(input("Enter the value "))
    print("Kelvin",x+273.15)
    print("Fahrenheit",x*1.8+32)
elif y==2:
    z=float(input("Enter the value "))
    print("celsius",z-273.15)
    print("Fahrenheit",(z-273.15)*1.8+32)
else:
    a=float(input("enter the value "))
    print("calsius", (a-32)*5/9)
    print("kelvin", (a-32)*5/9+273.15)
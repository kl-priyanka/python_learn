#to convert the data in degrees to radians
#1 pi (3.14) radians = 180 degrees
# x * (3.14/180)
# divide minutes with 60 and seconds with 3600
d=float(input("Enter the data in degrees: "))
m=float(input("Enter the data in minutes: "))
s=float(input("Enter the data in seconds: "))
rad = (d+(m/60)+(s/3600))*(3.14/180)
print("The value in radians is : ")
print(rad)
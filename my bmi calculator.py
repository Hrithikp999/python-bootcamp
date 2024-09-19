weight=float(input("enter your weight in kg"))
height=float(input("enter your height in meters"))
x=weight/(height*height)
if x<18.5:
 print("underweight")
elif x>=18.5 and x<24.9:
 print("normal weight")
elif x>=25 and x<29.9:
 print("overweight")
else:
 print("obese")
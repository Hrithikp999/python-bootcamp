age = int(input("ENTER YOUR AGE"))
gender =  input("ENTER YOUR GENDER")

if(age > 17 and gender == "female"):
    
     print("ELLIGIBLE FOR JOB GOVT JOB")
     
elif(age > 17 and gender == "male"):

     print("YOU ARE ELLIGIBLE for PVT JOB")

else:
    print("Not elligible")
    
    
    
#  METHOD 2   
 
if(age > 17):
   if(gender == "female"):
        print("not elligible for govt job")
   elif(gender == "male"):
    print("YOU ARE NOT ELLIGIBLE")
    
    
    # WAP TO CHECK THE GREATEST NO AMONG 3 NO
    
x = input("ENTER ANY NUMBER")
y = input("ENTER SECOND NUMBER")
z = input("ENTER THE THIRD NUMBER")

if(x > y and x > z):
    print("x is greater")
elif(y > x and y > z ):
    print("y is greater")
else:
    print("z is greater")
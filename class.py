class hrithik:
    age = 23
    print("hrithik parashar")
# print object and pass class properties

x= hrithik()
print(x.age)

class Age_calculate:
    current_year=int(input("enter current year"))
    birth_year=int(input("enter your birth year"))
    age=current_year-birth_year
x=Age_calculate()
print(x.age)
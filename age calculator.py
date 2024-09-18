from datetime import datetime 

def calculate_age(birthdate):
       current_date = datetime.now()
       
       age = current_date - birthdate
       year = age.days // 365
       months = (age.days % 365) //30
       days = (age.days % 365) % 30
       
       return year, months, days
   
year = int (input("ENTER THE BIRTH YEAR"))
month = int(input("ENTER THE BIRTH MONTH"))
day = int(input("ENTER THE BIRTH DAY"))

birthdate = datetime(year,month,day)
years,months,days = calculate_age(birthdate)

print(f"age:{years} years, {months} months, {days} days")
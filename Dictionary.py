myDict={
      "keys":"values",
      "name":"hrithik parashar",
      "email":"hrithiks916@gmail.com"
}
print(type(myDict))
print(myDict)

for keys in myDict:
       print(myDict[keys])
       
print(myDict.get("email"))
myDict["name"]="neeraj"
print(myDict)
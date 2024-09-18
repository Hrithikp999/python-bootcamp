friendname = ["hrithik","neeraj","amit",1,2,3,4]
print("before",friendname)

friendname.append("shivani") #add a name  in the end of the list
print("after",friendname)

friendname.insert(0, "shivani")  #print in indexing where akash will be written
print(friendname)

friendname.remove("amit")
print(friendname)

friendname.clear()  
print(friendname)
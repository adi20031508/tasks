#string are immutable never changes and cannot
name= "Harry"
nameshort =  name[0:3] #start from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1= name[2]
print(character1)

#negative slicing
print(name[-4:-1])
print(name[1:4]) #positive krlo

print(name[:4]) #means 0
print(name[1:]) #means length

a="abcdefghijklmnopqrst"
a= a[1:9:4]
print(a)

#funtions
name="aditi"
print(len(name))
print(name.endswith("iti"))
print(name.startswith("a"))
print(name.capitalize()) #start characther  

#escape sequence characthers
a="aditi is a good girl\nbut she is dumb\n hence she will learn python to get smart"
print(a)
#\n next line \t give tap jitni space
#\""\ will read double coat
b="aditi is a \"girl\""
print(b)

#questions
a= input("enter the name: ")
print(f"Good Afternoon {a}")

letter='''Dear <|Name|>,
Your are selected!
<|Date|>'''
print(letter.replace("<|Name|>,", "Aditi").replace("<|Date|>", "15 aug"))

a="aditi is a good  girl  in school"
print(a.find("  ")) #-1 means double space nhi hai
#find index         # koi aur number means space hai index mai

a="aditi is a good  girl  in school"
print(a.replace("  ", " "))




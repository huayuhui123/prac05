email=input("Email:")
dict={}
while email!=" ":
    nameread=email.split("@")[0].title()
    namecheck=' '.join(nameread.split("."))
    choice=input("Is your name {}?(Y/n)".format(namecheck))
    if choice.upper()=='Y':
       dict[email]=namecheck
    elif (choice.upper()=='N')or (choice=='no'):
       name=input("Name:")
       dict[email]=name
    email = input("Email:")
for key,value in dict.items():
    print("{}({})".format(value,key))
print("finished")
print("over")
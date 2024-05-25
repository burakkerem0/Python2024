import datetime
users=[]

while True:
    name=input("Write your name: ")
    surname=input("Write your surname: ")
    job = input("What is your job? ")
    birthday=input("What is your birthday year: ")
    today_date = datetime.date.today() 
    age= today_date.year - int(birthday)
    users_dict={"Name":name,
                "Surname": surname,
                "Birthday":birthday,
                "Job": job,
                "Age":age}
    users.append(users_dict)
    print(users)
    decision = input("To continue press Enter, To finish press q: ")
    if decision == "q":
        break
    else:
        continue
print(users)



 



   








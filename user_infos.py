infos = []
while True:

    name = input("Adınızı giriniz: ")
    surname = input("Soyadınızı giriniz: ")
    job = input("Mesleğinizi giriniz:")
    birthday = input("Doğum yılınızı giriniz: ")


    if name =="q" or surname == "q" or job == "q" or birthday == "q":
         break

    import datetime
    today = datetime.date.today().year
    age = bugun- int(birthday)

    users_dict={"ad": name, 
                            "soyad": surname, 
                            "meslek": job,
                            "yas": age }
  
    infos.append(users_dict)
    print(infos)   


 



   








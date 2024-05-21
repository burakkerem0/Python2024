word_list = {
    "Associated" : "bağlantılı",
    "intention" : "amaç",

}
point = 0 
print("Please write that words meaning.")
for words in word_list:
    users_input = input(words + " : ")
    if users_input.lower() == word_list[words]:
        point += 5
        print("Congrats! You're points is: " , point)
    else:
        print("You didn't reply corretly") 
print(" You finish de quiz with", point, "points")                        
    


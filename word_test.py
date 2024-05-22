word_list = {
    "Associated" : "bağlantılı",
    "intention" : "amaç",
    "wealthy" : "varlıklı",
    "enhance" : "artırmak",      
    "crucial" : "çok önemli",
    "alter" : "değiştirmek", 
    "assume": "varsaymak", 
    "confidence": "güven",
    "contribute": "katkı yapmak", 
    "debate" : "tartışmak", 
    "capable": "yetenekli",
    "struggle" : "mücadele",
    "generate": "oluşturmak",
    "emphasize": "vurgulamak",
    "satisfied" : "memnun",
    "decant" : "dökmek",
    "instance": "örnek",
    "resolve" : "kararlılık",
    "intention" : "amaç",
    "tend" : "eğiliminde olmak",
    "treat" : "davranmak",
    "label" : "etiket",
    "previously" : "daha önce",
    "encourage": "cesaretlendirmek",
    "indicate": "belirtmek",
    "statue": "heykel",
    "confident": "kendinden emin"

}
point = 0 
print("Please write that words meaning.")
for word in word_list:
    users_input = input(word + " : ")
    if users_input.lower() == word_list[words]:
        point += 5
        print("Congrats! You're points is: " , point)
    else:
        print("You didn't reply corretly") 
print(" You finish de quiz with", point, "points")                        
    


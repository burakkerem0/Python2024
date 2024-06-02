# This app about finding lucky number via users name, surname and birthday

vowels = ("a", "e", "i", "o", "u")
name_surname = input("Write your name and surname: ")
birthday = input("Wtite your birhday like DD.MM.YYYY: ")

# i need to decrease the space charecter
space_chracter = name_surname.count(" ")

# with this def I want to learn total letter
def total_letters(name_surname):
    total_letters = 0 
    for letter in name_surname:
        total_letters +=1 
    return total_letters

total_letters_count = total_letters(name_surname)



# with this def I want to learn total vowel sound
def is_it_vowel(name_surname):
    total_wovel_sound = 0
    for letter in name_surname.lower():
        if letter in vowels:
            total_wovel_sound +=1
    return total_wovel_sound


# number of vowel sounds
total_wovel_sound_count = is_it_vowel(name_surname)

# number of consonant 
consonant_letters = total_letters_count - total_wovel_sound_count - space_chracter


# get birthday and finding times of 3
int_number_in_birthday = []
for number in birthday:
    if number.isdigit():
        int_number_in_birthday.append(int(number))

times_3 = list(filter(lambda x: x%3 == 0, int_number_in_birthday))

count_times_3 =len(times_3)


print(f"Your lucky number is {total_wovel_sound_count}{consonant_letters}{count_times_3}")









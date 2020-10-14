import random

gibbet_list = ["SUN", "MUG", "CAT", "DOG", "HAT", "RED", "CAR", "PEN", "HEN", "FIG"]
random_word = random.choice(gibbet_list)
length = len(random_word)
count = 0
num_lett = 0
empty_l=["_","_","_"]

def compare(num_letters):
    num_letters = num_letters + 1
    return num_letters


while count < 6:
    input_word = input("guss the letters for a word from 3 letters: ")
    if input_word in random_word:
        num_lett = compare(num_lett)
       # print(re.sub(empty_l,input_word,random_word.re.find(input_word))

        if num_lett == length :
            print("Good Job")
            print("the word is:", random_word)
            break

        ind_1=random_word.find(input_word)
        print("this letter located in{} ".format(ind_1))
        empty_l[ind_1]=input_word
        print(empty_l)

    else:
        print("no my dear...choose another one")
        count = count + 1
else:
    print("OH no..see you next time")
import difflib
import json

def translate():

    file_pointer = open('data.json')
    data = json.load(file_pointer)

    user_input = input('Enter the word ')

    if user_input in data.keys():
        return data[user_input]
    elif user_input.lower() in data.keys():
        return data[user_input.lower()]
    elif user_input.capitalize() in data.keys():
        return data[user_input.capitalize()]
    elif len(difflib.get_close_matches(user_input,data.keys())) > 0:
        print("Do you mean {}".format(difflib.get_close_matches(user_input,data.keys())[0]))
        user_choice = input("Enter Y if yes N if No ")
        if user_choice == "Y":
            return data[difflib.get_close_matches(user_input,data.keys())[0]]
        else:
            return "Enter correct word"
    else:
        return "word does not exist in dictionary"


if  __name__ == "__main__":
    return_value = translate()
    if type(return_value) == list:
        for element in return_value:
            print(element)
    else:
        print(return_value)


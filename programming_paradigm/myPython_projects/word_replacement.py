greet = """Hi everyone! I am Astainy and I love programming ha ha ha ha ha """



# print(greet.replace(word_to_replace, word_replacement ))

def word_function():

    print(greet)
    word_to_replace = input("Enter word to replace: ")
    word_replacement = input("Enter new word as replacement: ")

    if len(word_to_replace) < 1 and len(word_replacement) < 1:
        print("Please enter word to replace.")

    else:
        print(greet.replace(word_to_replace, word_replacement))

word_function()
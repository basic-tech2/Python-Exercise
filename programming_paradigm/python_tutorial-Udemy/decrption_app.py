

# from encription_app import crpted

# Reversed encrption app in python
"""Create an app in python that will reverse an 
encrpted sentence into readable format"""

# Create a function 
def Crpted_Word(sentence):

    encrpted_word = 'Processing...................  \nConverted to: '
    for convert in sentence:
      
        if convert in "1":
            encrpted_word += "a"
        elif convert in "2":
            encrpted_word += "b"

        elif convert in "3":
            encrpted_word += "c"
        elif convert in "4":
            encrpted_word += "d"

        elif convert in "5":
            encrpted_word += "e"
        elif convert in "6":
            encrpted_word += "f"

        elif convert in "7":
            encrpted_word += "g"
        elif convert in "8":
            encrpted_word += "h"
        
        elif convert in "9":
            encrpted_word += "i"
        elif convert in "!":
            encrpted_word += "j"

        elif convert in "@":
            encrpted_word += "k"
        elif convert in "#":
            encrpted_word += "l"
        elif convert in "$":
            encrpted_word += "m"

        elif convert in "%":
            encrpted_word += "n"
        elif convert in "^":
            encrpted_word += "o"
        elif convert in "&":
            encrpted_word += "p"

        elif convert in "*":
            encrpted_word += "q"
        elif convert in "~":
            encrpted_word += "r"

        elif convert in ")":
            encrpted_word += "s"
        elif convert in "_":
            encrpted_word += "t"

        elif convert in "+":
            encrpted_word += "u"
        elif convert in "{":
            encrpted_word += "v"

        elif convert in "/":
            encrpted_word += "w"
        elif convert in "?":
            encrpted_word += "x"

        elif convert in "=":
            encrpted_word += "y"
        elif convert in ">":
            encrpted_word += "z"
        elif convert in "0":
            encrpted_word += " "
        elif convert in "|":
            encrpted_word += "."
        
        else:
            
            # encrpted_word += sentence
            # crpted(encrpted_word)
            encrpted_word = "Processing................... \nCan not be decrpted. "
            
          
    return encrpted_word

print(Crpted_Word(input("Decrpt text: ")))



            
            
            
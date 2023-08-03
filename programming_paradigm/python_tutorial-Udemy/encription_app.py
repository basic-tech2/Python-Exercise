# A basic encription app 

"""Our user will write down a sentence than our crpting engine will convert
each letter in the sentence with numbers and symbols."""



def crpted(sentence): # create a function
    encrption = ' ' # variable set to an empty string
    for element in sentence: # give the name "element" as out for variable
        if element in "Aa":
            encrption += "1"
        elif element in "Bb":
            encrption += "2"
        elif element in "Cc":
            encrption += "3"
        elif element in "Dd":
            encrption += "4"
        elif element in "Ee":
            encrption += "5"
        elif element in "Ff":
            encrption += "6"
        elif element in "Gg":
            encrption += "7"
        elif element in "Hh":
            encrption += "8"
        elif element in "Ii":
            encrption += "9"
        elif element in "Jj":
            encrption += "!"
        elif element in "Kk":
            encrption += "@"
        elif element in "Ll":
            encrption += "#"
        elif element in "Mm":
            encrption += "$"
        elif element in "Nn":
            encrption += "%"
        elif element in "Oo":
            encrption += "^"
        elif element in "Pp":
            encrption += "&"
        elif element in "Qq":
            encrption += "*"
        elif element in "Rr":
            encrption += "~"
        elif element in "Ss":
            encrption += ")"
        elif element in "Tt":
            encrption += "_"
        elif element in "Uu":
            encrption += "+"
        elif element in "Vv":
            encrption += "{"
        elif element in "Ww":
            encrption += "/"
        elif element in "Xx":
            encrption += "?"
        elif element in "Yy":
            encrption += "="
        elif element in "Zz":
            encrption += ">"
        elif element in " ":
            encrption += "0"
        elif element in ".":
            encrption += "|"
        else:
            encrption = encrption + element

    return encrption
print(crpted(input("What do you want to encrpt: ")))


#  Try to create a decrption app as practice
# print(crpted(input(" dfjsdfj")))
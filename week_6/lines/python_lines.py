
# user's input
word = input("What is the input string?").strip()

if word == "":
    print("You should enter any string!")
else:
    # this part of code counts number of charaters in given string
    count = len(word)
    print(word + " has a " + str(count) + " characters")
word = input("camelCase:")
char_list = list(word)

count = 0
for i in char_list:
    if count == 0:
        print("snake_case:", end="")
    count += 1
    if i.isupper():
        i = f"_{i.lower()}"
        print(i, end="")
    else:
        print(i, end="")
    if count == len(word):
        print(end="\n")













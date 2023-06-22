
def convert(sentence):
    x = sentence.replace(":)", "🙂")
    y = x.replace(":(", "🙁")
    return y

def main():
    sentence = input()
    print(convert(sentence))

main()
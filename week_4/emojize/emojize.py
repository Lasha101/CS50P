import emoji
text = input("input:")
emojized_text = emoji.emojize(text, language='alias')

print("output:", emojized_text)
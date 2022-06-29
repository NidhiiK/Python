message = input(">")

words = message.split(' ')

emojis = {":)": "😀", ":(": "😞 "}

output = ""
for words in words:
    output += emojis.get(words, words) + " "
print(output)

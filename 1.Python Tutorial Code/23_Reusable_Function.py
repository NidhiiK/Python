def emoji_converter(message):
    words = message.split(' ')

    emojis = {":)": "😀", ":(": "😞 "}

    output = ""
    for words in words:
        output += emojis.get(words, words) + " "
    print(output)

    message = input("< ")
    print(emoji_converter(message))
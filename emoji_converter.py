def emoji_converter(message):
    words = message.split(' ')
    emojies = {
        ":)": "😀",
        ":(": "😔",
        "heh": "😏",
        "chi?": "😒"
    }
    output = ""
    for word in words:
        output += emojies.get(word, word) + " "
    return output


message1 = input(">")
print(emoji_converter(message1))
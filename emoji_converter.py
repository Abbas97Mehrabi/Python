message = input(">")
words = message.split(' ')
print(words)
emojies = {
    ":)": "😀",
    ":(": "😔"
}
output = ""
for word in words:
    output += emojies.get(word, word) + " "
print(output)
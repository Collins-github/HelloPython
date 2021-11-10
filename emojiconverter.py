message = input(">")
def emoji_dict(message):
	word = message.split(" ")
	emojis = {
		":(":"🙃",
		":)":"🤧",
		"_+":"😇",
		"**":"🤩"
	}
	output = ""
	for words in word:
		output += emojis.get(words, words) + " "
	return output
print(emoji_dict(message))
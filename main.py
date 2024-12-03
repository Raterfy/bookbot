def main():
	text = get_text()
	cw = count_word(text)
	cc = count_character(text)
	# print(f"Frankenstein Text{text}")
	# print(f"The book contains {cw} words.")
	# print(f"Character counts: {cc}")
	report(cw, cc)


def get_text():
	with open("books/frankenstein.txt") as f:
		file_content = f.read()
	return file_content

def count_word(text):
	word_list = text.split()
	return len(word_list)

def count_character(text):
	lower_string = text.lower()
	word_dict = {}
	for character in lower_string:
		if character.isalpha():
			if character in word_dict:
				word_dict[character] += 1
			else:
				word_dict[character] = 1
	return word_dict

def report(word_count, character_count):
	print("--- Begin report of books/frankenstein.txt ---")
	print(f"{word_count} are found in Frankenstein.txt")
	sorted_cound_character = sorted(character_count.items(), key=lambda item: item[1], reverse=True)
	for char, count in sorted_cound_character:
		print(f"The '{char}' character was found {count} times")
	print("--- End report ---")


main()
open_text = open("letter.txt", "r")

find_word = ""
for word_line in open_text:
    for word in word_line:
        if word in ["a", "e", "i", "o", "u"]:
            find_word += word
    if find_word == "aeiou":
        print(word_line, end="")

    find_word = ""

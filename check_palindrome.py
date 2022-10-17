def check_palindrome(word_str):
    plain_word = word_str.lower().replace(" ", "").replace("'", "")
    rev_word = plain_word[::-1]
    # word_array = list(plain_word)
    # word_array.reverse()
    # rev_word = "".join(word_array)
    return plain_word == rev_word


if __name__ == '__main__':
    user_input = input("Enter a sentence to check if palindrome: ")
    if check_palindrome(user_input):
        print(f'"{user_input}" is palindrome')
    else:
        print(f'"{user_input}" is not palindrome')

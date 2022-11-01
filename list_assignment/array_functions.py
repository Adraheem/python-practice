def largest_element_in_array(array):
    largest_element = 0
    for element in array:
        if element > largest_element:
            largest_element = element
    return largest_element


def reverse_array(array):
    reversed_array = []
    for i in range(len(array) - 1, -1, -1):
        reversed_array.append(array[i])
    return reversed_array


def is_in_array(array, element):
    is_in = False
    if element in array:
        is_in = True
    return is_in


def odd_position_list(array):
    odd_list = []
    for i in range(0, len(array), 2):
        odd_list.append(array[i])
    return odd_list


def even_position_list(array):
    even_list = []
    for i in range(1, len(array), 2):
        even_list.append(array[i])
    return even_list


def total_element(array):
    total = 0
    for el in array:
        total += el
    return total


def is_palindrome(word_str):
    plain_word = word_str.lower().replace(" ", "").replace("'", "")
    rev_word = plain_word[::-1]
    return plain_word == rev_word

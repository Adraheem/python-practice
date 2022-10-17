def reverse(array):
    new_array = []
    for i in range(len(array)-1, -1, -1):
        new_array.append(array[i])
    return new_array


def print_array(array, title):
    print(title)
    for i in array:
        print(f"{i} ", end=" ")
    print("\n")


if __name__ == '__main__':
    num_array = [4, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
    num_array_reversed = reverse(num_array)

    print_array(num_array, "Original array")
    print_array(num_array_reversed, "Reversed array")

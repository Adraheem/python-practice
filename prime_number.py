def is_prime(num):
    response = True
    for counter in range(2, num):
        if num % counter == 0:
            response = False
            break
    return response


if __name__ == '__main__':
    for i in range(2, 100):
        if is_prime(i):
            print(i, end=' ')

if __name__ == '__main__':
    rectangle = [
        "".center(12, "*"),
        "*".ljust(11)+"*",
        "*".ljust(11)+"*",
        "*".ljust(11)+"*",
        "*".ljust(11)+"*",
        "*".ljust(11)+"*",
        "*".ljust(11)+"*",
        "*".ljust(11)+"*",
        "*".ljust(11)+"*",
        "".center(12, "*"),
    ]

    arrow = [
        "*".center(15),
        "***".center(15),
        "*****".center(15),
        "*******".center(15),
        "*".center(15),
        "*".center(15),
        "*".center(15),
        "*".center(15),
        "*".center(15),
        "*".center(15),
    ]

    for i in range(10):
        print(rectangle[i], arrow[i])

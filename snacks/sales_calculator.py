def do_sales(order_list):
    total = 0
    quantities = 0
    for item in order_list:
        if item[0] in range(1, 6):
            quantities += item[1]

            match item[0]:
                case 1:
                    total += 2.98 * item[1]
                case 2:
                    total += 4.50 * item[1]
                case 3:
                    total += 9.98 * item[1]
                case 4:
                    total += 4.49 * item[1]
                case 5:
                    total += 6.87 * item[1]

    print("Total price: {total:.2f} dollars".format(total=total))
    print("Total quantity: {}".format(quantities))


def print_products():
    return int(input(
            "Choose a product\n" +
            "1 -> Product 1 ($2.98)\n" +
            "2 -> Product 2 ($4.50)\n" +
            "3 -> Product 3 ($9.98)\n" +
            "4 -> Product 4 ($4.49)\n" +
            "5 -> Product 5 ($6.87)\n\n" +
            "99 -> quit\n"))


if __name__ == '__main__':
    order = []
    product_no = print_products()
    while product_no != 99:
        quantity = int(input("Enter quantity: "))
        order.append([product_no, quantity])
        product_no = print_products()
    do_sales(order)

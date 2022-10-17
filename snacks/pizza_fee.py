import math


def get_number_of_offenders(acc_bal, fee, pizza=5500, no_of_pizza=5):
    deficit = (pizza * no_of_pizza) - acc_bal
    return math.ceil(deficit / fee)


if __name__ == '__main__':
    balance = 4300
    for i in [100, 200, 500, 1000, 1500, 2000]:
        print(f"Number of offenders at #{i} per offence: {get_number_of_offenders(balance, i)}")

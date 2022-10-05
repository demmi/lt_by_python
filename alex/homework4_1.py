from functools import reduce

def big_num_sum1(number: int) -> int:
    while number >= 10:
        number = sum(map(int, str(number)))
    return number


def big_num_sum2(number: int) -> int:
    while len(str(number)) > 1:
        number = reduce(lambda a, b: int(a) + int(b), str(number))
    return number


if __name__ == "__main__":
    big_num = int(input("Input any number: "))
    print(f"SUM Result 1: {big_num_sum1(big_num)}")
    print(f"SUM Result 2: {big_num_sum2(big_num)}")


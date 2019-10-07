def fix_count_lower(number, lower_cnt, counter):
    while lower_cnt % 10 != 0:
        num = lower_cnt
        while num > 0:
            if num % 10 == number:
                counter = counter + 1
            num = num / 10
        lower_cnt = lower_cnt + 1
    return counter, lower_cnt


def fix_count_upper(number, upper_cnt, counter):
    while upper_cnt % 10 != 0:
        num = upper_cnt
        while num > 0:
            if num % 10 == number:
                counter = counter + 1
            num = num / 10
        upper_cnt = upper_cnt - 1
    return counter, upper_cnt


def occurrence(number, cnt_upper, cnt_lower):
    counter = 0
    upper_cnt = cnt_upper
    lower_cnt = cnt_lower
    counter, upper_cnt = fix_count_upper(number, upper_cnt, counter)
    counter, lower_cnt = fix_count_lower(number, lower_cnt, counter)
    while lower_cnt < upper_cnt:
        if (lower_cnt / 10) % 10 == number and (upper_cnt - lower_cnt) >= 10:
            counter = counter + 10
        else:
            counter = counter + 1
        lower_cnt = lower_cnt + 10
    return counter


if __name__ == '__main__':
    lower = int(input("Lower bound: "))
    upper = int(input("Upper bound: "))
    x = int(input("Digit: "))
    print("Counter : ", occurrence(x, upper, lower))

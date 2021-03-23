def main():
    check_sum = 0
    cc_number = get_valid_cc_number()
    n = cc_number
    while n > 0:
        last_digit = n % 10
        check_sum += last_digit
        n //= 100

    n = cc_number // 10

    while n > 0:
        eo_digit = n % 10
        times_two = eo_digit * 2
        check_sum += (times_two % 10) + (times_two // 10)
        n //= 100

    count = 0
    divisor = 10
    n = cc_number

    while n != 0:
        n //= 10
        count +=1

    for i in range(count - 2):
        divisor *= 10

    first_digit = cc_number // divisor
    first_two_digits = cc_number // (divisor // 10)

    if check_sum % 10 == 0:
        if count == 15 and (first_two_digits == 34 or first_two_digits == 37):
            print("AMEX")
        elif count == 16 and (first_two_digits > 50 and first_two_digits < 56):
            print("MASTERCARD")
        elif (count == 13 or count == 16) and first_digit == 4:
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")


def get_valid_cc_number():
    while True:
        cc_number = (int)(input("Number:"))
        if cc_number > 0:
            break
    return cc_number


main()
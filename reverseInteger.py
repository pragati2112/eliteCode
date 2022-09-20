def reverse(x: int):
    """
    :type x: int
    :rtype: int
    """

    reversed_digit = ''
    largest_int = 2147483647
    smallest_int = -2147483648

    if smallest_int < x < largest_int:

        if x > 0:
            while x:
                x, last_digit = divmod(x, 10)
                reversed_digit += str(last_digit)


        elif x < 0:
            y = str(x).replace('-', '')
            z = int(y)
            while z:
                z, last_digit = divmod(z, 10)
                reversed_digit += str(last_digit)

            reversed_digit = '-' + reversed_digit

        else:
            return 0
    else:
        return 0

    if smallest_int < int(reversed_digit) < largest_int:
        return int(reversed_digit)

    else:
        return 0


x = 1534236469

print(reverse(x))

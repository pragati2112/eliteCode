def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)

    left_to_right = x
    right_to_left = x[::-1]

    if left_to_right == right_to_left:
        return True
    else:
        return False


x = 10

print(isPalindrome(x))

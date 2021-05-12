def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    excepted_dict = {
    "IX":9,
    "IV":4,
    "XL":40,
    "XC":90,
    "CD":400,
    "CM":900
    }


    sample_dict={
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }

    n=len(s)
    num = 0
    for i in range(n):
        if i < n-1:
            if dic[s[i]]>= dic[s[i+1]]:
                
                num = num + dic[s[i]]
            else:
                num = num - dic[s[i]]
        else:
            num = num + dic[s[i]]

    return num


s = "MCMXCIV"

print(romanToInt(s))
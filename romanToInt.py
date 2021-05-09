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

    integer = 0

    if s in excepted_dict.keys():
        integer = integer+ excepted_dict[s]
        return integer


    for i in range(len(s)):
        try:
            j = i+1
            key = s[i]+s[j]
        except Exception as e:
            key = s[i]
       
        if key in excepted_dict.keys():
            integer = integer+ excepted_dict[key]
           
        else:
            integer = integer+sample_dict[s[i]]

    return integer

s = "MCMXCIV"

print(romanToInt(s))
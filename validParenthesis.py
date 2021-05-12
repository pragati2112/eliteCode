def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    sample_list = ['{}', '[]', '()']

    while any([op in s for op in sample_list]):
        s = s.replace('()', "").replace('{}', "").replace('[]', "")


    print(s) 
           
    if len(s)==0:
        return True    
    else:
        return False

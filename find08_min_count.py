def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    i=0
    mx=0
    ct=0
    while i<len(data):
        if mx>data[i]:
            a=mx=data[i]
            ct = data.count(mx)
        i+=1
    return ct

    

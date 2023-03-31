def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    i=0
    mx=0
    ct=0
    while i<len(data):
        if mx<data[i]:
            a=mx=data[i]
            ct = data.count(mx)
        i+=1
    return ct
print (find_max_count([1, 8, 3, 8, 5]))


def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    i=0
    mx=0
    while i<len(data):
        if mx<data[i]:
            mx=data[i]
        i+=1
    return mx
    
print (find_max([1, 2, 3, 4, 5]))

    
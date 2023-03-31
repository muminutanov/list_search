def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    i=0
    mx=0
    while i<len(data):
        if mx>data[i]:
            mx=data[i]
        i+=1
    return mx
    
print (find_min([1, 2, -3, 4, 5]))

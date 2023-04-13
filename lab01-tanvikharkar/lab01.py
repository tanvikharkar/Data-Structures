def max_list_iter(int_list):    # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""

    if len(int_list) == 0:
        return None
    
    elif all(x is None for x in int_list):
        raise ValueError
    
    else:
        return max(i for i in int_list if i is not None)
        

def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""

    if len(int_list) == 0:
        return []
    
    elif all(x is None for x in int_list):
        raise ValueError
    
    else:
        return [int_list[-1]] + reverse_rec(int_list[:-1])  # recursively calls function to return a final reversed int_list


def binarySearch(alist, item):  # must use recursion
    """recursively performs binary search on and returns True if item is in list
    If alist is empty, returns False. If alist or item is None, raises ValueError"""
    
    if len(alist) == 0:
        return False
    
    elif all(x is None for x in alist) or (item == None):
        raise ValueError
    
    elif item not in alist:
        return False
    
    else:
        end = len(alist)
        mid = (int(end / 2)) # rounds down to nearest int

        if (item == alist[mid]):
            return True
       
        elif (item > alist[mid]):  # right side of alist
            return binarySearch(alist[mid:], item)

        elif (item < alist[mid]):   # left side of alist
            return binarySearch(alist[:mid], item)
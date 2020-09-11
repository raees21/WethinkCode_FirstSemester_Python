
def find_min(element):
    """find minimum element in a list"""

    try:
        if len(element) == 1:
            return element[0]

        elif len(element) >= 2:
            if element[0] < find_min(element[1:]):
                return element[0]
            else:
                return find_min(element[1:])

        else:
            return -1

    except TypeError:
        return -1
        

def sum_all(element):
    """sum of an entire list"""

    
    try:
        if len(element) == 1:
            return element[0]
        
        elif len(element) > 1:
            if all(isinstance(x, int) for x in element) == True:
                return element[0] + sum_all(element[1:])
            else:
                return -1

        else:
            return -1

    except TypeError:
        return -1


def find_possible_strings(character_set, n):
    """Recursive string function for find_possible strings"""

    temp = []

    if n == 0:
        return character_set
     

    if n == 1:
        return character_set

    if n > 1:
       
        for i in character_set:
            for char in find_possible_strings(character_set, n-1):
                if all(isinstance(x, str) for x in character_set) == True:
                    temp.append(i+char)

        return temp

    



#print(find_min([7, 3, 5, 2, 6]))

#print(sum_all([7, 3, 5, 2, 6]))

#print(find_possible_strings(["a", "b", "c"], 3))


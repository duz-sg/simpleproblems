# Given a nested list with arbitrary level of nesting, write a function, flatten to flatten it.

# sample input:
x = [[4,5],[[1,2,3]],6]
# flatten(x) --> [4,5,1,2,3,6]


def flatten(element):
    res = []
    for item in element:
        if isinstance(item, int):
            res.append(item)
        if isinstance(item, list):
            for subitem in flatten(item):
                res.append(subitem)
    return res

print(flatten(x))
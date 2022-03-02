in_names = "A,B,C"
out_names = "D,E"


def eq(inputs):
    A, B, C = inputs
    X = A and not ((B or C) and (not B or not C))
    Y = ((not A and B) or (not A and not C)) and (not B or not C)
    D = X or Y
    E = not ((not A and not B) or not ((not A or not B) and C)) or (A and B)
    return [D, E]

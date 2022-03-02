in_names='A,B,C'
out_names='W'
def eq(inputs):
    A,B,C=inputs
    W=(D1 and D0 and A and B) or (D1 and not(D0) and A and B)
    return [W]
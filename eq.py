in_names='D1,D0,A,B'
out_names='W'
def eq(inputs):
    D1,D0,A,B=inputs
    W=(D1 and D0 and A and B) or (D1 and not(D0) and A and B)
    return [W]
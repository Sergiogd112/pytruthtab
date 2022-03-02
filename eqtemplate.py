# RENAME this file to eq.py when executing it
# Example using the circuit W from dygsis

# Input names
in_names='D1,D0,A,B'
# Output names
out_names='W'
#Defining the equation
def eq(inputs):
    # Unpacking the inputs
    D1,D0,A,B=inputs
    # The equations go here
    W=(D1 and D0 and A and B) or (D1 and not(D0) and A and B)
    # Write the list of outputs in order
    return [W]
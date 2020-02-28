def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The strands should have the same length")
    counter = 0
    for i, j in zip(strand_a, strand_b):
        if i != j: 
            counter += 1
    return counter
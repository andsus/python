def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('strands not equal in length')

    return sum(a != b for a,b in zip(list(strand_a),list(strand_b)))

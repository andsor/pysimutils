def index2parameter(
        index,
        lower_bound = 0.0,
        upper_bound = 1.0,
        geometric = false
    ):
    return smart_parameter_in_unit_interval_from_loop_index(index)
  
    
"""
Bit reversal:
http://stackoverflow.com/a/5333563 (John La Rooy)
http://stackoverflow.com/users/174728/gnibbler
"""
def smart_parameter_in_unit_interval_from_loop_index(index):

    n = int(index)
    if n <= 0:
        return 0.0

    # return the number of bits at the current resolution
    b = lambda n: int(math.ceil(math.log(n, 2))) if n else 0

    # return the (integer) denominator at the current resolution
    d = lambda n: int(math.pow(2, b(n))) if n else 0

    # return the index of the current position at the current resolution
    k = lambda n: int(n - d(n) / 2 - 1) if n > 1 else 0

    # reverses the bits
    bitreversal = lambda original, numbits: (
        sum(
            1 << (numbits - 1 - i) for i in range(numbits) if original >> i & 1
        ))

    # return the (integer) nominator at the current resolution
    nominator = lambda n: 2 * bitreversal(k(n), b(n) - 1) + 1

    return float(nominator(n)) / float(d(n)) if n else 0.0
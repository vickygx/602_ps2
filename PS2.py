def compute_G(A):
    # This method is OPTIONAL.  If implemented, it should take the A
    # matrix (a numpy.ndarray) and return the appropriate G matrix
    # (also a numpy.ndarray).  If you choose to use this method, you
    # will call it as part of encode().
    pass

def compute_H(A):
    # This method is OPTIONAL.  If implemented, it should take the A
    # matrix (a numpy.ndarray) and return the appropriate H matrix
    # (also a numpy.ndarray).  IF you choose to use this method, you
    # will call it as part of decode().
    pass

def compute_syndromes(H):
    # This method is OPTIONAL.  If implemented, it should take the H
    # matrix (a numpy.ndarray) and return a dictionary that provides a
    # mapping between error vectors and their corresponding symbols.
    # The data structures used within the mapping will differ
    # depending on your implementation of decode; for this reason, we
    # do not provide an explicit testing method for this function.  If
    # you choose to use this method, you will call it as part of
    # decode().
    pass

def encode(A, message):
    # This method is REQUIRED.  Here, you should implement the linear
    # encoder.  This requires the following steps:
    # 1. Calculate the G matrix
    # 2. Break the message into k-length blocks
    # 3. Use G to determine the codewords for each block
    # 4. Concatenate the codewords into a single string and return it
    pass

def decode(A, encoded_bits):
    # This method is REQUIRED.  Here you should implement the syndrome
    # decoder.  This requires the following steps:
    # 1. Calculate the H matrix
    # 2. Use H to set up the syndrome table
    # 3. Break the message into n-length codewords
    # 4. For each codeword, calculate the error bits
    # 5. If the error bits are nonzero, use the syndrome table to correct the error.
    # 6. Return the corrected bitstring
    #
    # Though we are not requiring it, we recommend you set up the
    # syndrome table before you perform the decoding, via the
    # compute_syndromes() function.  This will result in a more
    # organized design, and also a more efficient decoding procedure
    # (because you won't be recalculating the syndrome table for each
    # codeword).
    pass

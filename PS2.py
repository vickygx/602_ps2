import numpy as np

def compute_G(A):
    # Takes the A matrix (a numpy.ndarray) and return the appropriate 
    # G matrix = [I | A] (also a numpy.ndarray).
    k = A.shape[0]
    I = np.identity(k)
    return np.concatenate((I, A), axis=1)

def compute_H(A):
    # Takes in the A matrix (a numpy.ndarray) and returns the 
    # appropriate H matrix = [A^T | I] (also a numpy.ndarray).
    return np.concatenate((A.transpose(), np.identity(A.shape[1])), axis =1)

def compute_syndromes(H):
    # Takes the H matrix (a numpy.ndarray) and return a dictionary 
    # that provides a mapping between error vectors and their 
    # corresponding symbols. Only creates syndromes for 1-bit errors.
    # The keys will be a stringified version of the syndromes concatanated,
    # and the values will be index indicating the error.
    syndromes = dict()
    n = H.shape[1]
    k = n - H.shape[0]
    
    for i in xrange(0, k):
        error_vector = np.zeros(n)
        error_vector[i] = 1
        syndrome = H.dot(error_vector) % 2
        key = "".join(str(int(s)) for s in syndrome.tolist())
        syndromes[key] = i

    return syndromes 
    

def encode(A, message):
    k = A.shape[0]
    
    # Calculating the G matrix
    G = compute_G(A)

    # Break the message into k-length blocks
    messages = [" ".join(message[i:i+k]) for i in xrange(0, len(message), k)]

    # Use G to determine the codewords for each block
    codewords = ""
    for message in messages:
        msg_vector = np.fromstring(message, dtype=int, sep=" ")
        code = msg_vector.dot(G) % 2
        codewords += ''.join(str(int(c)) for c in code.tolist())

    return codewords

def decode(A, encoded_bits):
    # The syndrome decoder
    n = A.shape[0] + A.shape[1]
    k = A.shape[0]

    # Calculate the H matrix
    H = compute_H(A)
    
    # Setting up syndrome table
    syndromes = compute_syndromes(H)

    # Break the encoded_bits into n-length codewords
    codewords = [" ".join(encoded_bits[i:i+n]) for i in xrange(0, len(encoded_bits), n)]

    # For each codeword, calculate the error bits, by computing H*r^T = s
    correct_message = ""
    for codeword in codewords:
        codeword_vector = np.fromstring(codeword, dtype=int, sep=" ")
        codeword_syndrome = H.dot(codeword_vector) % 2
        syndrome_key = ''.join(str(int(c)) for c in codeword_syndrome.tolist())
        if syndrome_key in syndromes:
            error = syndromes[syndrome_key]
            codeword_vector[error] = (codeword_vector[error] + 1) % 2
        correct_message += ''.join(str(int(c)) for c in codeword_vector.tolist()[:k])

    return correct_message

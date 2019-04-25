from argparse import parse_args
import sys

def find_kmers_with_mismatches_and_reverse_complements(text, k, d):
    frequent_patterns = []
    frequency_array = computing_frequencies_with_mismatches(text, k, d)
    max_count = max(frequency_array)
    for i in range(0, 4**k - 1):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            if pattern not in frequent_patterns:
                frequent_patterns.append(pattern)
    return frequent_patterns

def computing_frequencies_with_mismatches(text, k, d):
    freq_arr = initialize_frequency_array(k)
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i+k]
        rc_pattern = reverse_complement(pattern)
        rc_neighborhood = neighbors(rc_pattern, d)
        neighborhood = neighbors(pattern, d)
        for neighbor in neighborhood:
            index = convert_sequence_to_num(neighbor)
            freq_arr[index] += 1
        for neighbor in rc_neighborhood:
            index = convert_sequence_to_num(neighbor)
            freq_arr[index] += 1
    return freq_arr
        
def reverse_complement(pattern):
    complements = {'A':'T', 'G':'C', 'C':'G', 'T':'A'}
    complement = [complements[nuc] for nuc in pattern]
    complement.reverse()
    return ('').join(complement)

def convert_sequence_to_num(sequence):
    nuc_vals = {"A":0, "C":1, "G":2, "T":3}
    seq_hex = 0
    power = len(sequence) - 1
    for nuc in sequence:
        hex_val = nuc_vals[nuc] * 4**power
        seq_hex += hex_val
        power -= 1
    return seq_hex

def number_to_pattern(index, k):
    num_to_nuc = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    if k == 1:
        return num_to_nuc[index]
    quotient = index // 4
    remainder = index % 4
    symbol = num_to_nuc[remainder]
    pattern = number_to_pattern(quotient, k - 1)
    return pattern + symbol
    
def initialize_frequency_array(k):
    return [0 for i in range(0, 4**k)]

def neighbors(pattern, d):
    nucs = {'A', 'G', 'T', 'C'}
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return nucs
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for suffix in suffix_neighbors:
        if hamming_distance(pattern[1:], suffix) < d:
            for nuc in nucs:
                neighborhood.add(nuc + suffix)
        else:
            neighborhood.add(pattern[0] + suffix)
    return neighborhood

def hamming_distance(p, q):
    hamming_distance = 0
    p_len = len(p)
    q_len = len(q)
    for i in range(0, p_len):
        if i < p_len and i < q_len and p[i] != q[i]:
            hamming_distance += 1
        elif not i < p_len:
            hamming_distance = hamming_distance + q_len - 1
        elif not i < q_len:
            hamming_distance = hamming_distance + p_len - 1
    return hamming_distance

if __name__ == '__main__':
    sequence, k, d = parse_args(sys.argv[1:])
    print(*find_kmers_with_mismatches_and_reverse_complements(sequence, k, d))
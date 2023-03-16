def best_score(a_dictionary):
    max_val = 0
    max_key = ''
    if not a_dictionary:
        return None
    for k in a_dictionary:
        if a_dictionary[k] > max_val:
            max_key = k
    return max_key
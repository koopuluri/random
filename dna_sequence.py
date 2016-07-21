
def build_state_machine(s, vocab):
    """
    State machine represented as: [{vocab_option: next_index}]
    """

    # building the options for the start state:
    start_options = {s[0]: 1}
    for v in vocab:
        if v != s[0]:
            start_options[v] = 0

    sm = [start_options]
    for i in xrange(len(s) - 1):
        curr_char, next_char = s[i], s[i + 1]
        options_map = {next_char: i + 2}

        # given a vocab option, find the next index if that option chosen:
        # note: Currently brute force approach, look to optimize finding this!
        def next_index(v):
            substr = s[:(i + 1)] + v
            for j in range(len(substr)):
                # compare j indices from front and j from back and see if same:
                if substr[:(j+1)] != substr[(len(substr) - j - 1):]:
                    return j

            return j

        # for each other option, determining which index to map to if it's chosen:
        for v in vocab:
            if v != next_char:
                options_map[v] = next_index(v)

        sm.append(options_map)

    return sm

def is_substring(needle, haystack):
    sm = build_state_machine(needle, set(needle))
    i = 0
    for c in haystack:
        if c in sm[i]:
            i = sm[i][c]
        else:
            i = 0

        # if terminal state reached, return True:
        if i == len(sm):
            return True

    return False

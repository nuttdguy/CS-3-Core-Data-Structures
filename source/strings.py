#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement contains here (iteratively and/or recursively)

    if pattern in text:
        return True
    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_index here (iteratively and/or recursively)
    if pattern is '':
        return 0

    text_size = len(text)                           # get the size of text for iteration
    compare_text = ''                               # set empty variable for text to match
    pattern_size = len(pattern)                     # get the size of pattern
    for idx in range(text_size):
        compare_text += text[idx]                   # store each letter of text with each iteration
        compare_text_size = len(compare_text)       # get the size of text to compare

        if compare_text_size == pattern_size:       # check size of compare text is equal to pattern size
            if compare_text in pattern:
                if compare_text_size <= 1:          # if compare text size is one or less one
                    return idx                      # return the idx
                else:
                    return idx - (compare_text_size - 1)  # otherwise, subtract (compare size - 1) to get current index

        if compare_text_size == pattern_size:       # reset text pattern minus pattern length
            if compare_text_size <= 1:
                compare_text = ''                   # size equal or less than one, set compare text to ''
            else:
                compare_text = compare_text[1:]     # otherwise, slice 1 letter from beginning and continue search
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_all_indexes here (iteratively and/or recursively)

    text_size = len(text)                           # get the size of text for iteration
    compare_text = ''                               # set empty variable for text to match
    pattern_size = len(pattern)                     # get the size of pattern
    match_total = 0
    match_list = []

    if pattern is '':                               # for special case of ''
        for emptyIdx in range(text_size):
            match_list.append(emptyIdx)
        return match_list

    for idx in range(text_size):
        compare_text += text[idx]                   # store each letter of text with each iteration
        compare_text_size = len(compare_text)       # get the size of text to compare

        if compare_text_size == pattern_size:       # check size of compare text is equal to pattern size
            if compare_text in pattern:
                if compare_text_size <= 1:          # if compare text size is one or less one
                    match_total += 1                # increment match total
                    match_list.append(idx)          # add the idx
                else:
                    # otherwise, subtract (compare size - 1) to get current index
                    match_total += 1                                       # increment match total
                    match_list.append(idx - (compare_text_size - 1))    # add the index

        if compare_text_size == pattern_size:       # reset text pattern minus pattern length
            if compare_text_size <= 1:
                compare_text = ''                   # size equal or less than one, set compare text to ''
            else:
                compare_text = compare_text[1:]     # otherwise, slice 1 letter from beginning and continue search

    return match_list


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()

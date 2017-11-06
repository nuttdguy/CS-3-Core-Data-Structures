#!python


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement contains here (iteratively and/or recursively)
    # WORST CASE == O(n2)
    has_pattern = find_all_indexes(text, pattern)       # O(n2)
    if has_pattern.__len__():                           # O(1)
        return True
    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_index here (iteratively and/or recursively)
    # WORST CASE == O(n2)

    if pattern is '':
        return 0
    try:
        return find_all_indexes(text, pattern)[0]       # O(n2) get the first value, which is index of pattern
    except IndexError:
        return None                                     # O(1) if list empty, return NONE - item was not found


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_all_indexes here (iteratively and/or recursively)
    # WORST CASE == O(n2)

    text_size = len(text)                           # O(1) get the size of text for iteration
    pattern_size = len(pattern)                     # O(1) get the size of pattern
    calc_range_stop = (text_size - (pattern_size - 1))      # O(1) calculate stop range for iteration

    slice_start = 0
    match_total = 0
    match_list = []

    if pattern is '':                               # for special case of ''
        for emptyIdx in range(text_size):           # O(N)
            match_list.append(emptyIdx)
        return match_list                           # O(1)

    for idx in range(0, calc_range_stop):           # O(N)
        slice_stop = pattern_size + slice_start         # O(1) set the slice stop
        compare_text = text[slice_start:slice_stop]     # O(1) slice letters of text with each iteration
        compare_text_size = len(compare_text)       # O(1) get the size of text to compare

        if compare_text_size == pattern_size:       # O(1) check size of compare text is equal to pattern size
            if compare_text == pattern:             # O(N)
                if compare_text_size <= 1:          # O(1) if compare text size is one or less one
                    match_total += 1                # O(1) increment match total
                    match_list.append(idx)          # O(1) add the current index position to list
                else:
                    match_total += 1                # O(1) increment match total
                    match_list.append(idx)          # O(1) add the current index position to list
            slice_start += 1                        # O(1) increment the slice start position

    return match_list                               # return the list


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # Uncomment these lines after you implement find_all_indexes
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

#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # implement the is_palindrome function iteratively here
    tl = len(text)              # set the length

    if tl <= 1:                 # check for zero or 1 occurrence
        return True

    reversed_text = ''
    forward_text = ''
    is_valid = True
    for idx in range(tl, 0, -1):                    # iterate through in reverse
        if text[idx - 1] in string.ascii_letters:
            reversed_text += text[idx - 1]          # apply current reverse as reversed text
        if text[tl - idx] in string.ascii_letters:
            forward_text += text[tl - idx]          # apply current char as forward_text
        if reversed_text is not forward_text:
            return False                            # break is any characters do not match
    return is_valid                                 # return as valid by default


def is_palindrome_recursive(text, left=None, right=None):
    # implement the is_palindrome function recursively here
    if left is None and right is None:
        right = len(text)               # set right length
        left = 0                        # set left

    if right <= 1:                      # check for zero or 1 occurrence
        return True

    if text[left] not in string.ascii_letters:
        return is_palindrome_recursive(text, left + 1, right)       # skip if not character, increment left plus 1
    elif text[right - 1] not in string.ascii_letters:
        return is_palindrome_recursive(text, left, right - 1)       # skip if not character, decrement right minus 1
    else:
        if text[left].lower() != text[right - 1].lower():
            return False                # if at any time, its not equal return false
        else:
            if left >= right:           # made it past mid-point, return true as all have matched
                return True
            return is_palindrome_recursive(text, left + 1, right - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()

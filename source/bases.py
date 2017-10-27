#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

"""Decode given digits in given base to number in base 10.
digits: str -- string representation of number (in given base)
base: int -- base of given number
return: int -- integer representation of number (in base 10)"""

# use dictionary to store HEX specific key:value pairs
HEX_DICT = {'A': 10, 'a': 10, 'B': 11, 'b': 11, 'C': 12, 'c': 12,
            'D': 13, 'd': 13, 'E': 14, 'e': 14, 'F': 15, 'f': 15,
            'G': 16, 'g': 16, 'H': 17, 'h': 17, 'I': 18, 'i': 18,
            'J': 19, 'j': 19, 'K': 20, 'k': 20, 'L': 21, 'l': 21,
            'M': 22, 'm': 22, 'N': 23, 'n': 23, 'O': 24, 'o': 24,
            'P': 25, 'p': 25, 'Q': 26, 'q': 26, 'R': 27, 'r': 27,
            'S': 28, 's': 28, 'T': 29, 't': 29, 'U': 30, 'u': 30,
            'V': 31, 'v': 31, 'W': 32, 'w': 32, 'X': 33, 'x': 33,
            'Y': 34, 'y': 34, 'Z': 35, 'z': 35}

HEX_VALUES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def decode(digits, base):

    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Decode digits from binary (base 2)
    # Decode digits from hexadecimal (base 16)
    # Decode digits from any base (2 up to 36)

    digits_list = list(digits)[::-1]    # convert to list, then reverse
    result = 0                          # initialize result to store value
    power = 0                           # set power to begin at n^0

    for num in digits_list:
        if HEX_DICT.get(num) is not None:   # check for HEX value
            num = HEX_DICT.get(num)             # assign value of corresponding hex key
        pw = base ** power              # n^0, n^1, n^2, n^3
        mod = int(num) % base           # modulus
        result += pw * mod              # multiply and add to result
        power += 1                      # increment power
    return result                       # decodes binary to integer


def encode(number, base):
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    assert number >= 0, 'number is negative: {}'.format(number)
    # Encode number in hexadecimal (base 16) [9AEF 0B1C 001A 4512]
    # Encode number in any base (2 up to 36)  [??]

    if number is 0:
        return '0'

    result = ''
    while number > 0:
        bit_value = number % base               # 1%2 = 1; will return number b/t 2 <= base <= 36

        if bit_value >= 10:
            bit_value = HEX_VALUES[bit_value - 10]       # return the character value

        result = str(bit_value) + result        # concat the result of 0 or 1
        number = int(number / base)             # divide by base, reduce by 1/2 for binary conversion
    return result                               # input '1101' > output 31


def convert(digits, base1, base2):
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # TODO: Convert digits from any base to any base (2 up to 36)

    decoded = decode(digits, base1)
    encoded = encode(decoded, base2)
    return encoded

    # string.digits is '0123456789'
    # string.hexdigits is '0123456789abcdefABCDEF'
    # string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
    # string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # string.ascii_letters is ascii_lowercase + ascii_uppercase
    # string.printable is digits + ascii_letters + punctuation + whitespace

    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')

# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

if __name__ == '__main__':
    main()


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
              'D': 13, 'd': 13, 'E': 14, 'e': 14, 'F': 15, 'f': 15}

# TODO: Decode digits from binary (base 2)
def decode(digits, base):

    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
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



    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    # 128 | 64 | 32 | 16 >> 8 | 4 | 2 | 0
def encode(number, base):
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    assert number >= 0, 'number is negative: {}'.format(number)
    # Encode number in binary (base 2) [1010 1010 1010] (12)
        result = 0
        power = 0
        while number > 0:
            pw = 10 ** power
            mod = number % 2
            result += pw * mod
            # number = round(number / 2)
            power += 1
        return result

    # TODO: Encode number in hexadecimal (base 16) [9AEF 0B1C 001A 4512]
    # use above function, continue to check hexi-decimal


    # TODO: Encode number in any base (2 up to 36)  [??]
    # ...


def convert(digits, base1, base2):
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)

    base2 = decode('10', 2)    # decode to binary
    print(base2)
    print(base2 == 2)










    # encode2 = encode(base2, 16)     # covert to hex
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
        # BASE II IS BINARY (ENCODE TO 10)
    base_10 = ''
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
        # BASE 10 TO BASE 16 (ENCODE FROM 2 10 16)
    base_16 = ''

    # TODO: Convert digits from any base to any base (2 up to 36)
        # REVISIT AFTER ALL OTHER IMPLEMENTATIONS

    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]


def main():
    """Read command-line arguments and convert given digits between bases."""
    convert(101011, 2, 8)
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


from collections import Counter

FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--"
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-"
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-"
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-"
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")


def convert_to_str(image):
    ''' Takes a list of lists, representing an
    image of numbers, and converts each pixel (int) into strings.'''

    str_image = []
    for layer in image:
        current_layer = []
        for digit in layer:
            current_layer.append(str(digit))
        str_image.append(current_layer)

    return str_image


def convert_font(font, num):
    ''' Converts the font into digit images, used for
    performing checks.'''

    digit = []
    if num == 0:
        num = 10
    num -= 1
    for layer in range(0, 5):
        digit_raw = font[layer*41:layer*41+41][(num*4)+1:(num*4)+4]
        digit_raw = digit_raw.replace('X', '1')
        digit_raw = digit_raw.replace('-', '0')
        digit += [p for p in digit_raw]
    return digit


def digit_to_layers(digit):
    ''' Takes an unrolled array of a single digit,
        and returns a 2D 5x3 array of layers. '''

    layers = []
    x = 0
    for _ in range(5):
        layers.append(digit[x:x+3])
        x += 3
    return layers


def positional_match(digit_layer, match_layer):
    ''' When a layer (3 x 1) of a digit matches exactly with
    the layer of the digit we're checking with, then the
    positional match rating increases by 1. '''

    positional_match = 0
    for x in xrange(5):
        for y in xrange(3):
            if digit_layer[x][y] == match_layer[x][y]:
                positional_match += 1
    return positional_match


def num_digits(image):
    ''' Calculate number of digits to process based on
    length of the overall layer of the image, minus spaces. '''

    x, d = 0, 0
    for _ in range(10):
        d += len(image[x+1:x+4])
        x += 4
    return d / 3


def checkio(image):
    ''' Monocaptcha - for each digit in a given 'image':

    1) 'Extract' next digit from the image.

    2) 'Unroll' digit into a 1D array (1x15) of pixels

    3) 'Check for a match' - iterate through potential matches
        (in global var 'FONT'), and unroll the digit.

        Then count pixels and positional alignment, and compare
        with those of the potential matching digit. Using
        thresholds to process noise, add the digit
        to the resultant string.
    '''

    conversion_print = ''
    # convert array 'image' to string
    str_image = convert_to_str(image)
    ndigits = num_digits(str_image[0])
    #split str image to digits
    for i in range(ndigits):
        current_digit = []

        # digit in sequence provided
        for l in str_image:
            digit_extract = l[(i*4)+1:(i*4)+4]
            current_digit += digit_extract  # digit unrolling
        # unroll current digit
        digilayers = digit_to_layers(current_digit)

        # scan for match
        for check in xrange(1, 11):
            match_digit = convert_font(FONT, check)
            img_pixels = Counter(current_digit)['1']
            md_pixels = Counter(match_digit)['1']
            matchlayers = digit_to_layers(match_digit)
            posmatch = positional_match(digilayers, matchlayers)
            # push digit along to final result, if it passes our thresholds
            if 14 <= posmatch <= 15 and (md_pixels <= img_pixels + 1):
                if check == 10:
                    check = 0
                conversion_print += str(check)

    return int(conversion_print)

if __name__ == '__main__':

    import unittest

    class MonoCaptchaTests(unittest.TestCase):

        def test_five_digit(self):
            test_case = [[0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0],
                        [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
                        [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                        [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]]
            self.assertEqual(checkio(test_case), 21312)

        def test_three_digit(self):
            test_case1 = [[0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                            [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0],
                            [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
                            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                            [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0]]
            self.assertEqual(checkio(test_case1), 519)

        def test_two_digit(self):
            test_case1 = [[0, 1, 0, 1, 0, 0, 1, 1, 0],
                            [0, 1, 0, 1, 0, 1, 0, 0, 0],
                            [0, 1, 1, 1, 0, 1, 1, 1, 0],
                            [0, 0, 0, 1, 0, 1, 0, 1, 0],
                            [0, 0, 0, 1, 0, 0, 1, 1, 0]]
            self.assertEqual(checkio(test_case1), 46)

    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, division

import time
import string
from collections import deque


class Five(object):
    def five(self, *args):
        return 5

    def __call__(self):
        return self.five()

    def up_high(self):
        return '⁵'

    def down_low(self):
        return '₅'

    def roman(self):
        return 'V'

    def convert_to(self, num):
        """convert to a number your specified.

        If you need other numbers I'd strongly suggest you call
        this function when your app starts up and cache the result."""
        one_fifth_of_five = self.five() / self.five()
        while num < one_fifth_of_five:
            num += one_fifth_of_five
        return num

    # Start of kinds of five in many languages, sorted by alphabetic.
    def arabic(self):
        return 'خمسة'

    def azerbaijani(self):
        return 'beş'

    def basque(self):
        return 'bost'

    def belarusian(self):
        return 'пяць'

    def bosnian(self):
        return 'pet'

    def bulgarian(self):
        return 'пет'

    def catalan(self):
        return 'cinc'

    def chinese(self):
        return '五'

    def choctaw(self):
        return 'tahlapi'

    def croatian(self):
        return 'pet'

    def czech(self):
        return 'pět'

    def dovah(self):
        return 'hen'

    def dutch(self):
        return 'vijf'

    def elvish(self):
        return 'lempe'

    def english(self):
        return 'five'

    def estonian(self):
        return 'viis'

    def finnish(self):
        return 'viisi'

    def french(self):
        return 'cinq'

    def german(self):
        return 'fünf'

    def greek(self):
        return 'πέντε'

    def hebrew(self):
        return 'חמש'

    def hindi(self):
        return 'पांच'

    def hungarian(self):
        return 'öt'

    def indonesian(self):
        return 'lima'

    def irish(self):
        return 'cúig'

    def italian(self):
        return 'cinque'

    def japanese(self):
        return '五'

    def kannada(self):
        return 'ಐದು'

    def klingon(self):
        return 'vagh'

    def korean(self):
        return '오'

    def latin(self):
        return 'quinque'

    def latvian(self):
        return 'pieci'

    def lithuanian(self):
        return 'penki'

    def mongolian(self):
        return 'таван'

    def norwegian(self):
        return 'fem'

    def persian(self):
        return 'پنج'

    def piglatin(self):
        return 'ivefay'

    def polish(self):
        return 'pięć'

    def portuguese(self):
        return 'cinco'

    def romanian(self):
        return 'cinci'

    def russian(self):
        return 'пять'

    def serbian(self):
        return 'pet'

    def slovakian(self):
        return 'päť'

    def slovenian(self):
        return 'pet'

    def spanish(self):
        return 'cinco'

    def swedish(self):
        return 'fem'

    def tamil(self):
        return 'ஐந்து'

    def telugu(self):
        return 'ఐదు'

    def turkish(self):
        return 'beş'

    def thai(self):
        return 'ห้า'

    def ukrainian(self):
        return 'п’ять'

    def welsh(self):
        return 'pump'
    # End of kinds of five in many languages.

    def morse_code(self):
        return '....-'

    def binary(self):
        return '101'

    def octal(self):
        return '5'

    def hex(self):
        return '5'

    def negative(self):
        return -5

    def loud(self, lang='englist'):
        """Speak loudly! FIVE! Use upper case!"""
        lang_method = getattr(self, lang, None)
        if lang_method:
            return lang_method().upper()
        else:
            return self.english().upper()

    def smooth(self):
        return 'S'

    def too_slow(self):
        time.sleep(0.555)
        return self.five()

    def map(self, seq):
        return map(self.five, seq)

    def reduce(self, seq):
        return reduce(self.five, seq)

    def fab(self):
        return ['Juwan Howard', 'Ray Jackson', 'Jimmy King', 'Jalen Rose',
                'Chris Webber']

    def jackson(self):
        return ['Jackie', 'Tito', 'Jermaine', 'Marlon', 'Michael']

    def rotate(self, word):
        """Replaced by a letter 5 right shift.
         e.g. a->f, b->g, . -> ."""
        lowercase_queue = deque(string.lowercase)
        lowercase_queue.rotate(-5)
        uppercase_queue = deque(string.uppercase)
        uppercase_queue.rotate(-5)
        lowercase_queue.extend(uppercase_queue)
        table = string.maketrans(string.letters,
                                 ''.join(list(lowercase_queue)))
        return word.translate(table)

    def oclock(self):
        return '🕔'

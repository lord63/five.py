#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, division

import math
import time
import string
from functools import reduce


class Five(object):
    # Start of "basic five'.
    def five(self, *args):
        return 5

    def pow(self, num):
        return math.pow(5, num)

    def sqrt(self):
        return math.sqrt(5)
    # End of "basic five".

    # Start of "math".
    def fibonacci(self):
        "The fifth num in the fibonacci sequence."
        return 5

    def factorial(self):
        "The factorial of five: 5!"
        return 120

    def factors(self):
        return [1, 5]

    def is_prime(self):
        return True
    # End of "math".

    def __call__(self):
        return self.five()

    # Start of "different sorts of five".
    def up_high(self):
        return '⁵'

    def down_low(self):
        return '₅'

    def too_slow(self):
        time.sleep(0.555)
        return self.five()

    def roman(self):
        return 'V'

    def morse_code(self):
        return '.....'

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

    def figlet(self):
        return ' _____\n| ____|\n| |__\n|___ \\\n ___) | \n|____/'

    def stars(self):
        return '*****'

    def bool(self):
        """Five should be true."""
        return True if 5 else False

    def elements(self):
        """The five basic elements on earth."""
        return ["Metal", "Wood", "Water", "Fire", "Earth"]

    def senses(self):
        """The five senses that provide data for perception."""
        return ["Sight", "Hearing", "Taste", "Smell", "Touch"]

    def circled(self):
        return '⑤'

    def flipside(self):
        """A five on the flipside should be upside down."""
        return 'ϛ'

    def lcd(self):
        return ' ---\n|\n --\n   |\n---'
    # End of "different sorts of five"

    # Start of "kinds of five in many languages",
    # sorted by alphabetic.
    def afrikaans(self):
        return 'vyf'

    def armenian(self):
        return 'հինգ'

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

    def canadian(self):
        return 'five eh'

    def catalan(self):
        return 'cinc'

    def chinese(self, case=None):
        if case == 'pinyin':
            return 'wǔ'
        elif case == 'financial':
            return '伍'
        else:
            return '五'

    def choctaw(self):
        return 'tahlapi'

    def croatian(self):
        return 'pet'

    def czech(self):
        return 'pět'

    def danish(self):
        return 'fem'

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

    def georgian(self):
        return 'ხუთი'

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

    def icelandic(self):
        return 'fimm'

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

    def lojban(self):
        return 'mu'

    def manx(self):
        return 'queig'

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

    def punjabi(self):
        return 'ਪੰਜ'

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

    def tagalog(self):
        return 'lima'

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

    def xhosa(self):
        return 'zintlanu'

    def urdu(self):
        return 'پانچ'

    def vietnamese(self):
        return 'năm'

    def welsh(self):
        return 'pump'
    # End of "kinds of five in many languages".

    # Start of "different radices of five".
    def binary(self):
        return '101'

    def octal(self):
        return '5'

    def hex(self):
        return '5'
    # End of "different radices of five".

    # Start of "map and reduce".
    def map(self, seq):
        return list(map(self.five, seq))

    def reduce(self, seq):
        return reduce(self.five, seq)
    # End of "map and reduce".

    # Start of "novelty five".
    def fab(self):
        return ['Juwan Howard', 'Ray Jackson', 'Jimmy King', 'Jalen Rose',
                'Chris Webber']

    def jackson(self):
        return ['Jackie', 'Tito', 'Jermaine', 'Marlon', 'Michael']

    def famous_five(self):
        """The Famous Five is the name of a series of children's
        adventure novels by English author Enid Blyton."""
        return ['Julian', 'Dick', 'Anne', 'George', 'Timmy']
    # End of "novelty five".

    def rotate(self, word):
        """Replaced by a letter 5 right shift.
         e.g. a->f, b->g, . -> ."""
        before = string.printable[:62]
        after = ''.join([i[5:] + i[:5] for i in [string.digits,
                                                 string.ascii_lowercase,
                                                 string.ascii_uppercase]])
        table = dict(zip(before, after))
        processed_word = [table[i] if i in before else i for i in word]
        return ''.join(processed_word)

    def oclock(self):
        return '🕔'

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, division

import math
import string
from unittest import TestCase

from five import Five
import pytest


class TestFive(TestCase):
    def setUp(self):
        self.five = Five()

    def test_basic_five(self):
        assert self.five() == 5
        assert self.five() != 6

    def test_operations_of_five(self):
        assert self.five() * self.five() == 25
        assert self.five() + self.five() == 10
        assert self.five() / self.five() == 1
        assert self.five() - self.five() == 0
        assert self.five() / self.five() * self.five() == self.five()
        assert self.five.pow(2) == 25
        assert self.five.sqrt() == math.sqrt(5)

    def test_math(self):
        assert self.five.fibonacci() == 5
        assert self.five.factorial() == 120
        assert self.five.factors() == [1, 5]
        assert self.five.is_prime() == True

    def test_different_sorts_of_five(self):
        assert self.five.up_high() == '⁵'
        assert self.five.down_low() == '₅'
        assert self.five.too_slow() == 5
        assert self.five.roman() == 'V'
        assert self.five.morse_code() == '.....'
        assert self.five.negative() == -5
        assert self.five.loud() == 'FIVE'
        assert self.five.loud('piglatin') == 'IVEFAY'
        assert self.five.smooth() == 'S'
        assert self.five.figlet() == (' _____\n| ____|\n| |__\n|___ '
                                      '\\\n ___) | \n|____/')
        assert self.five.stars() == '*****'
        assert self.five.bool() == True
        assert self.five.elements() == ["Metal", "Wood", "Water", "Fire",
                                        "Earth"]
        assert self.five.senses() == ["Sight", "Hearing", "Taste", "Smell",
                                      "Touch"]
        assert self.five.circled() == '⑤'
        assert self.five.flipside() == 'ϛ'
        assert self.five.lcd() == ' ---\n|\n --\n   |\n---'

    def test_multilingual_five(self):
        assert self.five.afrikaans() == 'vyf'
        assert self.five.armenian() == 'հինգ'
        assert self.five.arabic() == 'خمسة'
        assert self.five.azerbaijani() == 'beş'
        assert self.five.basque() == 'bost'
        assert self.five.belarusian() == 'пяць'
        assert self.five.bosnian() == 'pet'
        assert self.five.bulgarian() == 'пет'
        assert self.five.canadian() == 'five eh'
        assert self.five.catalan() == 'cinc'
        assert self.five.chinese() == '五'
        assert self.five.chinese('pinyin') == 'wǔ'
        assert self.five.chinese('financial') == '伍'
        assert self.five.choctaw() == 'tahlapi'
        assert self.five.croatian() == 'pet'
        assert self.five.czech() == 'pět'
        assert self.five.danish() == 'fem'
        assert self.five.dovah() == 'hen'
        assert self.five.dutch() == 'vijf'
        assert self.five.elvish() == 'lempe'
        assert self.five.english() == 'five'
        assert self.five.estonian() == 'viis'
        assert self.five.finnish() == 'viisi'
        assert self.five.french() == 'cinq'
        assert self.five.georgian() == 'ხუთი'
        assert self.five.german() == 'fünf'
        assert self.five.greek() == 'πέντε'
        assert self.five.hebrew() == 'חמש'
        assert self.five.hindi() == 'पांच'
        assert self.five.hungarian() == 'öt'
        assert self.five.icelandic() == 'fimm'
        assert self.five.indonesian() == 'lima'
        assert self.five.irish() == 'cúig'
        assert self.five.italian() == 'cinque'
        assert self.five.japanese() == '五'
        assert self.five.kannada() == 'ಐದು'
        assert self.five.klingon() == 'vagh'
        assert self.five.korean() == '오'
        assert self.five.latin() == 'quinque'
        assert self.five.latvian() == 'pieci'
        assert self.five.lithuanian() == 'penki'
        assert self.five.lojban() == 'mu'
        assert self.five.manx() == 'queig'
        assert self.five.mongolian() == 'таван'
        assert self.five.norwegian() == 'fem'
        assert self.five.persian() == 'پنج'
        assert self.five.piglatin() == 'ivefay'
        assert self.five.polish() == 'pięć'
        assert self.five.portuguese() == 'cinco'
        assert self.five.punjabi() == 'ਪੰਜ'
        assert self.five.romanian() == 'cinci'
        assert self.five.russian() == 'пять'
        assert self.five.serbian() == 'pet'
        assert self.five.slovakian() == 'päť'
        assert self.five.slovenian() == 'pet'
        assert self.five.spanish() == 'cinco'
        assert self.five.swedish() == 'fem'
        assert self.five.tagalog() == 'lima'
        assert self.five.tamil() == 'ஐந்து'
        assert self.five.telugu() == 'ఐదు'
        assert self.five.turkish() == 'beş'
        assert self.five.thai() == 'ห้า'
        assert self.five.xhosa() == 'zintlanu'
        assert self.five.ukrainian() == 'п’ять'
        assert self.five.urdu() == 'پانچ'
        assert self.five.vietnamese() == 'năm'
        assert self.five.welsh() == 'pump'

    def test_redix_of_five(self):
        assert self.five.binary() == '101'
        assert self.five.octal() == '5'
        assert self.five.hex() == '5'

    def test_map_and_reduce_of_five(self):
        assert self.five.map([1, 2, 3]) == [5, 5, 5]
        assert self.five.reduce([1, 2, 3]) == 5

    def test_novelty_five(self):
        assert self.five.jackson() == ['Jackie', 'Tito', 'Jermaine', 'Marlon',
                                       'Michael']
        assert self.five.fab() == ['Juwan Howard', 'Ray Jackson', 'Jimmy King',
                                   'Jalen Rose', 'Chris Webber']
        assert self.five.famous_five() == ['Julian', 'Dick', 'Anne', 'George',
                                           'Timmy']

    def test_rotation_of_five(self):
        assert self.five.rotate(string.digits) == '5678901234'
        assert self.five.rotate(string.ascii_lowercase) == (
            'fghijklmnopqrstuvwxyzabcde')
        assert self.five.rotate(string.ascii_uppercase) == (
            'FGHIJKLMNOPQRSTUVWXYZABCDE')
        assert self.five.rotate('$_$ -,- @.@?') == '$_$ -,- @.@?'

    def test_unicode_of_five(self):
        assert self.five.oclock() == '🕔'

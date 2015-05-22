#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, division

import string

from five.five import Five
import pytest


def test_five():
    five = Five()

    assert five() == 5
    assert five() != 6
    assert five() * five() == 25
    assert five() + five() == 10
    assert five() / five() == 1
    assert five() - five() == 0
    assert five() / five() * five() == five()

    assert five.up_high() == '⁵'
    assert five.down_low() == '₅'
    assert five.roman() == 'V'

    assert five.arabic() == 'خمسة'
    assert five.azerbaijani() == 'beş'
    assert five.basque() == 'bost'
    assert five.belarusian() == 'пяць'
    assert five.bosnian() == 'pet'
    assert five.bulgarian() == 'пет'
    assert five.catalan() == 'cinc'
    assert five.chinese() == '五'
    assert five.choctaw() == 'tahlapi'
    assert five.croatian() == 'pet'
    assert five.czech() == 'pět'
    assert five.dovah() == 'hen'
    assert five.dutch() == 'vijf'
    assert five.elvish() == 'lempe'
    assert five.english() == 'five'
    assert five.estonian() == 'viis'
    assert five.finnish() == 'viisi'
    assert five.french() == 'cinq'
    assert five.german() == 'fünf'
    assert five.greek() == 'πέντε'
    assert five.hebrew() == 'חמש'
    assert five.hindi() == 'पांच'
    assert five.hungarian() == 'öt'
    assert five.indonesian() == 'lima'
    assert five.irish() == 'cúig'
    assert five.italian() == 'cinque'
    assert five.japanese() == '五'
    assert five.kannada() == 'ಐದು'
    assert five.klingon() == 'vagh'
    assert five.korean() == '오'
    assert five.latin() == 'quinque'
    assert five.latvian() == 'pieci'
    assert five.lithuanian() == 'penki'
    assert five.mongolian() == 'таван'
    assert five.norwegian() == 'fem'
    assert five.persian() == 'پنج'
    assert five.piglatin() == 'ivefay'
    assert five.polish() == 'pięć'
    assert five.portuguese() == 'cinco'
    assert five.romanian() == 'cinci'
    assert five.russian() == 'пять'
    assert five.serbian() == 'pet'
    assert five.slovakian() == 'päť'
    assert five.slovenian() == 'pet'
    assert five.spanish() == 'cinco'
    assert five.swedish() == 'fem'
    assert five.tamil() == 'ஐந்து'
    assert five.telugu() == 'ఐదు'
    assert five.turkish() == 'beş'
    assert five.thai() == 'ห้า'
    assert five.ukrainian() == 'п’ять'
    assert five.welsh() == 'pump'

    assert five.morse_code() == '....-'
    assert five.binary() == '101'
    assert five.octal() == '5'
    assert five.hex() == '5'

    assert five.negative() == -5
    assert five.loud() == 'FIVE'
    assert five.loud('piglatin') == 'IVEFAY'
    assert five.smooth() == 'S'
    assert five.too_slow() == 5

    assert five.map([1, 2, 3]) == [5, 5, 5]
    assert five.reduce([1, 2, 3]) == 5

    assert five.jackson() == ['Jackie', 'Tito', 'Jermaine', 'Marlon',
                              'Michael']
    assert five.fab() == ['Juwan Howard', 'Ray Jackson', 'Jimmy King',
                          'Jalen Rose', 'Chris Webber']

    assert five.rotate(string.digits) == '5678901234'
    assert five.rotate(string.lowercase) == ('fghijklmnopqrstuvwxyzabcde')
    assert five.rotate(string.uppercase) == ('FGHIJKLMNOPQRSTUVWXYZABCDE')
    assert five.rotate('$_$ -,- @.@?') == '$_$ -,- @.@?'

    assert five.oclock() == '🕔'

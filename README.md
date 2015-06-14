# Five.py

[![Latest Version][1]][2]
[![Build Status][3]][4]
[![Coverage Status][5]][6]

A library to overcomplicate 5. It's a python port of the javascript [five][].


## Install

    $ pip install five


## Usage

```python
from five import Five
five = Five()
```

### Basic 5
```python
five()  # 5
five() + five()  # 10
five() * five()  # 25
five() / five()  # 1
five() - five()  # 0
five.pow(3)      # 125
five.sqrt()      # 2.23606797749979
```

### Counting is simple
```python
five() + five()  # 10
five() + five() - five() / five()  # 9
five() + (five() + five() + five()) / five()  # 8
five() + (five() + five()) / five()  # 7
five() + five() / five()  # 6
five()  # 5
five() - five() / five()  # 4
five() - (five() + five()) / five()  # 3
(five() + five()) / five()  # 2
five() / five()  # 1
```

### Math
```python
five.fibonacci()  # 5
five.factorial()  # 120
five.factors()  # [1, 5]
five.is_prime()  # True
```

### Different sorts of 5
```python
five.up_high()  # ⁵
five.down_low()  # ₅
five.too_slow()  # 5, with a 555-millisecond delay
five.roman()  # V
five.morse_code()  # .....(di-di-di-di-di)
five.negative()  # -5
five.loud()  # FIVE
five.loud('piglatin')  # IVEFAY
five.smooth()  # S
five.figlet()  #   _____
                  | ____|
                  | |__
                  |___ \
                   ___) |
                  |____/
five.stars()  # *****
five.bool()   # True
five.elements()  # ["Metal", "Wood", "Water", "Fire", "Earth"]
five.senses()  # ["Sight", "Hearing", "Taste", "Smell", "Touch"]
five.circled()  # ⑤
five.flipside()  # ϛ
five.lcd()  #  ---
              |
               --
                 |
              ---
```

### 5 goes multilingual
```python
five.afrikaans()  # vyf
five.armenian()  # հինգ
five.arabic()  # خمسة
five.azerbaijani()  # beş
five.basque()  # bost
five.belarusian  # пяць
five.bosnian()  # pet
five.bulgarian()  # пет
five.canadian()  # five eh
five.catalan()  # cinc
five.chinese()  # 五
five.chinese('pinyin')  # 'wǔ'
five.chinese('financial')  # '伍'
five.choctaw()  # tahlapi
five.croatian()  # pet
five.czech()  # pět
five.danish()  # fem
five.dovah()  # hen
five.dutch()  # vijf
five.elvish()  # lempe
five.english()  # Five
five.estonian()  # viis
five.finnish()  # viisi
five.french()  # cinq
five.georgian()  # ხუთი
five.german()  # fünf
five.greek()  # πέντε
five.hebrew()  # חמש
five.hindi()  # पांच
five.hungarian()  # öt
five.icelandic()  # fimm
five.indonesian()  # lima
five.irish()  # cúig
five.italian()  # cinque
five.japanese()  # 五
five.kannada()  # ಐದು
five.klingon()  # vagh
five.korean()  # 오
five.latin()  # quinque
five.latvian()  # pieci
five.lithuanian()  # penki
five.lojban()  # mu
five.manx()  # queig
five.mongolian()  # таван
five.norwegian()  # fem
five.persian()  # پنج
five.piglatin()  # ivefay
five.polish()  # pięć
five.portuguese()  # cinco
five.punjabi()  # ਪੰਜ
five.romanian()  # cinci
five.russian()  # пять
five.serbian()  # pet
five.slovakian()  # päť
five.slovenian()  # pet
five.spanish()  # cinco
five.swedish()  # fem
five.tagalog()  # lima
five.tamil()  # ஐந்து
five.telugu()  # ఐదు
five.thai()  # ห้า
five.turkish()  # beş
five.xhosa()  # zintlanu
five.ukrainian()  # п’ять
five.urdu()  # پانچ
five.vietnamese()  # năm
five.welsh()  # pump
```

### Different radices
```python
five.binary()  # 101
five.octal()  # 5
five.hex()  # 5
```

### Map and Reduce
```python
five.map([1, 2, 3])  # [5, 5, 5]
five.reduce([1, 2, 3])  # 5
```

### Novelty
```python
five.fab()  # ['Juwan Howard','Ray Jackson','Jimmy King','Jalen Rose','Chris Webber']
five.jackson()  # ['Jackie','Tito','Jermaine','Marlon','Michael']
five.famous_five()  # ['Julian', 'Dick', 'Anne', 'George', 'Timmy']
```

### Rotation
```python
five.rotate("five.py")  #knaj.ud
```

### Unicode
```python
five.oclock()  # '🕔'
```

## Development

run the tests:

    $ pip install -r dev-requirements.txt
    $ make test

## Credits

All the glories should belong to [@jackdcrawford][], I just port it to python :)

## License

MIT.

[1]: http://img.shields.io/pypi/v/five.svg
[2]: https://pypi.python.org/pypi/five
[3]: https://travis-ci.org/lord63/five.py.svg
[4]: https://travis-ci.org/lord63/five.py
[5]: https://coveralls.io/repos/lord63/five.py/badge.svg
[6]: https://coveralls.io/r/lord63/five.py
[five]: https://github.com/jackdcrawford/five
[@jackdcrawford]: https://github.com/jackdcrawford

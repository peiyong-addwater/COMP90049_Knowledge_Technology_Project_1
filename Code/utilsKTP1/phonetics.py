"""
Modified from https://github.com/Lilykos/pyphonetics, with numba acceleration
"""

import re
from itertools import groupby

import numba
from unidecode import unidecode

from .exceptions import UnicodeException
from .exceptions import WrongLengthException


def translation(first, second):
    """Create an index of mapped letters (zip to dict)."""
    if len(first) != len(second):
        raise WrongLengthException('The lists are not of the same length!')
    return dict(zip(first, second))


def squeeze(word):
    """Squeeze the given sequence by dropping consecutive duplicates."""
    return ''.join(x[0] for x in groupby(word))


class Metaphone:
    """
    The metaphone algorithm.
    [Reference]: https://en.wikipedia.org/wiki/Metaphone
    [Author]: Lawrence Philips, 1990
    """

    def __init__(self):
        super().__init__()

        self.rules = [
            (r'[^a-z]', r''),
            (r'([bcdfhjklmnpqrstvwxyz])\1+', r'\1'),
            (r'^ae', r'E'),
            (r'^[gkp]n', r'N'),
            (r'^wr', r'R'),
            (r'^x', r'S'),
            (r'^wh', r'W'),
            (r'mb$', r'M'),
            (r'(?!^)sch', r'SK'),
            (r'th', r'0'),
            (r't?ch|sh', r'X'),
            (r'c(?=ia)', r'X'),
            (r'[st](?=i[ao])', r'X'),
            (r's?c(?=[iey])', r'S'),
            (r'[cq]', r'K'),
            (r'dg(?=[iey])', r'J'),
            (r'd', r'T'),
            (r'g(?=h[^aeiou])', r''),
            (r'gn(ed)?', r'N'),
            (r'([^g]|^)g(?=[iey])', r'\1J'),
            (r'g+', r'K'),
            (r'ph', r'F'),
            (r'([aeiou])h(?=\b|[^aeiou])', r'\1'),
            (r'[wy](?![aeiou])', r''),
            (r'z', r'S'),
            (r'v', r'F'),
            (r'(?!^)[aeiou]+', r'')
        ]

    @numba.jit()
    def phonetics(self, word):
        if not isinstance(word, str):
            raise UnicodeException('Expected a unicode string!')

        code = unidecode(word).lower()
        for item in self.rules:
            code = re.sub(item[0], item[1], code)
        return code.upper()


class MatchingRatingApproach:
    """
    Functions related to the computation of the Match Rating Approach codex.
    [Reference]: https://en.wikipedia.org/wiki/Match_rating_approach
    [Article]: Moore, G B.; Kuhns, J L.; Treffzs, J L.; Montgomery, C A. (Feb 1, 1977).
        Accessing Individual Records from Personal Data Files Using Nonunique Identifiers.
        US National Institute of Standards and Technology. p. 17. NIST SP - 500-2.
    """

    def __init__(self):
        super().__init__()

    @numba.jit()
    def phonetics(self, word):
        if not isinstance(word, str):
            raise UnicodeException('Expected a unicode string!')

        codex = unidecode(word).upper()
        codex = re.sub(r'[^A-Z]', r'', codex)

        # Dropping non - leading vowels
        codex = codex[0] + re.sub(r'[AEIOU]', r'', codex[1:])

        # Dropping consecutive consonants
        codex = squeeze(codex)

        # Returning the codex
        offset = min(3, len(codex) - 3)
        return codex[:3] + codex[len(codex) - offset:offset + len(codex)]


class RefinedSoundex:
    """
    The Refined Soundex algorithm.
    [Reference]: https://en.wikipedia.org/wiki/Soundex
    [Authors]: Robert C. Russel, Margaret King Odell
    """

    def __init__(self):
        super().__init__()

        self.translations = translation(
            'AEIOUYWHBPFVCKSGJQXZDTLMNR',
            '000000DD112233344555667889'
        )

    @numba.jit()
    def phonetics(self, word):
        if not isinstance(word, str):
            raise UnicodeException('Expected a unicode string!')

        word = unidecode(word).upper()
        word = re.sub(r'[^A-Z]', r'', word)

        first_letter = word[0]
        tail = ''.join(self.translations[char] for char in word
                       if self.translations[char] != 'D')

        return first_letter + squeeze(tail)


class Soundex:
    """
    The Soundex algorithm.
    [Reference]: https://en.wikipedia.org/wiki/Soundex
    [Authors]: Robert C. Russel, Margaret King Odell
    """

    def __init__(self):
        super().__init__()

        self.translations = translation(
            'AEIOUYWHBPFVCSKGJQXZDTLMNR',
            '000000DD111122222222334556'
        )
        self.pad = lambda code: '{}0000'.format(code)[:4]

    @numba.jit()
    def phonetics(self, word):
        if not isinstance(word, str):
            raise UnicodeException('Expected a unicode string!')

        word = unidecode(word).upper()
        word = re.sub(r'[^A-Z]', r'', word)

        first_letter = word[0]
        tail = ''.join(self.translations[char] for char in word
                       if self.translations[char] != 'D')

        # Dropping first code's letter if duplicate
        if tail[0] == self.translations[first_letter]:
            tail = tail[1:]

        code = squeeze(tail).replace('0', '')
        return self.pad(first_letter + code)


class FuzzySoundex:
    """
    Implementation of the "Fuzzy Soundex" algorithm.
    [Reference]: http://wayback.archive.org/web/20100629121128/http://www.ir.iit.edu/publications/downloads
    /IEEESoundexV5.pdf
    [Article]: Holmes, David and M. Catherine McCabe. "Improving Precision and Recall for Soundex Retrieval."
    """

    def __init__(self):
        super().__init__()

        self.translations = translation(
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            '0193017-07745501769301-7-9'
        )

        self.rules = [
            (r'CA', r'KA'),
            (r'CC', r'KK'),
            (r'CK', r'KK'),
            (r'CE', r'SE'),
            (r'CHL', r'KL'),
            (r'CL', r'KL'),
            (r'CHR', r'KR'),
            (r'CR', r'KR'),
            (r'CI', r'SI'),
            (r'CO', r'KO'),
            (r'CU', r'KU'),
            (r'CY', r'SY'),
            (r'DG', r'GG'),
            (r'GH', r'HH'),
            (r'MAC', r'MK'),
            (r'MC', r'MK'),
            (r'NST', r'NSS'),
            (r'PF', r'FF'),
            (r'PH', r'FF'),
            (r'SCH', r'SSS'),
            (r'TIO', r'SIO'),
            (r'TIA', r'SIO'),
            (r'TCH', r'CHH'),
        ]

        self.set1 = ['CS', 'CZ', 'TS', 'TZ']
        self.set2 = ['HR', 'WR']
        self.set3 = ['KN', 'NG']
        self.set4 = 'HWY'

    @numba.jit()
    def phonetics(self, word):
        if not isinstance(word, str):
            raise UnicodeException('Expected a unicode string!')

        if not word:
            return ''

        word = unidecode(word).upper()

        # Substitutions for beginnings
        first_two, rest = word[:2], word[2:]

        if first_two in self.set1:
            word = 'SS' + rest
        elif first_two == 'GN':
            word = 'NN' + rest
        elif first_two in self.set2:
            word = 'RR' + rest
        elif first_two == 'HW':
            word = 'WW' + rest
        elif first_two in self.set3:
            word = 'NN' + rest

        # Substitutions for endings
        last_two, initial = word[-2:], word[0:-2]

        if last_two == 'CH':
            word = initial + 'KK'
        elif last_two == 'NT':
            word = initial + 'TT'
        elif last_two == 'RT':
            word = initial + 'RR'
        elif word[-3:] == 'RDT':
            word = word[0:-3] + 'RR'

        # Applying the rules
        for rule in self.rules:
            word = re.sub(rule[0], rule[1], word)

        # Catch the first letter
        first_letter = word[0]

        # Translating
        code = ''.join(self.translations.get(char, char) for char in word)

        # Removing hyphens
        code = code.replace('-', '')

        # Squeezing the code
        code = squeeze(code)

        # Dealing with initials
        code = first_letter if code[0] in self.set4 \
            else first_letter + code[1:]

        # Dropping vowels
        code = code.replace('0', '')
        return code

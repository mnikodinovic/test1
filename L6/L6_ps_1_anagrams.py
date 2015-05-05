__author__ = 'miroslav'

# -----------------
# User Instructions
#
# This homework deals with anagrams. An anagram is a rearrangement
# of the letters in a word to form one or more new words.
#
# Your job is to write a function anagrams(), which takes as input
# a phrase and an optional argument, shortest, which is an integer
# that specifies the shortest acceptable word. Your function should
# return a set of all the possible combinations of anagrams.
#
# Your function should not return every permutation of a multi word
# anagram: only the permutation where the words are in alphabetical
# order. For example, for the input string 'ANAGRAMS' the set that
# your function returns should include 'AN ARM SAG', but should NOT
# include 'ARM SAG AN', or 'SAG AN ARM', etc...

def anagrams(phrase, shortest=2):
    """Return a set of phrases with words from WORDS that form anagram
    of phrase. Spaces can be anywhere in phrase or anagram. All words
    have length >= shortest. Phrases in answer must have words in
    lexicographic order (not all permutations)."""
    # your code here

    # phrase = phrase.replace(' ', '')
    prefix = ''
    results = set()

    def find_anagrams(remainder, prefix, shortest=2):

        # print 'prefiks', prefix, 'remainder', remainder
        words = find_words(remainder)
        # print 'rijeci:', words

        if words:
            for word in words:
                print 'r', word

                if len(prefix) > 0:
                    prefix = prefix + ' ' + word
                else:
                    prefix = word

                remainder = removed(remainder, prefix)
                if word == 'DOCTOR':
                    print 'prefiks', prefix, 'remainder', remainder

                if len(prefix.replace(' ', '')) == len(phrase.replace(' ', '')) + 1:
                    # print 'prefiks koji dodajemo je', prefix
                    results.add(prefix)

                if remainder: find_anagrams(remainder, prefix)

        # print
        return 1

    find_anagrams(phrase, prefix)
    return results


# ------------
# Helpful functions
#
# You may find the following functions useful. These functions
# are identical to those we defined in lecture.

def removed(letters, remove):
    "Return a str of letters, but with each letter in remove removed once."
    for L in remove:
        letters = letters.replace(L, '', 1)
    return letters


def find_words(letters):
    return extend_prefix('', letters, set())


def extend_prefix(pre, letters, results):
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            extend_prefix(pre + L, letters.replace(L, '', 1), results)
    return results


def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]


def readwordlist(filename):
    "Return a pair of sets: all the words in a file, and all the prefixes. (Uppercased.)"
    wordset = set(open(filename).read().upper().split())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset


WORDS, PREFIXES = readwordlist('words4k.txt')

# ------------
# Testing
#
# Run the function test() to see if your function behaves as expected.

def test():
    assert 'DOCTOR WHO' in anagrams('TORCHWOOD')
    assert 'BOOK SEC TRY' in anagrams('OCTOBER SKY')
    assert 'SEE THEY' in anagrams('THE EYES')
    assert 'LIVES' in anagrams('ELVIS')
    assert anagrams('PYTHONIC') == set([
        'NTH PIC YO', 'NTH OY PIC', 'ON PIC THY', 'NO PIC THY', 'COY IN PHT',
        'ICY NO PHT', 'ICY ON PHT', 'ICY NTH OP', 'COP IN THY', 'HYP ON TIC',
        'CON PI THY', 'HYP NO TIC', 'COY NTH PI', 'CON HYP IT', 'COT HYP IN',
        'CON HYP TI'])
    return 'tests pass'

# print test()
# for (score, (i, j), (di, dj), word) in find_words('DOCTOR WHO'):
# print word
# print find_words('DOCTOR WHO')
# print removed('DOCTOR WHO', 'COT  ')
print anagrams('TORCHWOOD')
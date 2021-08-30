"""
import re, collections
from collections import defaultdict
not_word_pattern = "[^\'a-zA-Z0-9\"]+"

def count_words(sentence):
    words = defaultdict(int)
    splitted_words = [i.strip("\'") for i in re.split(not_word_pattern, sentence.lower()) if i != '']
    
    for word in splitted_words:
        words[word] += 1
    return dict(words)



Great for passing the test.

> Do you want to rewrite using re.findall() , use regex to extract the word?
> Nice works.

> You may use defaultdict to simplify further. [My solution as reference](https://exercism.io/my/solutions/f1f354c2007b4a998fac95f0d38cc6b1)

"""
from collections import defaultdict

bound_word = r"\b[\w']+\b"
def count_words_bound(sentence):
    words = defaultdict(int)
    for word in re.findall(bound_word, sentence):
        words[word] += 1
    return dict(words)

"""
import re, collections
def count_words(sentence):
    word_regex = re.compile(
        r"""
                [0-9]+              # A number...
            |   [a-z]+ ' [a-z]+     # or a word with an apostrophe...
            |   [a-z]+              # or a word without an apostrophe.
        """,
        re.VERBOSE
    )
    return collections.Counter(word_regex.findall(sentence.lower()))
"""
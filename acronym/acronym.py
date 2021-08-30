import re
def abbreviate(words):
    return "".join( w[0] for w in re.split(r'[\s,_-]+', words.upper()) )

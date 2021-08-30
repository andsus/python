def is_isogram(string):
    iso_map = dict()
    for c in string.lower():
        if c.isalpha():
            if c in iso_map:
                return False
            iso_map[c] = True
    return True

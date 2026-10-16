def word_frequency(words):
    result = {}
    for word in words:
        key = word.lower()
        result[key] = result.get(key, 0) + 1
    return result

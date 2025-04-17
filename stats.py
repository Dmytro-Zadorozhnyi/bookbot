def get_words_count(text):
    return len(text.split())

def count_words(data):
    results = {}
    for word in data.split():
        if word.lower() in results:
            results[word.lower()] += 1
        else:
            results[word.lower()] = 1
    return results

def count_characters(data):
    results = {}
    for char in data:
        if char.lower() in results:
            results[char.lower()] += 1
        else:
            results[char.lower()] = 1
    return results

def sort_char(dict):
    return dict["count"]
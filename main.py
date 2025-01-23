def main():
    filepath = "books/frankenstein.txt"
    print_report(filepath)

def read_file(filepath):
    with open(filepath) as f:
        data = f.read()
    return data

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

def print_report(filepath):
    data = read_file(filepath)
    print(f"--- Begin report of {filepath} ---")
    print(f"{get_words_count(data)} words found in the document")
    print()

    char_list = [{"char": k, "count": v} for k,v in count_characters(data).items() if k.isalpha()]
    char_list.sort(reverse=True, key=sort_char)
    
    for line in char_list:
        print(f"The '{line["char"]}' character was found {line["count"]} times")


    print("--- End report ---")
    #for character, val in 
main()
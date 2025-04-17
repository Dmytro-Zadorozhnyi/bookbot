from stats import *
import sys
def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print_report(filepath)

def read_file(filepath):
    with open(filepath) as f:
        data = f.read()
    return data

def print_report(filepath):
    data = read_file(filepath)
    print(f"--- Begin report of {filepath} ---")
    print(f"{get_words_count(data)} words found in the document")
    print()

    char_list = [{"char": k, "count": v} for k,v in count_characters(data).items() if k.isalpha()]
    char_list.sort(reverse=True, key=sort_char)
    
    for line in char_list:
        print(f"'{line["char"]}: {line["count"]}'")


    print("--- End report ---")
    #for character, val in 
main()
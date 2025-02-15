from collections import Counter

def main():
    file_path = "/home/zakarias/workspace/github.com/ZakariasFagerstedt/bookbot/books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
    char_counts = count_characters(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(char_counts)
    
    print(f"--- Begin report of {file_path} ---")
    print("There are ", count_words(file_contents) , " words in this book!")
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The {item["char"]} character was found {item["num"]} times")
    
    print("end of report")


def count_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    character_counts = Counter(text)
    return dict(character_counts)

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
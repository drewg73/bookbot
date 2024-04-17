def main():
    file_path = "books/frankenstein.txt"
    text = get_file_text(file_path)
    num_words = word_count(text)
    chars_dict = get_chars_dict(text)
    sorted_chars_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_chars_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
     

def word_count(text):
    words = text.split()
    return len(words)

def sort_on(dict):
     return dict["num"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
             chars[lowered] += 1
        else:
             chars[lowered] = 1
    return chars

def get_file_text(path):
     with open(path) as f:
        return f.read()

main()


        

def count_words(user_string):
    words = user_string.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def count_chars(user_string):
    num_characters = {}
    words = user_string.lower().split()
    for word in words:
        for char in word:
            if char.isalpha():
                if char in num_characters:
                    num_characters[char] += 1
                else:
                    num_characters[char] = 1
    return num_characters

def sort_on(dict):
    return dict["num"]

def list_dict(dict):
    new_list = []
    for key in dict:
        new_list.append({"char": key, "num": dict[key]})
    return new_list

def print_report(user_string):
    print("--- Begin report of books/frankenstein.txt ---")

    num_words = count_words(user_string)
    print(f"{num_words} words found in the document\n")
    
    chars_dict = count_chars(user_string)
    new_dict = list_dict(chars_dict)
    new_dict.sort(reverse = True, key=sort_on)
    
    for dict in new_dict:
        print(f"The {dict["char"]} character was found {dict["num"]} times")
    print()

    print("--- End report ---")

def main():
    path_to_book = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_book)
    print_report(file_contents)
main()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    for char in text.lower():
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def sort_on(dict):
    return dict["count"]

def chars_dict_to_sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "count": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    print(f"Word count: {word_count}")
    char_count = count_chars(file_contents)
    char_sorted_list = chars_dict_to_sorted_list(char_count)
    print(char_sorted_list)

main()
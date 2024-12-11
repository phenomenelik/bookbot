def main():
    file_path = "books/frankenstein.txt"
    words = get_text_from_file(file_path)
    num_words = count_words(words)
    num_char = count_characters(words)
    converted_num_char = convert_dict_to_list(num_char)
    converted_num_char.sort(reverse=True, key=sort_on)
    generate_a_report(file_path=file_path, num_words=num_words, converted_num_char=converted_num_char)


def get_text_from_file(file: str):
    with open(file) as f:
        return f.read()


def count_words(text: str):
    return len(text.split())


def count_characters(text: str):
    char_count = {}
    for char in text:
        char_lowered = char.lower()
        if char_lowered.isalpha():
            if char_lowered in char_count:
                char_count[char_lowered] += 1
            else: char_count[char_lowered] = 1
    return char_count


def convert_dict_to_list(dict):
    converted_list = []
    for k in dict:
        to_append = {"letter": k, "count": dict[k]}
        converted_list.append(to_append)
    return converted_list


def sort_on(dict):
    return dict["count"]


def generate_a_report(file_path, num_words, converted_num_char):
    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for item in converted_num_char:
        letter = item["letter"]
        count = item["count"]
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")


main()

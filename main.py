print("hello world")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lower_case_file_contents = file_contents.lower()
        letters_list = lower_case_file_contents.split()

        print(file_contents)

        letter_dict = {}
        for letter in lower_case_file_contents:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1 

    print(f"{len(letters_list)} words found in the document") 

    for letter in letter_dict:
        if letter.isalpha():
            print(f"The '{letter}' character was found {letter_dict[letter]} times")

main()

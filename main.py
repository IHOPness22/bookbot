 

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()

        characters = file_contents.lower()
        char_counts = {}
        
        for char in characters:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        
        char_counts_list = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
                   
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document")
        for char, count in char_counts_list:
            if char.isalpha():
                print(f"The '{char}' character was found {count} times")


if __name__ == '__main__':
    main()
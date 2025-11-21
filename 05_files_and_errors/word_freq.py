def count_word_frequencies(filename):
    """
    Read text file and return dictionary mapping each word to frequency.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}
    
    # Normalize: lowercase everything
    text = text.lower()

    # Replace punctuation with spaces
    for char in ",.!?;:\"'()[]{}":
        text = text.replace(char, " ")

    # Split text into words
    words = text.split()

    # Count frequencies
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies

def main():
    filename = input("Enter the filename to process: ")

    frequencies = count_word_frequencies(filename)

    if frequencies:
        print("\nWord Frequencies:")
        for word, count in sorted(frequencies.items()):
            print(f"{word}: {count}")

if __name__ == "__main__":
    main()
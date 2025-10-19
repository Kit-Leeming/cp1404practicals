"""
Word Occurrences
Estimated time: 15 mins
Actual time:    19 mins
"""


def main():
    text = str(input("Text: ")).lower()
    words = sorted(text.split())
    word_to_count = {}
    for word in words:
        cleaned_word = word.strip(".,()!?")
        # If word exists in dictionary return count, if not return 0
        word_to_count[cleaned_word] = word_to_count.get(cleaned_word, 0) + 1

    max_word_length = max(len(key) for key in word_to_count)

    for word, count in word_to_count.items():
        print(f"{word:<{max_word_length}} : {count}")


main()

from typing import Dict, List


def book_open(path: str) -> str:
    with open(path) as f:
        return f.read()


def count_chars(text: List[str]) -> Dict[str, int]:
    chars = {}
    for c in text.lower():
        if c not in chars:
            chars[c] = 0
        chars[c] += 1
    return chars


def sort_letters(chars: Dict[str, int]):
    letters = [] * 26
    for k in chars:
        if k.isalpha():
            letters.append([k, chars[k]])

    return sorted(letters, key=lambda x: x[1], reverse=True)


def report(filepath: str, words: List[str], chars: Dict[str, int]):
    print(f"*** Begin report of {filepath} ***")
    print()
    print(f"There were {len(words)} words found in the document.")
    print()
    print("Letter  |  Frequency")
    print("-------------------------")

    letters = sort_letters(chars)
    for x in letters:
        print(f"   {x[0]}    |    {x[1]}")
    return


def main():
    path = "./books/frankenstein.txt"
    text = book_open(path)
    words = text.split()
    print(f"\nwords in {path}: {len(words)}")

    chars = count_chars(text)
    print(f"\ncharacters in {path}:\n{chars}")
    print()

    report(path, words, chars)
    print()


main()

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


def gen_report(filepath: str, words: List[str], chars: Dict[str, int]) -> List[str]:
    output = []
    output.append(f"*** Begin report of {filepath} ***")
    output.append("")
    output.append(f"There were {len(words)} words found in the document.")
    output.append("")
    output.append("Letter  |  Frequency")
    output.append("-------------------------")

    letters = sort_letters(chars)
    for x in letters:
        output.append(f"   {x[0]}    |    {x[1]}")

    return output


def write_report(filename: str, report: List[str]):
    try:
        f = open(filename, "x", encoding="utf-8")
    except OSError:
        f = open(filename, "w", encoding="utf-8")

    for line in report:
        print(line, file=f)


def main():
    path = "./books/frankenstein.txt"
    text = book_open(path)
    words = text.split()
    print(f"\nwords in {path}: {len(words)}")

    chars = count_chars(text)
    print(f"\ncharacters in {path}:\n{chars}")
    print()

    franken_report = gen_report(path, words, chars)
    for line in franken_report:
        print(line)
    print()

    output = "./reports/report.txt"
    write_report(output, franken_report)


main()

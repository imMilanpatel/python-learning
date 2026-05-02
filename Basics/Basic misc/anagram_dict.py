"""Anagram dictionary analyzer for LabVIEW.

Reads a list of words from a dictionary file and separates them into:
- words_with_anagrams: words that have at least one anagram in the dictionary
- words_without_anagrams: words with no anagrams in the dictionary

The script prints JSON on stdout so LabVIEW can parse the result.

Contributor(s):
- Milan Patel -- 05/2026

"""

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


def read_words_from_file(path: Path) -> List[str]:
    """Read one word per line from a file and normalize them."""
    words: List[str] = []
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            word = line.strip()
            if word:
                words.append(word)
    return words


def normalized_key(word: str) -> str:
    """Return a normalized key for anagram comparison."""
    return ''.join(sorted(word.replace(' ', '').lower()))


def find_anagram_groups(words: Iterable[str]) -> Dict[str, List[str]]:
    """Group words by their sorted normalized letters."""
    groups: Dict[str, List[str]] = defaultdict(list)
    for word in words:
        groups[normalized_key(word)].append(word)
    return groups


def split_words_by_anagram_presence(words: Iterable[str]) -> Tuple[List[str], List[str]]:
    """Return (words_with_anagrams, words_without_anagrams)."""
    groups = find_anagram_groups(words)
    with_anagrams: List[str] = []
    without_anagrams: List[str] = []

    for word in words:
        key = normalized_key(word)
        if len(groups[key]) > 1:
            with_anagrams.append(word)
        else:
            without_anagrams.append(word)

    with_anagrams.sort(key=str.lower)
    without_anagrams.sort(key=str.lower)
    return with_anagrams, without_anagrams


def build_output_data(words: Iterable[str]) -> Dict[str, List[str]]:
    """Build the final JSON serializable output structure."""
    with_anagrams, without_anagrams = split_words_by_anagram_presence(words)
    return {
        "words_with_anagrams": with_anagrams,
        "words_without_anagrams": without_anagrams,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze a dictionary file for anagrams and split words into two fields."
    )
    parser.add_argument(
        "dictionary",
        type=Path,
        help="Path to the dictionary file containing one word per line.",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=None,
        help="Optional path to save JSON output instead of printing it.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    words = read_words_from_file(args.dictionary)
    result = build_output_data(words)
    serialized = json.dumps(result, indent=2, ensure_ascii=False)

    if args.output_json:
        args.output_json.write_text(serialized, encoding="utf-8")
        print(f"Saved output to {args.output_json}")
    else:
        print(serialized)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

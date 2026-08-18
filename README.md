# leetcode-string-11

11 classic LeetCode string problems solved in Python. Each solution is a standalone file with a `Solution` class, ready to paste into LeetCode or run locally.

## Problems

| # | Problem | File | Difficulty | Approach |
|---|---------|------|------------|----------|
| 771 | Jewels and Stones | [jewels_and_stones.py](jewels_and_stones.py) | Easy | Set membership lookup |
| 344 | Reverse String | [reverse_string.py](reverse_string.py) | Easy | Two pointers, in-place swap |
| 1768 | Merge Strings Alternately | [merge_strings_alternately.py](merge_strings_alternately.py) | Easy | Two pointers + leftover slices |
| 412 | Fizz Buzz | [fizz_buzz.py](fizz_buzz.py) | Easy | Modulo branching |
| 242 | Valid Anagram | [valid_anagram.py](valid_anagram.py) | Easy | Frequency counting (dict) |
| 345 | Reverse Vowels of a String | [reverse_vowels_of_a_string.py](reverse_vowels_of_a_string.py) | Easy | Collect vowels, reverse, rebuild |
| 125 | Valid Palindrome | [valid_palindrome.py](valid_palindrome.py) | Easy | Two pointers, skip non-alnum |
| 459 | Repeated Substring Pattern | [repeated_substring_pattern.py](repeated_substring_pattern.py) | Easy | Double string trick |
| 205 | Isomorphic Strings | [isomorphic_strings.py](isomorphic_strings.py) | Easy | Two-way char mapping |
| 392 | Is Subsequence | [is_subsequence.py](is_subsequence.py) | Easy | Two indices, greedy scan |
| 796 | Rotate String | [rotate_string.py](rotate_string.py) | Easy | `goal in s + s` |

## When frequency counting beats sorting

Sorting two strings is O(n log n) in time, whereas counting character frequencies with a dictionary (or array) is O(n) — strictly faster for large inputs, and it avoids materializing sorted copies of the strings, which costs extra O(n) space as well. Frequency counting is the right tool whenever you care only about the *multiset* of characters (anagrams, duplicates, minimum-window substrings, most-frequent char) rather than their relative order. Sorting should be preferred only when the order of the elements matters or the alphabet is so small that the constant factors of a count array outweigh the log factor — for anything over a few dozen characters, counting wins.

## Running the solutions

Each file is self-contained; run it with Python directly:

```bash
python valid_anagram.py
```

Or import the class into your own script:

```python
from valid_anagram import Solution

s = Solution()
print(s.isAnagram("anagram", "nagaram"))  # True
```
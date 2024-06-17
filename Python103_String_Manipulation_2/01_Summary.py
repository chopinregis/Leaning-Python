# Example 1: Reverse a String
def reverse_string(s):
    return s[::-1]

# Example 2: Check if a String is a Palindrome
def is_palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]

# Example 3: Count the Number of Vowels in a String
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Example 4: Remove All Whitespace from a String
def remove_whitespace(s):
    return ''.join(s.split())

# Example 5: Capitalize the First Letter of Each Word in a String
def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

# Example 6: Find the Longest Word in a String
def longest_word(s):
    words = s.split()
    return max(words, key=len)

# Example 7: Replace All Occurrences of a Substring in a String
def replace_substring(s, old, new):
    return s.replace(old, new)

# Example 8: Remove Punctuation from a String
import string
def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

# Example 9: Find the Frequency of Each Character in a String
def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Example 10: Check if Two Strings are Anagrams
def are_anagrams(s1, s2):
    return sorted(s1.replace(' ', '').lower()) == sorted(s2.replace(' ', '').lower())

# Testing the functions
print(reverse_string("hello"))  # Output: "olleh"
print(is_palindrome("A man a plan a canal Panama"))  # Output: True
print(count_vowels("hello world"))  # Output: 3
print(remove_whitespace("hello world"))  # Output: "helloworld"
print(capitalize_words("hello world"))  # Output: "Hello World"
print(longest_word("The quick brown fox jumps over the lazy dog"))  # Output: "jumps"
print(replace_substring("hello world", "world", "there"))  # Output: "hello there"
print(remove_punctuation("hello, world!"))  # Output: "hello world"
print(char_frequency("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(are_anagrams("listen", "silent"))  # Output: True
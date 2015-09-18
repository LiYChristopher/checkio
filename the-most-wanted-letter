'''You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string (unicode for py2.7).

Output: The most frequent letter in lower case as a string.'''

def checkio(text):
    h_count = 0
    most_wanted = 'a'
    only_chars = [char.lower() for char in text if char.isalpha()]
    for char in only_chars:       
        if only_chars.count(char) >= h_count:
            h_count, most_wanted = (only_chars.count(char), char) 
    for char in only_chars:
        if only_chars.count(char) == h_count and char < most_wanted:
            most_wanted = char
    return most_wanted    

''' A basic text decryption task 
Input: A text for analysis as a string (unicode for py2.7).
Output: The most frequent letter in lower case as a string.

More info at https://www.checkio.org/mission/most-wanted-letter/
'''

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

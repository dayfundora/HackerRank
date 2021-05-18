def filter_vowels(word)
    consonants_word = [letter for letter in word if not isVowel(letter)]
    filtered_word = ''.join(consonants_word)
    return filtered_word

def filter_consonants(word)
    vowels_word = [letter for letter in word if isVowel(letter)]
    filtered_word = ''.join(vowels_word)
    return filtered_word

def isVowel(letter)
    vowels=['a','e','i','o','u']
    if letter.lower() in vowels:
        return True
    else:
        return False
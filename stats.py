def count_words(text):
    """
    Counts the number of words in a given text.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The word count.
    """
    words = text.split()
    return len(words)
def count_characters(text):
    """
    Counts the number of characters in a given text.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The character count.
    """
    character_lower = text.lower()
    character_count = {}
    for char in character_lower:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count
    
def sort_characters(character_count):
    """
    Sorts the character count dictionary by character.
    Args:
        character_count (dict): The dictionary containing character counts. 
    return character_count  
    """
    sorted_characters = dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True))
    return sorted_characters
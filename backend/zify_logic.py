def zify_word(word):
    """
    Z-ifies a word based on simple linguistic rules:
    - Replace the first consonant with 'Z' if it flows better.
    - Add 'Z' as a prefix if the first letter is a vowel.
    - Handle special blends (e.g., "ch", "sh").
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    first_letter = word[0].lower()

    # Rule 1: If the first letter is a vowel, add 'Z' as a prefix
    if first_letter in vowels:
        return "Z" + word

    # Rule 2: Check for common blends
    blends = {"sh", "ch", "th", "ph", "bl", "br"}
    if word[:2].lower() in blends:
        return "Z" + word[2:]

    # Rule 3: Default to replacing the first consonant with 'Z'
    return "Z" + word[1:]

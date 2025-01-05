def zify_word(word):
    """
    Z-ifies a word based on simple linguistic rules:
    - Add 'Z' as a prefix if the first letter is a vowel.
    - Remove common blends (e.g., "sh", "ch") and replace with 'Z'.
    - Replace the first consonant with 'Z' if none of the above applies.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    first_letter = word[0].lower()

    if " " in word:
        return "Error: Input must be a single word."

    negative_words = {"no", "nope", "nah"}
    if word.lower() in negative_words:
        return "Z"

    # Rule 1: If the first letter is a vowel, add 'Z' as a prefix
    if first_letter in vowels:
        return "Z" + word.lower()

    #Rule 2: Handle common blends
    blends = {"sh", "ch", "th", "ph", "sp", "tr", "wh"}
    if len(word) > 1 and word[:2].lower() in blends:
        return "Z" + word[2:]  # Skip the first two letters (blend)

    # Rule 3: Default to replacing the first consonant with 'Z'
    return "Z" + word[1:]

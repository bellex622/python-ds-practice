def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    lower = to_swap.islower()
    if lower:
        phrase = phrase.replace(to_swap, "$")
        phrase = phrase.replace(to_swap.upper(), to_swap)
        phrase = phrase.replace("$", to_swap.upper())
    else:
        phrase = phrase.replace(to_swap, "$")
        phrase = phrase.replace(to_swap.lower(), to_swap)
        phrase = phrase.replace("$", to_swap.lower())

    return phrase

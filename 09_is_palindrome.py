def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # use built-in string method to replace " "

    phrase_lowercase = phrase.lower()
    left = 0
    right = len(phrase_lowercase)-1


    while left<right:
        # check for space

        while phrase_lowercase[left] == " ":
            left +=1
        while phrase_lowercase[right] == " ":
            right -=1


        if phrase_lowercase[left]!=phrase_lowercase[right]:
            return False
        else:
            left+=1
            right-=1

    return True






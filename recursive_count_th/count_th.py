'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) < 2:
        return 0
    # if string is less than 2 characters, there cannot be any "th". Stop.
    if word[0:2] == "th":
        return count_th(word[2:]) + 1
    # if the first two characters are "th", add one and repeat function without them
    else:
        return count_th(word[1:])
    # if the first two characters are not "th", remove the first character and repeat the function

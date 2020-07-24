'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    if len(word) < 2:
        return 0
    if word[0:2] == 'th':
        # if found: add 1 to count and continue recursion
        return count_th(word[1:]) + 1
    else:
        # not found: don't add, keep looking
        return count_th(word[1:])

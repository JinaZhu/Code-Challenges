# Write a function that reverse characters inside paraentheses in a given string and return a new string with characters inside parentheses reversed and parentheses removed
# (bar) >> rab, foo(bar)baz >> foorabbaz, foo(bar(baz))blim >> foobazrabblim


def reverse_in_parentheses(str):
    while str.find(")") != -1:
        str = reverseP(str)

    return str


def reverseP(str):

    open_bracket_int = str.rindex("(")

    before_bracket = str[0:open_bracket_int+1]

    after_bracket = str[open_bracket_int+1:]

    close_bracket_int = len(before_bracket) + after_bracket.find(")")

    firstPart = str[:open_bracket_int]
    secondPart = str[close_bracket_int+1:]
    middle = str[open_bracket_int+1: close_bracket_int]

    middle = middle[::-1]

    return firstPart + middle + secondPart


a = "(abc)d(efg)"
print(reverse_in_parentheses(a))

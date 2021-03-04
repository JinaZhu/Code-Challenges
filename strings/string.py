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
b = "foo(bar)baz"
print(reverse_in_parentheses(b))

# Count and Say
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# https://leetcode.com/problems/count-and-say/

def count_and_say(times):
    if times == 1:
        return "1"
    
    current = "1"

    for _ in range(times-1):
        next = ""
        count = 1

        for j in range(len(current)-1):
            if current[j] == current[j+1]:
                count += 1
            else:
                next += str(count) + current[j]
                count = 1
        next += str(count) + current[-1]
        current = next
    return current 

count_and_say_testcase = 7
count_and_say_result = count_and_say(count_and_say_testcase)
count_and_say_test = count_and_say_result == "13112221"
print('count_and_say_test', count_and_say_test)

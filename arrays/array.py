# return a list of all characters that show up in all strings within the list (including duplicates).


def common_char(word_lst):
    previous_word = list(word_lst[0])

    for word in word_lst[1:]:
        current_word = []
        for char in word:
            if char in previous_word:
                current_word.append(char)
                previous_word.remove(char)
        previous_word = current_word

    return previous_word


print('common_char', common_char(
    ["bella", "label", "roller"]))

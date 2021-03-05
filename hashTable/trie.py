# Escape Room Keypads
# You're attempting to solve a puzzle in an escape room with your team where you need to open a door to get to the next stage. There are serveral doors, each with a different keypad on it. The keypads each have 7 keys, containing 7 distinct letters
# The instructions state that one of the keypads will open the correct door leading to the next stage of the game. Your job is to find a word that unlocks the correct keypad
# After struggling for some time, the escape room leader have you a clue, that the first letter of the keypad is guaranteed to be in the word that opens the door. We will call this the key letter
# the goal of this exercise is to come up with as many words as possible that your team can test out on the keypads and find the correct comhination to go to the next stage of the game.
# what you know:
# the correct combination will be a valid english word
# the words are at least 5 letters long, with no max length
# the key letter will be in the correct answer
# the words do not contain any letters outside the seven letters on the keypad
# letters may be reused, including the key letter

def escape_room_keypads(words, keys):
    trie = {}

    for word in words:
        current_level = trie

        for letter in sorted(word):
            if letter not in current_level:
                current_level[letter] = {}

            current_level = current_level[letter]
        current_level['match_count'] = current_level.get('match_count', 0) + 1
    
    result = [0] * len(keys)

    def traverse_trie_helper(trie, index, contain_first_letter):
        if 'match_count' in trie and contain_first_letter:
            result[index] += trie['match_count']
        current_keyword = keys[index]

        for key in trie:
            if key in current_keyword:
                if current_keyword[0] == key or contain_first_letter:
                    traverse_trie_helper(trie[key], index, True)
                else:
                    traverse_trie_helper(trie[key], index, False)
        
    for index in range(len(keys)):
        traverse_trie_helper(trie, index, False)
        
    return result

escape_room_keypads_words = ['APPLE', 'PLEAS', 'PLEASE']
escape_room_keypads_keys = ['AELWXYZ', 'AELPXYZ', 'AELPSXY', 'SAELPRT', 'XAEBKSY']
escape_room_keypads_result = escape_room_keypads(escape_room_keypads_words, escape_room_keypads_keys)
escape_room_keypads_test = escape_room_keypads_result == [0, 1, 3, 2, 0]
print('escape_room_keypads_test', escape_room_keypads_test)

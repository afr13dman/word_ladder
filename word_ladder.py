#!/bin/python3

from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny',
        'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots',
        'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    if start_word == end_word:
        return [start_word]

    stack = []
    stack.append(start_word)
    queue = deque()
    queue.append(stack)

    dict_list = []
    with open(dictionary_file, "r", newline="") as dict_file:
        for row in dict_file:
            dict_list.append(row.strip())

    while len(queue) != 0:
        working_stack = queue.popleft()
        for word in list(dict_list):
            check_adjacent = _adjacent(working_stack[-1], word)
            if check_adjacent:
                if word == end_word:
                    working_stack.append(word)
                    return working_stack
                new_stack = copy.copy(working_stack)
                new_stack.append(word)
                queue.append(new_stack)
                dict_list.remove(word)
    if len(queue) == 0:
        # it is impossible to generate a word ladder with the two words
        return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if len(ladder) == 0:
        return False
    if len(ladder) == 1:
        return True

    entry = 1  # start one before initial index so it indexes to the next word
    for word in ladder:
        if word == ladder[-1]:
            return True
        if not _adjacent(word, ladder[entry]):
            return False
        entry += 1
    # if all words are adjacent to its neighbors the for loop will complete
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False

    #  if words are same length proceed
    same_chars = 0
    for let in range(len(word1)):
        if word1[let] == word2[let]:
            same_chars += 1
    if same_chars + 1 == len(word1):
        return True
    else:
        return False

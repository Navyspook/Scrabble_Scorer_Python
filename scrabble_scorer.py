

old_point_structure = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    letter_points = ""

    for char in word:
        for point_value in old_point_structure:
            if char in old_point_structure[point_value]:
                letter_points += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letter_points

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
    prompt = input("Let's play some Scrabble!\n\nEnter a word you would like scored: ")
    return prompt

def simple_scorer(word):
    score = 0

    for letter in word.lower():
        score += 1
    
    return score

def vowel_bonus_scorer(word):
    score = 0
    const = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    vowel = ['a', 'e', 'i', 'o', 'u']

    for letter in word.lower():
        if letter in const:
            score += 1

        if letter in vowel:
            score += 3
 
    return score

new_point_structure = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def scrabble_scorer(word):
    score= 0

    for letter in word.lower():
        if letter in new_point_structure:
            score += new_point_structure[letter]
    return score 

def scorer_prompt():
    prompt = input('Which scoring alogrithm would you like to use?\n\n0 - Simple: One point per character\n1 - Vowel Bonus: Vowels are worth 3 points\n2 - Scrabble: Uses scrabble point system\nEnter 0, 1, or 2: ')
    return prompt

def transform():
    return

def run_program():
    word = initial_prompt()
    scorer = scorer_prompt()

    if scorer == '0':
        print(f'Your score for "{word}" is {simple_scorer(word)}')
    elif scorer == '1':
        print(f'Your score for "{word}" is {vowel_bonus_scorer(word)}')
    elif scorer == '2':
        print(f'Your score for "{word}" is {scrabble_scorer(word)}')
    else:
        print(run_program())



run_program()
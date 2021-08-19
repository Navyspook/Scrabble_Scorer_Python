

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

# def old_scrabble_scorer(word):
#     word = word.upper()
#     score = 0

#     for char in word:
#         for point_value in old_point_structure:
#             if char in old_point_structure[point_value]:
#                 score += point_value

#     return score

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

def scrabble_scorer(word):
    score = 0

    for letter in word.lower():
        if letter in new_point_structure:
            score += new_point_structure[letter]

    return score

old_scrabble_scorer_dict = {
    'name': 'Scrabble',
    'description': 'is the traditional scoring algorithm.',
    'score_function': scrabble_scorer
}
simple_scorer_dict = {
    'name': 'Simple Score',
    'description': 'each letter is worth 1 point.',
    'score_function': simple_scorer
}
vowel_bonus_scorer_dict = {
    'name': 'Bonus Vowels',
    'description': 'vowels are 3 pts, consonants are 1 pt.',
    'score_function': vowel_bonus_scorer
}

# print(simple_scorer_dict['name'])
# print(simple_scorer_dict['description'])
# print(simple_scorer_dict['score_function']('justin'))

scoring_algorithms = (old_scrabble_scorer_dict, simple_scorer_dict, vowel_bonus_scorer_dict)

# print(scoring_algorithms[0]['name'])

def scorer_prompt():
    user_selection = int(input('Which scoring alogrithm would you like to use?\n\n0 - Scrabble: Uses scrabble point system\n1 - Simple: One point per character\n2 - Vowel Bonus: Vowels are worth 3 points \nEnter 0, 1, or 2: '))
    
    scoring_algorithm_dict = scoring_algorithms[user_selection]

    return scoring_algorithm_dict

def transform(provided_dict):
    new_dict = {}

    for (key, value) in provided_dict.items():
        for letter in value:
            new_dict[letter.lower()] = key

    return new_dict

new_point_structure = transform(old_point_structure)

def run_program():
    word = initial_prompt()

    scoring_algorithm_dict = scorer_prompt()

    score = scoring_algorithm_dict['score_function'](word)

    print(
        f'''
The word you entered was "{word}".
You selected the "{scoring_algorithm_dict["name"]}" scoring algorithm which {scoring_algorithm_dict["description"]}.
Your word is worth {score} points!'''
    )



run_program()
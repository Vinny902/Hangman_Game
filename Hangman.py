hangman_logo = '''
_
| |
| |__ __ _ _ __ __ _ _ __ ___ __ _ _ __
| '_ \ / | '_ \ / _ | ' _ \ / _ | '_ \
| | | | (| | | | | (| | | | | | | (| | | | |
|| ||_,|| ||_, || || ||_,|| ||/||/ \n'''

print(hangman_logo)

import random

words = ["python",
"coding", 
"tomato", 
"javascript", 
"colors", 
"utility", 
"lecture", 
"teacher"
'abruptly',
'absurd',
'abyss',
'affix',
'askew',
'avenue',
'awkward',
'axiom',
'azure',
'bagpipes',
'bandwagon',
'banjo',
'bayou',
'beekeeper',
'bikini',
'blitz',
'blizzard',
'boggle',
'bookworm',
'boxcar',
'boxful',
'buckaroo',
'buffalo',
'buffoon',
'buxom',
'buzzard',
'buzzing',
'buzzwords',
'caliph',
'cobweb',
'cockiness',
'croquet',
'crypt',
'curacao',
'cycle',
'daiquiri',
'dirndl',
'disavow',
'dizzying',
'duplex',
'dwarves',
'embezzle',
'equip',
'espionage',
'euouae',
'exodus',
'faking',
'fishhook',
'fixable',
'fjord',
'flapjack',
'flopping',
'fluffiness',
'flyby',
'foxglove',
'frazzled',
'frizzled',
'fuchsia',
'funny',
'gabby',
'galaxy',
'galvanize',
'gazebo',
'giaour',
'gizmo',
'glowworm',
'glyph',
'gnarly',
'gnostic',
'gossip',
'grogginess',
'haiku',
'haphazard',
'hyphen',
'iatrogenic',
'icebox',
'injury',
'ivory',
'ivy',
'jackpot',
'jaundice',
'jawbreaker',
'jaywalk',
'jazziest',
'jazzy',
'jelly',
'jigsaw',
'jinx',
'jiujitsu',
'jockey',
'jogging',
'joking',
'jovial',
'joyful',
'juicy',
'jukebox',
'jumbo',
'kayak',
'kazoo',
'keyhole',
'khaki',
'kilobyte',
'kiosk',
'kitsch',
'kiwifruit',
'klutz',
'knapsack',
'larynx',
'lengths',
'lucky',
'luxury',
'lymph',
'marquis',
'matrix',
'megahertz',
'microwave',
'mnemonic',
'mystify',
'naphtha',
'nightclub',
'nowadays',
'numbskull',
'nymph',
'onyx',
'ovary',
'oxidize',
'oxygen',
'pajama',
'peekaboo',
'phlegm',
'pixel',
'pizazz',
'pneumonia',
'polka',
'pshaw',
'psyche',
'puppy',
'puzzling',
'quartz',
'queue',
'quips',
'quixotic',
'quiz',
'quizzes',
'quorum',
'razzmatazz',
'rhubarb',
'rhythm',
'rickshaw',
'schnapps',
'scratch',
'shiv',
'snazzy',
'sphinx',
'spritz',
'squawk',
'staff',
'strength',
'strengths',
'stretch',
'stronghold',
'stymied',
'subway',
'swivel',
'syndrome',
'thriftless',
'thumbscrew',
'topaz',
'transcript',
'transgress',
'transplant',
'triphthong',
'twelfth',
'twelfths',
'unknown',
'unworthy',
'unzip',
'uptown',
'vaporize',
'vixen',
'vodka',
'voodoo',
'vortex',
'voyeurism',
'walkway',
'waltz',
'wave',
'wavy',
'waxy',
'wellspring',
'wheezy',
'whiskey',
'whizzing',
'whomever',
'wimpy',
'witchcraft',
'wizard',
'woozy',
'wristwatch',
'wyvern',
'xylophone',
'yachtsman',
'yippee',
'yoked',
'youthful',
'yummy',
'zephyr',
'zigzag',
'zigzagging',
'zilch',
'zipper',
'zodiac',
'zombie',
]



def hangman():
    chosen_word = random.choice(words)
    


    display = []
    word_lenth = len(chosen_word)



    for ch in range(word_lenth):
        display += '_'
    print(display)
    lives = 6
    end_of_game = False

    while not end_of_game:
        users_guess = input("Guess a letter: ").lower()
    
        if users_guess in display:
            print(f"You've have already guessed {users_guess} ")

        for position in range(word_lenth):
            letter = chosen_word[position]
            if letter == users_guess:
                display[position] = letter
            
        print(display)
        

        if users_guess not in chosen_word:
            print(f'You guessed {users_guess}, It is not in the word.\nYou lose a life')
            lives -= 1
            print(f"You have {lives} lives left")
            if lives == 0:
                print("You have ran out of lives\nYOU LOSE!")   
                end_of_game = True

                question = input("Do you still want to play?\nYes/No: ").lower()
                if question == 'yes':
                    hangman()
                elif question == "no":
                    print("GAME OVER!\nThank you for playing Hangman")
                    end_of_game = True
                else:
                    print("Invald Input")
                    
                   


        if "_" not in display:
            end_of_game = True
            print("You win!")      

            question = input("Do you still want to play?\nYes/No: ").lower()
            if question == 'yes':
                hangman()
            elif question == 'no':
                print("GAME OVER!\nThank you for playing Hangman")
                end_of_game = True
            else:
                print("Invald Input")
                
    

hangman()


import random

def h6():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |     --|--') 
    print('        |       |')
    print('        |      /|\ ') 
    print('        |     / | \ ')
    print('        |') 
    print('      -----')

def h5():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |     --|--') 
    print('        |       |')
    print('        |      /|') 
    print('        |     / | ')
    print('        |') 
    print('      -----')

def h4():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |     --|--') 
    print('        |       |')
    print('        |       |')
    print('        |       |') 
    print('        |') 
    print('      -----')

def h3():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |     --|') 
    print('        |       |')
    print('        |       |') 
    print('        |       | ')
    print('        |') 
    print('      -----')

def h2():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |       |') 
    print('        |       |')
    print('        |       |') 
    print('        |       |')
    print('        |') 
    print('      -----')

def h1():
    print('        _________')
    print('        |/      |')  
    print('        |       O') 
    print('        |') 
    print('        |')
    print('        |') 
    print('        |') 
    print('      -----')

def h0():
    print('        _________')
    print('        |/      |')  
    print('        |') 
    print('        |') 
    print('        |')
    print('        |') 
    print('        |') 
    print('      -----')

def hang(status):
        if status == 1:
            h1()
        elif status == 2:
            h2()
        elif status == 3:
            h3()
        elif status == 4:
            h4()
        elif status == 5:
            h5()
        elif status == 6:
            h6()
    
def get_word():
    words = ['Woodstock',
        'Gary',
        'Tucker',
        'Gopher',
        'Spike',
        'Ed',
        'Faline',
        'Willy',
        'Rex',
        'Rhino',
        'Roo',
        'Littlefoot',
        'Bagheera',
        'Remy',
        'Pongo',
        'Kaa',
        'Rudolph',
        'Banzai',
        'Courage',
        'Nemo',
        'Nala',
        'Alvin',
        'Sebastian',
        'Iago',
        'Zazu',
        'Diego',
        'Dory',
        'Pumbaa',
        'Rabbit',
        'Garfield',
        'Manny',
        'Chewbacca',
        'Sid',
        'Flik',
        'Marty',
        'Gloria',
        'Melman',
        'Alex',
        'Julien',
        'Wilbur',
        'Asian',
        'Droopy',
        'Simba',
        'Snoopy',
        'Mufasa',
        'Kerchak',
        'Scar',
        'Pete',
        'Balto',
        'Eeyore',
        'Piglet',
        'Donkey',
        'Timon',
        'Baloo',
        'Thumper',
        'Bambi',
        'Goofy',
        'Tom',
        'Sylvester',
        'Jerry',
        'Tigger']

    return random.choice(words).upper()

def check(word, guesses, guess):
    guess = guess.upper()
    status = ''

    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += '*'

        if letter == guess:
            matches += 1

    if matches > 1:
        print('Yes! The word contains',matches,'"' + guess + '"' + 's')
    elif matches == 1:
        print('Yes! The word contains the letter "' + guess + '"')
    else:
        print('Sorry. The word does not contain the letter"' + guess + '"')

    return status

def main():
    word = get_word()
    #print(word)
    guesses = []
    guessed = False ## boolean
    print('The word contains', len(word), 'letters.')
    failedCount = 0
    currentresult = ''

    for i in range(0, len(word)):
        currentresult = currentresult + '*'

    while not guessed:
        text = 'Please enter one letter or a {}-letter word. '.format(len(word))
        guess = input(text)
        guess = guess.upper()
        if guess in guesses:
            print('You already guessed "' + guess + '"')
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print('Sorry, that is incorrect.')

        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word,guesses,guess)
            if result == word:
                guessed = True
            else:
                if result == currentresult: 
                    failedCount = failedCount + 1
                    print('faildCount ' + str(failedCount)) 
                  
                print(result)
                currentresult = result


        else:
           print('Invalid entry.')

    print('Yes, the word is', word + '! You got it in', len(guesses), 'tries.')

main()
     
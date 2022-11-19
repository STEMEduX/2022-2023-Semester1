story = '''
{}. But! {} only if ye be {} of valor!
For {} is guarded by a {} so {},
so {}, that no {} yet has {}
with it... and {}!
'''

def main():
    command = input('Enter a command (e.g. Eat): ')
    plural_noun = input('Enter a plural noun (e.g. trees): ')
    animal = input('Enter an animal (e.g. cow): ')
    location = input('Enter a location (e.g., Maine or the playground): ')
    singular_noun = input('Enter a singular noun (e.g., tree): ')

    adjectives = []
    adjectives.append(input('Enter an adjective (e.g. big): '))
    adjectives.append(input('Enter another adjective: '))

    past_participles = []
    past_participles.append(input('Enter a past participle: '))
    past_participles.append(input('Enter another past participle: '))

    mad_lib = story.format(command, 
                           command,
                           plural_noun,
                           location,
                           animal,
                           adjectives[0],
                           adjectives[1],
                           singular_noun,
                           past_participles[0],
                           past_participles[1])

    print(mad_lib)

main()


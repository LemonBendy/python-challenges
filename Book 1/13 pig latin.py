vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
ay = 'ay'
way = 'way'

new_word: str = input("Input word to be changed: ")
new_word = new_word.lower()
f_letter: str = new_word[0]

if f_letter in consonants:
    len_word: int = len(new_word)
    rem_word: str = new_word[1: len_word]
    pig_latin: str = rem_word + f_letter + ay
    print(pig_latin)
elif f_letter in vowels:
    pig_latin = new_word + way
    print(pig_latin)


        

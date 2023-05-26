#show the full word at the end of the game
#only 6 tries **DONE**
#implement a menu **DONE**

import random
from words import words
import string


def get_valid_word(words):
	word = random.choice(words) #randomly chooses something from the list
	while '-' in word or ' ' in word:
		word = random.choice(words)
	
	return word.upper()

def hangman():
	word = get_valid_word(words)
	word_letters = set(word) #letter in the word
	alphabet = set(string.ascii_uppercase)
	used_letters = set() #what the user has guessed

	#getting user input


	wrong_guesses = 0
	
	while len(word_letters) > 0 and wrong_guesses < 6:

		#letters used
		print("\n\tYou have already used these letters: ", ' '.join(used_letters))

		#current word with -
		word_list = [letter if letter in used_letters else "-" for letter in word ]
		print('\tCurrent word: ', ' '.join(word_list))

		user_letter = input("\tTry to guess the letter: ").upper()
	
		if user_letter in alphabet - used_letters:
			used_letters.add(user_letter)
			if user_letter in word_letters:
				word_letters.remove(user_letter)
			else:
				wrong_guesses = wrong_guesses + 1
		elif user_letter in used_letters:
			print('\tYou have already typed this character')
		else:
			print('\tInvalid character! Please, try again')

		if wrong_guesses == 6:
			print('\tGAMER OVER\n')


#user_input = input("Type something: ")
#print(user_input)

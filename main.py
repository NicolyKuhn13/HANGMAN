from hangman import hangman


def menu():

	print('''
	-------------------
	----- HANGMAN -----
	-------------------
	1) Play
	2) Rules
	3) Exit
	-------------------''')

	return int(input('''
	Pick: '''))

op = menu()

if op == 1:
	hangman()

elif op == 2:
	print('''
	
	Can you beat the clock to guess the hidden word before the poor stick figure meets its doom? Hangman is a quick and easy game thats perfect if youre trying to kill some time, prove your vocab superiority, or turn a boring old study session into something more exhilarating. In this article, well break down everything you need to know about playing this classic game.
	
	''')

elif op == 3:
  print('Bye!')
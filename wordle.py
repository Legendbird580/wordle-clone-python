print('''
Hello and welcome to Bad Wordle Clone!
You have five guesses to guess a word! 
It can only be a five letter word.
 P.S Please don't write nonsense words. We don't have a filter for that.
''')
answer=list('moose')
rounds=0
counter=0 #this in NOT the thing that counts the rounds. It should only ever have the value of zero. If it isn't zero, please go ahead and panic.
correctanswer=False
while rounds <5:
	wrongplace=[]
	y=5-rounds
	print('you have')
	print(y)
	print( 'guesses left')
	myinput=list(input())
	if len(myinput) ==5:
		counter=0
	else:
		print ('only five-letter words please.')
		continue
	if myinput==answer:
		correctanswer=True
		break
	else:
		for x in myinput:
			if x in answer and x not in wrongplace:
				wrongplace.append(x)
	if wrongplace==[]:
		print('wrong')
	else:
			print('the letters that are in the word are(in no specific order:)')
			print(wrongplace)
	rounds = rounds+1
	
if correctanswer==True:
	print('''Congrats! 
You won Wordle!
Are you proud of yourself?
SHOULD you be proud of yourself?
You gonna put Wordle Master on your CV? Nah mate.
You just wasted your time here.
Just like I did, writing this program. ''')
else:
	print('Haha loser.')
	print('the word was')
	print(answer)
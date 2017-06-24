while.py

#!/usr/bin/python
# Filename:while.py

number = 23
running = True

while running:
	guess = int(raw_input('Enter an intege:'))

	if guess == number:
		print 'Congratulations,you guessed it.'
		running = false # this causes the while loop to stop
    elif guess < number:
    	print 'No,it is a little higher than that'
    else:
    	print 'No,it is a little lower than that'
else:
	print 'The while loop is over.'
	# Do anyting else you want to do heer

print 'Done'
break.py

#!/usr/bin/python
# Filename: break.py

while True:
	s = raw_input('Enter someting:')
	if s == 'quit':
		break
	print 'length of the string is',len(s)
print 'Done'


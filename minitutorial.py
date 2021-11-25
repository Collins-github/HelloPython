''' 
1. 

When you create a variable and assign a name to it, the computer creates space in its memory to store/save that variable with that name. For example, when you write;
'''
		
	numb = 4

		
'''
Think of a new file been created, the content is 4 and the name of the file is numb. 


When you assign numb to a different variable without giving 4 another name, 4 has been orphaned. 

e.g
'''

	numb = 4
	max = numb 
	numb = 7
	
'''
4 is not orphaned because it is still stored in max though numb changed. 
Think of max as a duplicate of numb.
But here:
'''
	numb = 4
	numb = 5 

'''
4 is lost. Think of a 4 as a fike without a name. It means 4 cannot be queried which means 4 cannot be found on the device. Essentially, it does not exist.


When Python reclaims the previously allocated memory and uses it for something else, it is called 'Garbage Collection.' 

This isn't a tip that helps you write better codes but to give you an understanding of the system you are working with. 

It is more of an interview question.


2. 

I believe you know the rules of naming variables:


i. Variable names can be anything and is case sensitive.


ii. Variable names cannot start with numbers but can have numbers in them. For example:	
'''

 	1num = 6	# -> invalid
 	n1um = nu1m = num1 = 6	# all valid
 	
'''
iii. Variable names can take underscores(_). Underscores can be used to separate multi-word variable names and can start a variable name. For example: 
'''

	_age = new_age = a_g_e = 16	# all valid
	
'''
iv. Variable names do not take symbols, because these symbols are used in the language syntaxes.


What you probably did not know is that variable names cannot exactly be anything. Certain words cannot be used as variable names. These are called 'keywords' and are used in python syntaxes. For example:
'''

if else print input def in is and or not # etc.

'''
The reason is obvious. If these words are variable containers, how would python differentiate them and the built-in function they are assigned to. Someone could write this:
'''

	print = "A string"
	print(print)
	
# or

	if = 10
	for number in range(0,30)
	if += 1
	if if == 20:
		print(if)
		
'''
If you were python would you enjoy processing this?

3. 

When calculating on the interpreter/terminal/interactive shell, using an underscore gets the value of the last expression. For example: 
'''

	>>> 3 + 8
	>>> 24	# output
	>>> _ / 2
	>>> 12	# output
	
'''
This doesn't work on an IDE, unfortunately. This feature was sold for a GUI.
'''
'''
Bonus: These are syntax I learnt from a Python 2 materials. 
1. I did not know a variable can contain multiple values like a list without explicitly being one.
2. I filled placeholders without concatenation, formatting or f strings.
Obviously, this is unpythonic for Python 3.
'''
        names = "Mercedes", "Honda"
        number = 4, 5
        print("My cars are", names[0], "and", names[1], "and they are", number[0], "and", number[1], "in numbers respectively")

'''
	String
	raw_input() py2 input() py3
'''

my_string = 'kk'
print (len(my_string))
print (my_string.upper())

#name = raw_input("What is your name? ")
#quest = raw_input("What is your quest? ")
#color = raw_input("What is your favorite color? ")

name = input("What is your name? ")
quest = input("What is your quest? ")
color = input("What is your favorite color? ")

print ("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))
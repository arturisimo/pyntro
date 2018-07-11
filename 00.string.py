'''
	String

'''

my_string = 'kk'
print (len(my_string))
print (my_string.upper())

#slice
other_string ='kakotas'
print (other_string[1:5])

#split
ab = '1,2,3,4,5'
mylist = ab.split(',')
print (mylist) #> ['1','2','3','4','5']

#join
cd = "-".join(mylist)
print (cd) #> 1-2-3-4-5

#raw_input() en py2 /  input() en py3
name = input("What is your name? ")
quest = input("What is your quest? ")
color = input("What is your favorite color? ")

#string con paramentos
print ("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))
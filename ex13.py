#from sys import argv

#script, first, second, third = argv

#print "The script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third

from sys import argv

script, firstname, lastname = argv

firstname = raw_input("What's your first name")
lastname = raw_input("what's your last name")

print "The script is called:", script
print "Your first name is:", firstname
print "Your last name is:", lastname

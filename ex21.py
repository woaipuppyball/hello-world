def add(a,b):
    print "Adding %d + %d" % (a,b)
    return a + b

def subtract (a,b):
    print "Subsctracting %d - %d" % (a,b)
    return a - b

def multiply (a,b):
    print "Multiple %d * %d" % (a,b)
    return a  * b

def divid (a,b):
    print "Dividing %d / %d" % (a,b)
    return a / b

print "Let's do some math with just functions!"

age = add (30, 5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divid(100,2)

print "Age: %d, height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."

what = add (age, subtract(height, multiply(weight,divid(iq,2))))

print "That becomes:", what, "Can you do it by hand?"


age2 = 24
iq2 = divid (34,100)
weight2 = 1023
what2 = add(age2,subtract(iq2,weight2))
print "What2 equals:", what2

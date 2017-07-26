name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_centimeter = height * 2.54
weight_kilo = weight * 0.453592

print "Let's talk about %s." % name
print "He's %r inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height,weight,age + height + weight) 

print "He's %d sentimeters tall" % height_centimeter
print "He's %d kilos heavy" % weight_kilo
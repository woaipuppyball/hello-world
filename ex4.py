# set cars to 100
cars = 100
# set space in a car variable
space_in_a_car = 4.0
# set drivers to 30
drivers = 30
# set passengers
passengers = 90
# calculate cars not driven
cars_not_driven = cars - drivers
# set cars driven
cars_driven = drivers
# calculate carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# calcuate average passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars avaialbe."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
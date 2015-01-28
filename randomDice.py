import random

diceroll = raw_input("How many times do you want to roll the dice? ")
diceroll = int(diceroll)
count = 0
one = 0.0
two = 0.0
three = 0.0
four = 0.0
five = 0.0
six = 0.0

while True:
    number = random.randrange(1,7)
    count += 1
    if number == 1:
        one += 1
    if number == 2:
        two += 1
    if number == 3:
        three += 1
    if number == 4:
        four += 1
    if number == 5:
        five += 1
    if number == 6:
        six += 1
    if count == diceroll:
        break

statsone = (one/count)*100
statstwo = (two/count)*100
statsthree = (three/count)*100
statsfour = (four/count)*100
statsfive = (five/count)*100
statssix = (six/count)*100

print "Out of %d rolls, your results are: " % diceroll
print "______________________"
print "One: %.2f%%, Count: %d" % (statsone, one)
print "Two: %.2f%%, Count: %d" % (statstwo, two)
print "Three: %.2f%%, Count: %d" % (statsthree, three)
print "Four: %.2f%%, Count: %d" % (statsfour, four)
print "Five: %.2f%%, Count: %d" % (statsfive, five)
print "Six: %.2f%%, Count: %d" % (statssix, six)

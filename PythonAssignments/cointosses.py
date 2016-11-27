print "Starting the program..."
import random
heads = 0
tails = 0
for count in range (1,5001):
    random_num = random.random()
    coin = round(random_num)
    # 1 = Heads 0 = Tails
    if coin == 1:
        heads = heads + 1
        print "Attempt #" + str(count) + ": Throwing a coin... It's a head...  Got " + str(heads) + " head(s) so far and " + str(tails) + " so far."
    else:
        tails = tails + 1
        print "Attempt #" + str(count) + ": Throwing a coin... It's a tail...  Got " + str(heads) + " head(s) so far and " + str(tails) + " so far."

print "Ending the program, thank you."

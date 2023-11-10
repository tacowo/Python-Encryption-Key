from alphaconverter import alphabet_position
from alphaconverter import return_to_text
from passchecker import passcheck
import random
import time
count = 0
guess = ""
while True:
    if passcheck(guess) == True:
        break
    guess = random.randrange(10000000000001, 16119199999999)
    count = count + 1      # 16119192315184
    print("ATTEMPT " + str(count) + " UNSUCCESSFUL... REROLL: " + str(guess) + " " + str(return_to_text(guess))) 
    time.sleep(0.5)
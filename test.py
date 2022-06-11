import random
import time
l = ["Can you cook pasta?", "Can she play guitar?", "Can he speak Chinese?", 
"Can they swim?", "Can you drive a car?", "I have a cold, what should I do?", 
"He is always late, what should he do?", "You failed the test, what should you do?",
 "We missed the bus, what should we do?", "They want to lose some weight, what should they do?", 
 "Describe one person in your family.", "Describe one of your friends.", 
 "Who is taller, your mom or your dad?", "Which is more delicious, cola, or coffee?", 
 "Who is funnier, you or your friend.", "Which is more difficult, English or Chinese?", 
 "Which is more enjoyable, watching YouTube or watching Netflix?"]
 
for i in range(10):
    r = random.randrange(17)
    print(l[r])
    time.sleep(10)


#자연스럽게

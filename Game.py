import random
score = botscore = 0
bat = False ; bowl = False 
print("Welcome to hand cricket Game  \n \n \n \n \n \n \n ")
usr = int(input("Enter 1 or 0 for toss :"))
toss = random.randint(0,1)
                
print(toss)
if toss == usr:
    print("U have won the toss")
    ch = int(input("enter 0 for batting and 1 for bowling :"))
else:
    print("U lost the toss")
    ch = random.randint(0,1)

if ch  == 0:
    bat = True
else:
    bowl = True
print("enter number 1 to 6")

if bat:
    print("               U are batting")
    while True:
        runs = int(input("Batting:"))
        rand = random.randint(1,6)
        if runs == rand:
            print("               OUT")
            break
        else:
            score += runs
    print("               U are bowling")
    while True:
        ball = int(input("Bowling:"))
        rand = random.randint(1,6)
        if ball == rand:
            print("               Out")
            break
        else:
            botscore += rand
        if botscore > score:
            break

if bowl:
    print("               U are Bowling")
    while True:
        ball = int(input("Bowling:"))
        rand = random.randint(1,6)
        if ball == rand:
            print("               Out")
            break
        else:
            botscore += rand
    print("               U are batting")
    while True:
        runs = int(input("Batting:"))
        rand = random.randint(1,6)
        if runs == rand:
            print("               OUT")
            break
        else:
            score += runs
        if score > botscore :
            break

print("Score = ",score,"Bot Score = ",botscore)

if score > botscore:
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n                U WON \n \n \n \n \n \n \n \n \n \n \n \n \n ")
else:
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n                U LOST \n \n \n \n \n \n \n \n \n \n \n \n \n ")

from random import randint # randint() used to print any randam number


win_count = 0
lose_count = 0
dice = ['1','2','3','4','5','6']
while True:
    input("press enter to Roll Dice")
    out = randint(1,6)
    print(f'🎲=>{dice[out-1]}')
    if out == 6:
        win_count += 1
    elif out == 1:
        lose_count += 1
    if win_count == 3:
        print("you win")  
        break   
    elif lose_count ==3:
        print("you lose") 
        break  

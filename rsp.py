import random
def main():
    playercounter=0
    computercounter =0
    for i in range(5):
        choices=("rock","paper","scissors")
        computer=random.choice(choices)
        player=input("whats your take ?").lower().strip()
        result = decidewinner(player,computer)
        if result=="player":
            playercounter=playercounter+1
        elif result=="computer":
            computercounter=computercounter+1
        print(f"player:{player},computer:{computer}")
        print(f"player:{playercounter},computer:{computercounter}") 
    print(f"FINAL SCORE = PLAYER : {playercounter} , COMPUTER : {computercounter}")       

def decidewinner(player,computer):
        if computer == player:
                return "tie"
        if player== "rock" and computer=="scissors":
                return"player"
                    
        if player== "scissors" and computer=="paper":
                return"player"
        if player== "paper" and computer=="rock":
                return "player"
        else:
                return "computer"                

main()      
       

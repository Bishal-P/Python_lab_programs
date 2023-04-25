import random
words=["name","game","quick","lion","single","loyal"]
player_1=0
player2=0
words_shown=[]
print("Player_1 will play first then player2 :")
def jumbled_word():
    global words_shown,words,current_word,jword
    while True:
        current_word=random.choice(words)
        if current_word not in words_shown:
            break
    words_shown.append(current_word)
    a=[i for i in range(len(current_word))]
    curlist=random.sample(a,len(current_word))
    jword=""
    for i in curlist:
        jword+=current_word[i]
    # print(jword)
    return jword
current_player=1
continue_or_not="y"
chance=1
while True:
    if chance==1:
        print("\n")
        print("The word is :",jumbled_word())
        result=input(f"Player{current_player} chance :")
    else:
        result=input(f"One more chance of Player{current_player}:")
        
    if result==current_word:
        if chance==1:
            if current_player==1:
                player_1+=2
            else:
                player2+=2
        else:
            if current_player==1:
                player_1+=1
            else:
                player2+=1
        chance=1
        if current_player==1:
            current_player+=1
        else:
            current_player=1
    else:
        if chance==1:
            chance+=1
            continue
        chance=1
        if current_player==1:
            current_player+=1
        else:
            current_player=1
    if current_player==1:
        continue_or_not=input("Do you want to continue the game (Y/n): ")
    if continue_or_not=="n" or continue_or_not=="N":
        break
        
print("\n")
if player_1>player2:
    print("Player_1 is the winner")
elif player_1==player2:
    print("Match draw")
else:
    print("Player2 is the winner")

print("\n")

print("The score of player_1 = ",player_1)
print("The score of player2 = ",player2)
print("\n")
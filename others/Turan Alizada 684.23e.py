import random

def BlackJack(Money) :
    Dict = {
        "2": 2,"3": 3,
        "4": 4, "5": 5,
        "6": 6, "7": 7,
        "8": 8, "9": 9,
        "10": 10, "J": 10,
        "A": 11
        }
    answer = "No"
    while answer.upper() == "NO" or Money > 0:
        answer = str(input("Do you want to quit? Yes or No : "))
        if answer.upper() == "YES" :
            return "Balance : " + str(Money)
        sum = 0
        sum_player = 0
        dealer = []
        player = []
        numbers = []
        bet = int(input("Place Your bet : "))
       
        for i in range(4) :
            choice = random.choice(list(Dict.items()))
            numbers.append(choice)
       
        for i in range(2) :
            choice = random.choice(list(Dict.items()))
            dealer.append(choice)
       
        for i in range(2) :
            choice = random.choice(list(Dict.items()))
            player.append(choice)
        print("Your hand : ", player)
       
        for i in player :
            sum_player += i[1]
        print("Your hand : " + str(sum_player))
       
        for i in dealer :
            sum += i[1]
       
        if sum > 21 or sum_player == 21 :
            Money += bet
            print("You Win")
            print("Balance : " + str(Money))
            print("Your hand : " + str(sum_player))
            print("Dealer's hand : " + str(sum))
           
        elif sum_player > 21 or sum == 21 :
            Money -= bet
            print("You Lost")
            print("Balance : " + str(Money))
            print("Your hand : " + str(sum_player))
            print("Dealer's hand : " + str(sum))
       
        else :
            n = 1
            for i in numbers :
                if sum_player == 21 :
                    Money += bet
                    print("You Win")
                    print("Balance : " + str(Money))
                    print("Your hand : " + str(sum_player))
                    print("Dealer's hand : " + str(sum))
                    break
                if sum_player > 21 :
                    Money -= bet
                    print("You Lost")
                    print("Balance : " + str(Money))
                    print("Your hand : " + str(sum_player))
                    print("Dealer's hand : " + str(sum))
                    break

                if sum > 21 and sum_player <= 21 :
                    Money += bet
                    print("You Win")
                    print("Balance : " + str(Money))
                    print("Your hand : " + str(sum_player))
                    print("Dealer's hand : " + str(sum))
                    break
                
                if i[0] == "A" and sum >= 16 :
                        sum += 1
                else :
                    sum += numbers[n][1]
                n += 1
                
                hand = str(input("Hit or Pass? : "))
                   
                if hand.upper() == "HIT" :
                    if i[0] == "A" and sum_player >= 16 :
                        sum_player += 1
                    else :
                        sum_player += i[1]
                    
                    print("Your hand : " + str(sum_player), i)
               
                else :
                    if sum_player <= sum :
                        Money += bet
                        print("You Win")
                        print("Balance : " + str(Money))
                        print("Your hand : " + str(sum_player))
                        print("Dealer's hand : " + str(sum))
                        break
                    else :
                        Money -= bet
                        print("You Lost")
                        print("Balance : " + str(Money))
                        print("Your hand : " + str(sum_player))
                        print("Dealer's hand : " + str(sum))
                        break
            
print(BlackJack(5000))
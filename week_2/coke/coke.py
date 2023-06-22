amount = 50
coin_25 = 25
coin_10 = 10
coin_5 = 5

while amount > 0:
    print("Amount Due:", amount)
    insert_coin = int(input("Insert Coin:"))
    if insert_coin == coin_25 or insert_coin == coin_10 or insert_coin == coin_5:
        amount -= insert_coin
        if amount == 0:
            print("Change Owed:", amount)
            break
        elif amount < 0:
            amount *= -1
            print("Change Owed:", amount)
            break
    else:
        print("Amount Due:", amount)






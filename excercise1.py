def ticketPrice(age,price,welfare=False):
    age = int(age)
    price = int(price)
    if(age <=11 and age >= 0):
        return price/2
    elif(age >=12 and age <= 18):
        return price*(3/4)
    elif(age >= 19 and welfare == True):
        return price * (3 / 4)
    else:
        return price

print(ticketPrice(10,500))
print(ticketPrice(15,500))
print(ticketPrice(20,500))
print(ticketPrice(20,500,True))
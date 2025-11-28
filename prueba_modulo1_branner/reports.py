from sales import (sales_consult)#here im trying to import the stock to read it and calculate

def range_books(registration): #I not finished this... but it supossed to be the range of most soled book
    for x in range (sales_consult(registration)):
        print(x)

def calculate_statistics(registration):#with this, it should calculate the price of all your stock of one book, but it doesnt works
    print("Choose one option: ")
    view_gain = (input("1. Gross profit\n2. Ganancia Neta\n"))
    taxes = 0.5
    Y = tickets['Amount']
    X = tickets['Price']
    Gross_profit = X * Y
    net_profit = Gross_profit / taxes
    if view_gain == ("1"):
        print("Your gross profit is: "(Gross_profit))
    elif view_gain == ("2"):
        print("Your neth profit is:: "(net_profit))
    else:
        print("Please use a valid title")

#I tried so much ):
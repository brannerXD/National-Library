#that is the employee services
def register_inventory(registration):#with this, the employee can add to the list the book what the client is buying
    ticket = {"Name": "", "Amount": 0, "Price": 0}
    ticket["Name"] = str(input("Enter the book title: "))
    while True:#thats a validation
        try:
            ticket["Amount"] = int(input("Enter te book amount: "))
            break
        except ValueError:
            print("Please, enter a valid number.")
    while True:#same
        try:
            ticket["Price"] = int(input("Enter the price of the book: "))
            break
        except ValueError:#if the employee makes something wrong, this print will be in his screen
            print("Please, enter a valid price.")
    registration.append(ticket)
    print(f"Book {ticket['Name']} added to stock.")

def sales_consult(registration):#that function makes a search possible for the employee, to see the stock and price
    if len (registration) == 0:
        print("The stock is empty, you can not see the inventory.")
        return
    Book_Name = input("Enter the book name: ").lower()
    Found = [Book for Book in registration if Book['Name'].lower() == Book_Name]
    if Found:
        for Book in Found:
            print(f"Book found: Name: {Book['Name']}, Amount: {Book['Amount']}, Price: ${Book['Price']:.2f}")
            return Book
        else:
            print("Product not found, please check title")
    input("Press ENTER to get back...")#with this, the employee can go back to main menu

def update_stock(registration):#with this, the employee can report when some books isnt in stock and update the info of them
    Book = sales_consult(registration)
    if Book:
        while True:#another validation LOL
            try:
                New_Price= int(input(f"Enter the new price for {Book['Name']}: "))
                Book['Price'] = New_Price
                print(f"Price updated for {Book['Name']}.")
                break
            except ValueError:
                print("Please, enter a valid number for the price...")
    while True:
        try:
            New_Amount= int(input(f"Enter new amount for {Book['Name']}: "))
            Book['Amount'] = New_Amount
            print(f"Amount updated for {Book['Name']}.")
            break
        except ValueError:
            print("Please, enter a valid amount to update...")
    input("Press ENTER to get back...")

def register_sales(registration):#with this, the employee can do like a voucher to the client, where he can see the book, amount and price of the product what he bought
    Product = sales_consult(registration)
    while True:
        try:
            registration.remove(Product)#with this, he get remove the book from stock, adn the client take it
            input(f"Press ENTER to confirm purcharse {Product['Name']} ")
            print(f"The book {Product['Name']} was purchased by you.")
            break
        except ValueError:
            print("Book not found.")
            break
    input("Press ENTER to get back...")

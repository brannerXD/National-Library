def register_book(stock):#this function saves the data of the books that the customer buys.
    stck = {"name": "", "author": "", "category": "", "amount": 0, "price": 0.0}
    stck["name"] = str(input("Enter the book title: "))
    stck["author"] = str(input("Enter the authors name: "))
    stck["category"] = str(input("Enter the books category: "))
    while True:#this is a validation 
        try:
            stck["amount"] = int(input("Enter te book amount: "))
            break
        except ValueError:
            print("Please, enter a valid number.")
    while True:#This is a validation too
        try:
            stck["price"] = float(input("Enter the price of the book: "))
            break
        except ValueError:
            print("Please, enter a valid price.")
    stock.append(stck)
    print(f"Producto {stck['name']} agregado al inventario.")

def search_book(stock):#This function makes a search possible
    if len (stock) == 0:
        print("The stock is empty, you can not search books.")
        return
    book_name = input("Enter the book name: ").lower() #That 'lower' makes uppercase letters in lowercas
    found = [book for book in stock if book['name'].lower() == book_name]
    if found:
        for book in found:
            print(f"Book found: Name: {book['name']}, Author: {book['author']},Category: {book['category']} amount: {book['amount']}, Price: ${book['price']:.2f}")#with that, you get all info of the book youre buying
            return book
        else:
            print("Book not found")
    input("Press ENTER to get back...")#with this, you can back to the menu


def update(stock):#with this function, you can update the order of the books what youre buying
    book = search_book(stock)
    if book:
        while True:#another validation
            try:
                new_amount= int(input(f"Enter the new amount for {book['name']}: "))#that line makes the magic, with this you can update it
                book['amount'] = new_amount
                print(f"Amount updated for {book['name']}.")
                break
            except ValueError:
                print("Please, enter a valid number for the amount.")
    while True:#same
        try:
            new_price= float(input(f"Enter new price for {book['name']}: "))
            book['price'] = new_price
            print(f"Price updated for {book['name']}.")
            break
        except ValueError:
            print("Please, enter a valid price.")
    input("Press ENTER to get back...")

def delete(stock):
    book = search_book(stock)
    while True:
        try:
            stock.remove(book)
            input(f"Press ENTER to confirm DELETE {book['name']} ")
            print(f"The book {book['name']} was deleted.")
            break
        except ValueError:
            print("Book not found.")
            break
    input("Press ENTER to get back...")

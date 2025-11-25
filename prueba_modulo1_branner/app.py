stock = [] #This is where customer information is storing

#Here I am importing customer services
from inventory_mng import (
    register_book, 
    search_book,
    update,
    delete

)

registration = []#This is where emplyee informtaion is storing
#Here I am importing employee services
from sales import (
    register_inventory,
    sales_consult,
    update_stock,
    register_sales,
)
#here im trying to import services for stadistics but I cant make it work :(
from reports import (
calculate_statistics,
range_books
)


def show_menu(stock):#that function is all the menu, where you can choose options to do something or end the program
    while True:
        print ("==================================")
        print ("=  Welcome to Branner`s Library  =")
        print ("==================================")
        print ("Choose an Option:")
        
        opcion = (input("1. Register Books\n2. Search Books\n3. Update Books\n4. Delete Books\
        \n5. Register new book\n6. Register sell \n7. validate available stock\n8. Update stock\
        \n9. Product range\n10. Calculate Income\n11 . Exit\n"))#with this, you can see the list and chose an option
        
        if opcion == "1":  
            print("Redirecting to register book...")
            register_book(stock)
        elif opcion == "2":
            print("Redirecting to the search engine...")
            search_book(stock)
        elif opcion =="3":
            print("Opening the updater...")
            update(stock)
        elif opcion =="4":
            print("Permissions to DELETE granted")
            delete(stock)
    #admin panel is where the employee makes everything
        elif opcion =="5":
            print("Registering book in inventory:")
            register_inventory(registration)
        elif opcion =="6":
            register_sales(registration)
            print("Registering sale...")
        elif opcion =="7":
            sales_consult(registration)
            print("Validating stock...")
        elif opcion =="8":
            print("Updating stock...")
            update_stock(registration)
        elif opcion =="9":
            print("Product range...")
            range_books(registration)
        elif opcion =="10":
            print("Calculating income...")
            calculate_statistics(registration)
        elif opcion =="11":
            print("Good bye!")
            exit()
        else:#if you chose an wrong option, you can try it again, so you will get this print in the screen
            print ("Invalid option. Please enter a valid option.: ") 

show_menu(stock)#with this you call the menu to see it
import Payment_Method as pay

menu_dict = {
    'coffee': 50,
    'pizza': 100,
    'burger': 50,
    'tea': 30,
    'noodle': 25
}

order_list = []

def display_menu():
    print("\nWelcome to the menu! ")
    for item, price in menu_dict.items():
        print(f"{item.title()} : Rs {price}")

def take_order():
    while True:
        print("\nWhat would you like to order? (type 'done' to finish) ")
        display_menu()
        item = input("Enter the order item: ").lower()
        
        if item == 'done':
            break
        
        elif item in menu_dict:
            order_list.append(item)
            print(f"{item.title()} added to your order!")
        else:
            print("Sorry, we don't have that item. Please try again.")
        
        print("Your current order:", [i.title() for i in order_list])

def calculate_bill():
    if not order_list:
        print("*" * 70)
        print("\nYou have not ordered anything yet.")
        return None
    
    total = 0
    print("\nYour Bill:")
    for item in order_list:
        print(f"{item.title()} : Rs {menu_dict[item]}")
        total += menu_dict[item]
    print(f"Total: Rs {total}")
    return total

def process_payment():
    total = calculate_bill()
    if total is None:
        return

    amount = int(input("Enter the amount to pay: "))
    
    payment_successful = pay.main()
    
    if payment_successful:  #import payment method using
        print("Payment successful. Thank you for your purchase!")
        ordered_list.clear()  # Clear the order list after successful payment
    else:
        print("Payment failed. Please try again.")
        
    # if amount < total:
    #     print(f"Insufficient amount. You need to pay Rs {total - amount} more.")
    # elif amount == total:
    #     print("Payment successful. Thank you for your visit!")
    #     order_list.clear()
    # else:
    #     print(f"Payment successful. Here is your change: Rs {amount - total}")
    #     order_list.clear()

def main():
    while True:
        print("\nWelcome to Desi Cafe :-")
        print("Choose any option: ")
        print("1. Menu")
        print("2. Order")
        print("3. Bill")
        print("4. Payment")
        print("5. Exit the cafe app")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            display_menu()
        elif choice == 2:
            take_order()
        elif choice == 3:
            calculate_bill()
        elif choice == 4:
            process_payment()
        elif choice == 5:
            print("Exiting the app. Use again!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
    
if __name__ == "__main__":
    main()

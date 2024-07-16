
def case_payment():
    print("Case Payment ")

def debite_card():
    card_no = input("Enter the card number: ")
    expiry_dt = input("Enter the expiry date: ")
    card_name = input("Card Holder name : ")
    cvv= input("CVV Number: ")
    print("Sucessfully Payment!")

def credite_card():
    card_no = input("Enter the card number: ")
    expiry_dt = input("Enter the expiry date: ")
    card_name = input("Card Holder name : ")
    cvv= input("CVV Number: ")
    print("Sucessfully Payment!")
    
def online_bank():
    pass

def upi_payment():
    upi_id = input("Enter the upi id : ")
    print("Sucessfully Payment!")

def main ():
    print("\nPayment Method")
    print("1. Case Payment")
    print("2. Debite Card")
    print("3. Credite Card")
    print("4. Online Banking")
    print("5. UPI Payment")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("You have selected Cash Payment")
        case_payment()
    elif choice == 2:
        print("You have selected Debite Card")
        debite_card()
    elif choice == 3 :
        print("You have selected Credite Card")
        credite_card()
    elif choice == 4 :
        print("You have selected  Online Banking")
        online_bank()
    elif choice == 5:
        print("You have selected UPI Payment")
        upi_payment()
    else:
        ("Invalid choice. Please choose a valid option.")

if __name__  == "__main__":
    main()
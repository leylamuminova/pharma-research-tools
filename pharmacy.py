import random

def legal_age(age):
    """Check for user's legal age"""
    if age < 18:
        print("Sorry, you are too young to use this software!")
        quit() #The code stops
    else:
        print("Great! Let's continue!") 
        
def create_account(name):
    """User can create an account"""
    account = input(f"Dear {name.capitalize()}, would you like to create an account so we can save your orders? ").lower()
    if account == "yes":
        letters = "1234567890qwertyuioplaksjdhfgzxcvbnml"
        password = ""
        for i in range(8):    
            new_str = random.choice(letters)
            password += new_str
        print(f"Your generated password: {name.upper() + password.upper()}") #Generate password that begins from user's inputed name
    
def tax_info(choice):
    """Provide user with relevant tax"""
    if choice == 1:
        tax = 7.25
        state = "Califonia"
    elif choice == 2:
        tax = 6.25
        state = "Texas"
    elif choice == 3:
        tax = 4.00
        state = "New York"
    elif choice == 4:
        tax = 6.00
        state = "Florida"
    elif choice == 5:
        tax = 6.25
        state = "Illinois"
    elif choice == 6:
        tax = 6.00
        state = "Pennsylvania"
    elif choice == 7:
        tax = 5.75
        state = "Ohio"
    elif choice == 8:
        tax = 4.00
        state = "Georgia"
    elif choice == 9:
        tax = 4.75
        state = "North Carolina"
    elif choice == 10:
        tax = 6.00
        state = "Michigan"
    elif choice == 11:
        tax = 6.63
        state = "New Jersey"
    elif choice == 12:
        tax = 5.30
        state = "Virginia"
    elif choice == 13:
        tax = 6.50
        state = "Washington"
    elif choice == 14:
        tax = 5.60
        state = 'Arizona'
    elif choice == 15:
        tax = 6.25
        state = "Massachusetts"
    elif choice == 16:
        tax = 7.00
        state = "Tennessee"
    elif choice == 17:
        tax = 7.00
        state = "Indiana"
    elif choice == 18:
        tax = 4.22
        state = "Missouri"
    elif choice == 19:
        tax = 6.00
        state = "Maryland"
    elif choice == 20:
        tax = 5.00
        state = "Wisconsin"
    elif choice == 21:
        tax = 2.90
        state = "Colorado"
    elif choice == 22:
        tax = 6.88
        state = "Minnesota"
    elif choice == 23:
        tax = 6.00
        state = "South Carolina"
    elif choice == 24:
        tax = 4.00
        state = "Alabama"
    elif choice == 25:
        tax = 6.00
        state = "Kentucky"
    elif choice == 26:
        tax = 0.00
        state = "Oregon"
    elif choice == 27:
        tax = 4.45
        state = "Louisiana"
    elif choice == 28:
        tax = 6.00
        state = "Iowa"
    elif choice == 29:
        tax = 6.35
        state = "Connecticut"
    elif choice == 30:
        tax = 4.85
        state = "Utah"
    else:
        print("Sorry, we only serve these 30 states right now!")
        quit()

    print(f"Great! You have chosen {state}. We wanted to remind you that prices for our medicine does not include your state sales tax. The sales tax in your state {tax}%.")

    return tax

def terminate_software():
    """Check if user wants to continue"""
    terminate = input("If you want to continue please enter YES: ").lower() #User's choice to stop
    if terminate == "yes":
        print("Great! Let's choose medicine now")
    else: 
        quit()

def med_choice():
    """User makes choice about intended purchase"""
    number_med = int(input('Please specify the quantity of medicine required: '))

    total_price = 0
    for i in range(1, number_med + 1):
        medicine = int(input(f"Medicine #{i}: "))

        if medicine == 1:
            price = 5.00
            total_price += price
        elif medicine == 2:
            price = 8.50
            total_price += price
        elif medicine == 3:
            price = 4.75
            total_price += price
        elif medicine == 4:
            price = 12.00
            total_price += price
        elif medicine == 5:
            price = 15.00
            total_price += price
        elif medicine == 6:
            price = 10.50
            total_price += price
        elif medicine == 7:
            price = 9.00
            total_price += price
        elif medicine == 8:
            price = 11.00
            total_price += price
        elif medicine == 9:
            price = 13.25
            total_price += price
        elif medicine == 10:
            price = 14.50
            total_price += price
        elif medicine == 11:
            price = 17.00
            total_price += price
        elif medicine == 12:
            price = 20.00
            total_price += price
        elif medicine == 13:
            price = 11.50
            total_price += price
        elif medicine == 14:
            price = 7.50
            total_price += price
        elif medicine == 15:
            price = 16.00
            total_price += price
        elif medicine == 16:
            price = 18.00
            total_price += price
        elif medicine == 17:
            price = 19.00
            total_price += price
        elif medicine == 18:
            price = 21.00
            total_price += price
        elif medicine == 19:
            price = 25.00
            total_price += price
        elif medicine == 20:
            price = 22.00
            total_price += price
        elif medicine == 21:
            price = 9.50
            total_price += price
        elif medicine == 22:
            price = 23.00
            total_price += price
        elif medicine == 23:
            price = 24.00
            total_price += price
        elif medicine == 24:
            price = 15.50
            total_price += price
        elif medicine == 25:
            price = 10.00
            total_price += price
        elif medicine == 26:
            price = 12.50
            total_price += price
        elif medicine == 27:
            price = 6.00
            total_price += price
        elif medicine == 28:
            price = 8.00
            total_price += price
        elif medicine == 29:
            price = 7.00
            total_price += price
        elif medicine == 30:
            price = 5.50
            total_price += price
        else:
            print("Invalid selection, please choose a valid medicine number next time.")    

        print(f"Price: ${price}")
    
    return total_price

def add_tax(tax, total_price):
    """Calculate final price including tax"""
    final_price_with_tax = total_price * (1 + (tax / 100)) #Adding tax

    print(f"Final price (including tax): ${final_price_with_tax:.2f}")

    return final_price_with_tax

def promo_code(final_price_with_tax, name):
    "Assign user with promocode if their purchase is done for more than $30"
    if final_price_with_tax >= 30.00:
        print("You are eligible for a discount promo code!")
        key = input("Please enter any string: ").lower()

        #Ensuring the key is the same length as the name
        if len(key) > len(name):
            key = key[:len(name)]  #Slicing the key to match the length of the name
        elif len(key) < len(name):
            if len(key) > 0:  #To avoid division by zero
                key = key * (len(name) // len(key)) + key[:len(name) % len(key)]
        else:
            key = name 

        new_cipher = ""
        for i in range(len(name)):
            n_pos = ord(name[i]) - ord("a")
            k_pos = ord(key[i]) - ord("a")
            cipher = (n_pos + k_pos) % 26
            new_cipher += chr(cipher + ord("a"))

        print(f"Your promo code: {new_cipher}")
        return new_cipher

def delivery_option(final_price_with_tax):
    """Providing user with delivery option"""
    delivery_option = (input("Do you want delivery? ")).lower()
    
    if delivery_option == "yes":
        print(f"Okay! Our delivery costs 30$ Your final price with delivery is ${final_price_with_tax + 30.00:.2f}")
        agreement = input("Doy you want to use still to use this option?: ")
        if agreement == "yes":
            address = input("Please enter the address: ")
        else:
            print(f"Fine! Your final price is ${final_price_with_tax:.2f}")

def main():
    name = input("Please enter your name?: ").lower()
    age = int(input("Please enter your age: "))
    legal_age(age)

    create_account(name)

    print(" 1. California", "2. Texas", "3. New York\n","4. Florida", "5. Illinois", "6. Pennsylvania\n",
    "7. Ohio", "8. Georgia", "9. North Carolina\n", "10. Michigan", "11. New Jersey", "12. Virginia\n",
    "13. Washington", "14. Arizona", "15. Massachusetts\n", "16. Tennessee", "17. Indiana", "18. Missouri\n",
    "19. Maryland", "20. Wisconsin", "21. Colorado\n", "22. Minnesota", "23. South Carolina", "24. Alabama\n",
    "25. Kentucky", "26. Oregon", "27. Louisiana\n", "28. Iowa", "29. Connecticut", "30. Utah")

    choice = int(input("Please choose your state: "))
    tax = tax_info(choice)
    terminate_software()

    print(" 1. Aspirin", "2. Ibuprofen", "3. Acetaminophen\n",
      "4. Amoxicillin", "5. Metformin", "6. Lisinopril\n",
      "7. Amlodipine", "8. Omeprazole", "9. Simvastatin\n",
      "10. Gabapentin", "11. Atorvastatin", "12. Levothyroxine\n",
      "13. Albuterol", "14. Prednisone", "15. Sertraline\n",
      "16. Fluoxetine", "17. Clonazepam", "18. Furosemide\n",
      "19. Hydrocodone", "20. Tramadol", "21. Doxycycline\n",
      "22. Citalopram", "23. Venlafaxine", "24. Metoprolol\n",
      "25. Montelukast", "26. Topiramate", "27. Diphenhydramine\n",
      "28. Ranitidine", "29. Cetirizine", "30. Tamsulosin")
    
    total_price = med_choice()
    final_price_with_tax = add_tax(tax, total_price)
    proomocode = promo_code(final_price_with_tax, name)
    delivery = delivery_option(final_price_with_tax)

    print("Thank you for your time with us!")


main()

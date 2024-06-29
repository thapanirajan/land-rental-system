import operation  # Importing the operation module which contains functions for renting and returning land

def nextLine():
    print("\n")  # Function to print a newline for better readability in the output

def header():
    nextLine()
    print("_"*190)  # Prints a line of underscores for header separation
    nextLine()
    print("\t\t\t\t\t\t\t\t\t\t Welcome To Techno Rental Property ")  # Welcome message
    print("\t\t\t\t\t\t\t\t\t\t------------------------------------")  # Decorative underline for the welcome message
    print("_"*190)  # Prints another line of underscores
    nextLine()
    
    print("\t\t\t\t\t\t\t\t\t\t\t","  Kathmandu")  # Prints location of the property
    nextLine()
    
def menu():
    nextLine()
    print("Press 1 to rent ")  # Option to rent land
    print("Press 2 to return")  # Option to return rented land
    print("Press 3 to exit")  # Option to exit the program
    nextLine()      

def main():
    header()  # Displays the header information
            
    valid = True  # Control variable for the while loop
    
    while valid:
        menu()  # Displays the menu options
        try:
            userInput = int(input("enter a number according to your requirement: "))  # Takes user input for menu selection

            if userInput == 1:
                operation.rentLandOperation()  # Calls the rentLandOperation function from the operation module
                
            elif userInput == 2:
                operation.returnLandOperation()  # Calls the returnLandOperation function from the operation module
                
            elif userInput == 3:
                nextLine()
                userExit = input("Are you sure you want to exit the system: y/n ").lower()  # Confirm exit
                if userExit == "y":
                    nextLine()
                    print("Exiting the program....")  # Exit message
                    nextLine()
                    break  # Breaks the loop to exit
                else:
                    print("continuing......")  # Continues the program if not exiting
                    
            else:
                print("Please enter a number from 1-3 according to your requirement")  # Error message for invalid option
                
        except ValueError:
            print("\nINVALID INPUT !! ")  # Error message for non-integer input
            
if __name__ == "__main__":
    main()  # Ensures the main function is called only when the script is executed directly

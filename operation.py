

import read
import write
import datetime

import sys

''' The function rentLandOperation is designed to handle the operation of renting land. It interacts with the user to gather information about the land they wish to rent, calculates the total price based on the duration of the rental, updates the land status to "Not Available", and generates an invoice for the transaction'''
def rentLandOperation():
    print("\n")
    print("-"*220)
    print("\t"*10+ "R E N T   L A N D ")
    print("-"*220)
    
    customer_name = input("\nEnter your name: ")
    customer_phone_number = input("\nEnter your phone number: ")
    
    
    invoice_list = []  # List to store invoice data
    grand_total_price = 0
    
    while True:
        available_land_dict = read.available_lands()
        print("\n")
        
        while True:
            kitta_id = int(input("Enter kitta number: ")) 
            if kitta_id in available_land_dict.keys():
                city = available_land_dict[kitta_id][0]
                direction = available_land_dict[kitta_id][1]
                anna = available_land_dict[kitta_id][2]
                break
            else:
                print("INVALID kitta number!!")
                print("\n")
        gg = True
        while gg:
            try:     
                month = int(input("Enter a number of months you want to rent land for: "))
                price = int(available_land_dict[kitta_id][3])
                total_price = month * price
                
                grand_total_price += total_price
                gg = False
            except(ValueError):
                print("INVALID INPUT!!")
                gg = True

        
        write.update_land(kitta_id)
        invoice_list.append((kitta_id,month,total_price,grand_total_price,city,direction,anna))
        more = input("Do you want more land? (y/n): ")
        if more.lower() == "n":
            break

    write.invoice(customer_name,customer_phone_number,invoice_list)

    print("\n")
    print("-"*220)
    print("\t"*10 +"I N V O I C E")
    print("-"*220)
    print("\n")
    print("Billed to: ")
    dateee = datetime.datetime.now()
    current_date = dateee.strftime("%b %d, %Y %H:%M:%S")
    print(f"Name: {customer_name}"+"\t"*20+"Date: "+f"{current_date}")
    print(f"Phone Number: {customer_phone_number}")
    print("-"*220)
    print("\n")
    print("-"*220)
    print("Kitta Number"+"\t"*4 +"  City"+"\t"*6+ "Direction"+"\t"*4+"Anna"+"\t"*5+"Month"+"\t"*5+"Total Price")
    print("-"*220)
    
    for item in invoice_list:
        # unpacking things from invoice list
        kitta_number = item[0]
        months = item[1]
        total_price = item[2]
        city = item[4]
        direction = item[5]
        anna = item[6]
        print(f"{kitta_number}"+"\t"*5+f"  {city}"+"\t"*5+f"{direction}"+"\t"*5+ f"{anna}"+"\t"*5+f"{months}"+"\t"*5+f"{total_price}")

    print("\n")
    print("\t"*23+"Grand Total:"+"\t"*2 ,grand_total_price)
    print("\t"*23+"-"*31)
    print("\n")
    print("T H A N K   Y O U ! ")
    print("\n")
    print("-"*220)
    return invoice_list


''' The function returnLandOperation is designed to handle the process of returning leased lands. It interacts with the user to collect necessary details, checks for the validity of the kitta number, calculates fines if the land is returned after the lease period, updates the land status, and generates an invoice for the return operation.'''
def returnLandOperation():
    print("\n")
    print("-"*220)
    print("\t"*10+ "R E T U R N  L A N D ")
    print("-"*220)
    invoiceForReturn= []
    total_fine = 0
    customer_name = input("\nEnter your name: ")
    customer_phone_number = input("\nEnter your phone number: ")

        
    
    while True:
        unavailable_land_dict= read.landsToReturn() #calls landsToReturn() function from read.py module
        print("\n")
        while True:
            try:
                print("\n")
                kitta = int(input("Enter kitta number : "))
                if kitta in unavailable_land_dict.keys():
                    city = unavailable_land_dict[kitta][0]
                    direction = unavailable_land_dict[kitta][1]
                    anna = unavailable_land_dict[kitta][2]
                    
                    for v in unavailable_land_dict.values():
                        amount = unavailable_land_dict[kitta][3]
                    break
                else:
                    print("\n")
                    print("invalid kitta number!! ")
            except(ValueError):
                print("INCORRECT INPUT !!!")
                
        loop_ = True
        while loop_:
            try:
                lease_month = int(input("Enter lease month: "))
                print("\n")
                month = int(input("Time between rental end and land return?  "))
                
                if month>lease_month:
                    exceed_month  =  month-lease_month
                    rate = 0.1*float(amount)
                    fine = exceed_month*rate
                    total_fine+=fine
                    print("return month exceeds the lease_month ")
                    print("\n")
                    print("Fine : "+ f"{fine}")
                    loop_ = False
                elif month == lease_month:
                    print("Thank you for returning ")
                    exceed_month = 0
                    rate = 0
                    fine = 0
                    total_fine = 0
                    break
                else:
                    print("\n")
                    print("You can not return the land before lease month ")
                    print("\n")
                    print("Exiting the system.......")
                    sys.exit()
            except ValueError:
                print("INCORRECT INPUT !!")
                
        write.update_return_landd(kitta) 
        
        #append land details to the list
        invoiceForReturn.append((kitta,exceed_month,rate,fine,total_fine,city,direction,anna))
        write.fine_invoice(customer_name,customer_phone_number,invoiceForReturn)
        more = input("Do you want to return more? y/n : ").lower()        
        if more == "n":
            break
        elif more != "y":
            print("INVALID RESPONSE!")
        
    
    # generating invoice to print in terminal 
    print("\n")
    print("-"*220)
    print("\t"*10 +"I N V O I C E")
    print("-"*220)
    print("\n")
    print("Billed to: ")
    dateee = datetime.datetime.now()
    current_date = dateee.strftime("%b %d, %Y %H:%M:%S")
    print(f"Name: {customer_name}"+"\t"*20+"Date: "+f"{current_date}")
    print(f"Phone Number: {customer_phone_number}")
    print("-"*220)
    print("\n")
    print("Kitta Number"+"\t"*4 +"city"+"\t"*4+"Direction"+"\t"*4+"Anna"+"\t"*4+"Extra month"+"\t"*4+ "Rate"+"\t"*3+"Fine")
    print("-"*220)
    for item in invoiceForReturn:
        #unpacking the items of list invoiceForReturn
        kittaNum = item[0]
        extraMonth = item[1]
        ratee = item[2]
        fine = item[3] 
        city = item[5]
        direction = item[6]
        anna = item[7]
        print(f"{kittaNum}"+"\t"*4+f"       {city}"+"\t"*3+f"   {direction}"+"\t"*4+f"{anna}"+"\t"*4+f"  {extraMonth}"+"\t"*4+f"     {ratee}"+"\t"*3+f"{fine}")

    print("-"*220)
    print("\n")
    print("\t"*23+"Total Fine :"+"\t"*2 ,total_fine)
    print("\t"*23+"-"*31)
    print("\n")
    print("T H A N K   Y O U ! ")
    print("\n")
    print("-"*220)
    return invoiceForReturn


    
    


import read
import datetime

''' The function update_land takes a single parameter kitta_id, which is used to identify a specific land record in a data dictionary. The function attempts to update the availability status of the land associated with kitta_id to "Not Available". It reads the existing data from a file using read.read_data(), modifies the relevant record in memory, and then writes the updated data back to the file. If the file is not found, it prints an error message.'''
def update_land(kitta_id):
    try:  
        status = " Not Available" 
        data_dict = read.read_data()
        with open("data.txt","w") as file:
            data_dict[kitta_id][4]= status  
            for key,value in data_dict.items():
                if key == kitta_id:
                    if value[4] == " Available":
                        value[4]= status 
                file.write(",".join(str(i) for i in value))
                file.write("\n")
    except(FileNotFoundError):
        print("FILE NOT FOUND !!!")
        

'''The function update_return_landd is designed to update the availability status of a land identified by kitta_id in a data file named data.txt. It sets the availability status to " Available" for the specified kitta_id.'''
def update_return_landd(kitta_id): 
    try: 
        stat = " Available" 
        data_dict = read.read_data()
        with open("data.txt","w") as file:
            data_dict[kitta_id][4]= stat
            for key,value in data_dict.items():
                if key == kitta_id:
                    if value[4] == " Not Available":
                        value[4]= stat
                    
                file.write(",".join(str(i) for i in value))
                file.write("\n")
    except(FileNotFoundError):
        print("FILE NOT FOUND !!")


''' The function invoice is defined to generate an invoice file for a customer based on the provided details. It accepts three parameters: customer_name, customer_phone_number, and invoice_list. The function formats and writes these details into a text file named after the customer, appending "txt" directly to the customer's name with a dot'''
def invoice(customer_name,customer_phone_number,invoice_list):
    dateee = datetime.datetime.now()
    current_date = dateee.strftime("%b %d, %Y %H:%M:%S")
    a = f"{customer_name}.txt"
    with open(a,"w") as f:
        f.write("-"*210)
        f.write("\n")
        f.write("\t"*13+"I N V O I C E ")
        f.write("\n")
        f.write("-"*210)
        f.write("\n")
        f.write("\n")
        f.write("Billed to: ")
        f.write("\n")
        f.write(f"Name: {customer_name}"+"\t"*20+"Date: "+f"{current_date}")
        f.write("\n")
        f.write(f"Phone Number: {customer_phone_number}")
        f.write("\n")
        f.write("\n")
        f.write("Kitta Number"+"\t"*4 +"City"+"\t"*4+ "Direction"+"\t"*4+"Anna"+"\t"*4+"Month"+"\t"*4+"Total Price")
        f.write("\n")
        f.write("-"*210)
        for item in invoice_list:
            f.write("\n")
            f.write("\n")
            kitta = item[0]
            month = item[1]
            total_price= item[2]
            grand_total_price= item[3]
            city = item[4]
            direction = item[5]
            anna = item[6]
            f.write(f"{kitta}"+"\t"*5+f"{city}"+"\t"*3+f"{direction}"+"\t"*5+ f"{anna}"+"\t"*4+f"{month}"+"\t"*4+f"{total_price}")
        f.write("\n")
        f.write("\n")
        f.write("\t"*19+"Grand Total:"+"\t"*2 +f"{grand_total_price}")
        f.write("\n")
        f.write("\t"*19+"-"*31)
        f.write("\n")
        f.write("\n")
        f.write("T H A N K   Y O U")
        f.write("\n")
        f.write("-"*210)
        
        
''' The function fine_invoice is defined to generate an invoice for fines related to late returns of land leases. It accepts three parameters: customer_Name, phoneNumber, and InvoiceReturn. The function formats and writes these details into a text file named after the customer, appending ".txt" to the customer's name. The invoice includes details such as the date, customer's name and phone number, and a detailed list of fines for each land lease item, including the kitta number, city, direction, anna, extra months, rate, and fine amount. The function concludes by writing the grand total of all fines and a thank you message at the end of the invoice.'''
def fine_invoice(customer_Name, phoneNumber,InvoiceReturn):
    dateee = datetime.datetime.now()
    current_date = dateee.strftime("%b %d, %Y %H:%M:%S")# formating date 
    file = f"{customer_Name}.txt"
    with open(file,"w") as file:
        file.write("-"*210)
        file.write("\n")
        file.write("\t"*13+"I N V O I C E ")
        file.write("\n")
        file.write("-"*210)
        file.write("\n")
        file.write("\n")
        file.write("Billed to: ")
        file.write("\n")
        file.write(f"Name: {customer_Name}"+"\t"*20+"Date: "+f"{current_date}")
        file.write("\n")
        file.write(f"Phone Number: {phoneNumber}")
        file.write("\n")
        file.write("\n")
        file.write("Kitta Number"+"\t"*4 +"city"+"\t"*4+"Direction"+"\t"*4+"Anna"+"\t"*3+"Extra month"+"\t"*4+ "Rate"+"\t"*3+"Fine")
        file.write("\n")
        file.write("-"*210)
        for item in InvoiceReturn:
            file.write("\n")
            file.write("\n")
            kitta = item[0]
            extra_Month = item[1]
            rate = item[2]
            fine= item[3]
            total_fine= item[4]
            city = item[5]
            direction = item[6]
            anna = item[7]
            file.write(f"{kitta}"+"\t"*4+f"       {city}"+"\t"*3+f"   {direction}"+"\t"*4+f"{anna}"+"\t"*3+f"  {extra_Month}"+"\t"*4+f"      {rate}"+"\t"*3+f"{fine}")

        file.write("\n")
        file.write("\n")
        file.write("\t"*22+"Grand Total:"+"\t"*2 +f"{total_fine}")
        file.write("\t"*23+"-"*31)
        file.write("\n")
        file.write("\n")
        file.write("T H A N K   Y O U")
        file.write("\n")
        file.write("-"*210)

    

       


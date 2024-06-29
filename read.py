
''' The function read_data() is designed to read data from a file named "data.txt" and store it in a dictionary. Each line of the file is expected to contain comma-separated values. The function initializes a dictionary data_dict and a starting kitta_Number of 100. For each line in the file, it strips any leading or trailing whitespace, splits the line by commas, and then adds these values to data_dict with the current kitta_Number as the key. After processing each line, kitta_Number is incremented by 1. If the file "data.txt" is not found, the function catches a FileNotFoundError and prints "FILE NOT FOUND!!". The function returns the populated dictionary.'''
def read_data():
    try:
        with open("data.txt","r") as file:
            data_dict = {}
            
            kitta_Number = 100
            for line in file:
                values = line.strip().split(",") # remove whitespaces and split line into list by commas.
                data_dict.update({kitta_Number:values}) # update kitta_Number and values as key and values.
                kitta_Number+=1
            return data_dict
    except(FileNotFoundError):
        print("FILE NOT FOUND!! ")

    

''' The function available_lands()  is designed to display and return a dictionary of lands that are available. It utilizes another function read_data() to fetch data from a file and process it into a dictionary where each key is a kitta_Number and the value is a list of properties related to the land.'''
def available_lands():
    data_dict = read_data()
    kitta_Number = read_data()
    available_land_dict = {}
    print("\n")
    print("AVAILABLE LANDS: ")
    print("-"*194)
    print("Kitta Number\t\t\t\tCity     \t\t\t\tLand Faced\t\t\t\tAana\t\t\t\tPrice\t\t\t    Availability")
    print("-"*194)
    for kitta_Number,values in data_dict.items():
        if " Available" in values:
            available_land_dict.update({kitta_Number:values})
            print(f"{kitta_Number}\t\t\t\t\t{values[0]}\t\t\t\t{values[1]}\t\t\t\t        {values[2]}\t\t\t       {values[3]}\t\t\t    {values[4]}")
    print("-"*194)
    return available_land_dict
        
        
''' The function landsToReturn()  is designed to identify and display lands that are not available. It uses data from the read_data() function, which reads and parses a file named data.txt into a dictionary where each key is a kitta_Number and the value is a list of attributes related to the land.'''
def landsToReturn():
    data_dict = read_data()
    kitta_Number = read_data()
    unavailable_land_dict = {}
    print("\n")
    print("Land you can return: ")
    print("-"*194)
    print("Kitta Number\t\t\t\tCity     \t\t\t\tLand Faced\t\t\t\tAana\t\t\t\tPrice\t\t\t    Availability")
    print("-"*194)
    for kitta_Number,values in data_dict.items():
        if " Not Available" in values:
            unavailable_land_dict.update({kitta_Number: values})
            print(f"{kitta_Number}\t\t\t\t\t{values[0]}\t\t\t\t{values[1]}\t\t\t\t        {values[2]}\t\t\t       {values[3]}\t\t\t    {values[4]}")
    print("-"*194)
    return unavailable_land_dict
        

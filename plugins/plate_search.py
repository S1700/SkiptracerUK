import requests
from bs4 import BeautifulSoup
from colorama import Fore
import re
import os

def plate():
    # Some global variables cuz python is a pain:
    global gearbox, vehicle_type, model, make, colour, engine_size, fuel_type, top_speed, zero_to_sixty, top_speed, bhp, reg_location

    os.system("clear")

    print("This is a script (made by me) that finds quite a lot of information about a car using the car plate.")
    print("Please type the UK car plate (make sure there are no spaces in the plate)")
    print("-")

    try:
        plate = str(input("OPTION: "))

    except KeyboardInterrupt:
        print("\nCanceled by user \n")

    plate_url = "https://www.rapidcarcheck.co.uk/results?RegPlate=" + plate
    plate_url2 = "https://www.checkcardetails.co.uk/cardetails/" + plate


    resp = requests.get(plate_url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    resp2 = requests.get(plate_url2)
    soup2 = BeautifulSoup(resp2.text, 'html.parser')

    p_lst = soup.select("p")
    d_lst = soup.select("div")
    tr_lst = soup2.select("tr")

    # General car plate info from URL1 and URL2

    for p in p_lst:
        match = re.match("Reg: (.*)", p.text)

        if match:
            reg = match.group(1)

    for tr in tr_lst:
        match = re.match("Registration Place(.*)", tr.text)

        if match:
            reg_location = match.group(1)
        else:
            reg_location = "Not Found"

    for p in p_lst:
        match = re.match("Make: (.*)", p.text)

        if match:
            make = match.group(1)
        else:
            make = "Not Found"

    for p in p_lst:
        match = re.match("Model: (.*)", p.text)

        if match:
            model = match.group(1)
        else:
            model = "Not Found"

    for p in p_lst:
        match = re.match("Vehicle Type: (.*)", p.text)

        if match:
            vehicle_type = match.group(1)
        else:
            vehicle_type = "Not Found"

    for p in p_lst:
        match = re.match("Engine Size: (.*)", p.text)

        if match:
            engine_size = match.group(1)
        else:
            engine_size = "Not Found"

    for tr in tr_lst:
        match = re.match("Transmission(.*)", tr.text)

        if match:
            transmission = match.group(1)
        else:
            transmission = "Not Found"

    for p in p_lst:
        match = re.match("Colour: (.*)", p.text)

        if match:
            colour = match.group(1)
        else:
            colour = "Not Found"

    for p in p_lst:
        match = re.match("Fuel Type: (.*)", p.text)

        if match:
            fuel_type = match.group(1)
        else:
            fuel_type = "Not Found"

    for p in p_lst:
        match = re.match("Top Speed: (.*)", p.text)

        if match:
            top_speed = match.group(1)
        else:
            top_speed = "Not Found"

    for p in p_lst:
        match = re.match("0-60 MPH: (.*)", p.text)

        if match:
            zero_to_sixty = match.group(1)
        else:
            zero_to_sixty = "Not Found"

    for p in p_lst:
        match = re.match("BHP: (.*)", p.text)

        if match:
            bhp = match.group(1)
        else:
            bhp = "Not Found"

    for p in p_lst:
        match = re.match("AVG Yearly Mileage: (.*)", p.text)

        if match:
            yearly_mileage = match.group(1)
        else:
            yearly_mileage = "Not Found"

    for p in p_lst:
        match = re.match("Vehicle Age: (.*)", p.text)

        if match:
            vehicle_age = match.group(1)
        else:
            vehicle_age = "Not Found"

    for p in p_lst:
        match = re.match("Year: (.*)", p.text)

        if match:
            registered_date = match.group(1)
        else:
            registered_date = "Not Found"

    for tr in tr_lst:
        match = re.match("Exported(.*)", tr.text)

        if match:
            exported = match.group(1)
        else:
            exported = "Not Found"

    os.system("clear")

    try:
        reg
    except NameError:
        print(Fore.RED + "\nCould not get info, check if the licence plate is correct.\n" + Fore.RESET)
        input(Fore.BLUE + "\nPress Enter to continue..." + Fore.RESET)
        plate()
    else:
        print(Fore.RED + "\nVehicle Information:\n" + Fore.RESET)
        print("Reg: " + reg)

        if reg_location == "N/A":
            print("Registration Location: " + Fore.RED + "Not Available" + Fore.RESET)
        else:
            print("Registration Location: " + reg_location)

        if make == "Not Available":
            print("Make: " + Fore.RED + "Not Available" + Fore.RESET)
        else:
            print("Make: " + make)
            
            if model == "Not Available":
                print("Model: " + Fore.RED + "Not Available" + Fore.RESET)
            else:
                print("Model: " + model)

                if vehicle_type == "Not Available":
                    print("Vehicle Type: " + Fore.RED + "Not Available" + Fore.RESET)
                else:
                    print("Vehicle Type: " + vehicle_type)

                if colour == "Not Available":
                    print("Colour: " + Fore.RED + "Not Available" + Fore.RESET)
                else:
                    print("Colour: " + colour)

                if engine_size == "Not Available":
                    print("Engine Size: " + Fore.RED + "Not Available" + Fore.RESET)
                else:
                    print("Engine Size: " + engine_size)

                if transmission == "N/A" or transmission == "":
                    print("Transmission: " + Fore.RED + "Not Available" + Fore.RESET)
                else:
                    print("Transmission: " + transmission)

                if fuel_type == "Not Available":
                    print("Fuel Type: " + Fore.RED + "Not Available" + Fore.RESET)
                else:
                    print("Fuel Type: " + fuel_type)

                if top_speed == "Not Available":
                    print("Top Speed: " + Fore.RED + "Not Available" + Fore.RESET)
                else:
                    print("Top Speed: " + top_speed)

                if zero_to_sixty == "Not Available":
                    print("0-60 MPH: " + Fore.RED + "Not Available" + Fore.RESET)
                else:
                    print("0-60 MPH: " + zero_to_sixty)

                if bhp == "Not Available":
                    print("BHP: " + Fore.RED + "Not Available" + Fore.RESET)
                else:
                    print("BHP: " + bhp)

                if yearly_mileage == "Not Available":
                    print("AVG Yearly Mileage: " + Fore.RED + "Not Available" + Fore.RESET)
                else:
                    print("AVG Yearly Mileage: " + yearly_mileage)
            
                if vehicle_age == "Not Available":
                    print("Vehicle Age: " + Fore.RED + "Not Available" + Fore.RESET)
                else:
                    print("Vehicle Age: " + vehicle_age)

                if registered_date == "Not Available":
                    print("Registered Year: " + Fore.RED + "Not Available" + Fore.RESET)
                else:
                    print("Registered Year: " + registered_date)

                if exported == "N/A":
                    print("Exported: " + Fore.RED + "Not Available" + Fore.RESET)
                else:
                    print("Exported: " + exported)


    print(Fore.RED + "\n\nMOT & Tax Information:\n" + Fore.RESET)

    for p in p_lst:
        match = re.match("Previous MOT Records: (.*)", p.text)

        if match:
            pre_mot_records = match.group(1)

    for p in p_lst:
        match = re.match("Last MOT Date: (.*)", p.text)

        if match:
            last_mot_date = match.group(1)

    for p in d_lst:
        match = re.match("MOT Due Date: (.*)", p.text.strip())

        if match:
            mot_due_date = match.group(1)

    for p in p_lst:
        match = re.match("TAX Due Date: (.*)", p.text)

        if match:
            tax_due_date = match.group(1)

    for p in p_lst:
        match = re.match("Emissions: (.*)", p.text)

        if match:
            emissions = match.group(1)

    print("Previous MOT Records: " + pre_mot_records)
    print("MOT Due Date: " + mot_due_date)
    print("Last MOT Date: " + last_mot_date)
    print("TAX Due Date: " + tax_due_date)
    print("Emissions: " + emissions)


    print(Fore.RED + "\n\nMileage Stats:\n" + Fore.RESET)

    for p in d_lst:
        match = re.match("Total Mileage Records: (.*)", p.text.strip())

        if match:
            total_mileage_rec = match.group(1)

    for p in p_lst:
        match = re.match("Last Record: (.*)", p.text)

        if match:
            last_mileage_rec = match.group(1)

    for p in p_lst:
        match = re.match("AVG Yearly Mileage: (.*)", p.text)

        if match:
            avg_yearly_mileage = match.group(1)

    for p in p_lst:
        match = re.match("Estimated Total Mileage Now: (.*)", p.text)

        if match:
            est_total_mileage = match.group(1)

    try:
        total_mileage_rec
    except NameError:
        print(Fore.RED + "Car hasn't got mileage stats yet" + Fore.RESET)
    else:
        print("Total Mileage Records: " + total_mileage_rec)
        print("Last Mileage Record: " + last_mileage_rec)
        print("AVG Yearly Mileage: " + avg_yearly_mileage)
        print("Estimated Total Mileage Now: " + est_total_mileage)

    print(Fore.GREEN + "\n\nDone!" + Fore.RESET)
    input(Fore.BLUE + "\nPress Enter to continue..." + Fore.RESET)


if __name__ == "__main__":
    plate()

import requests
from bs4 import BeautifulSoup
from colorama import Fore
import re
import os



os.system("clear")

print("""

\033[1;34;37m░██████╗██╗░░██╗██╗██████╗░████████╗██████╗░░█████╗░░█████╗░███████╗██████╗░
██╔════╝██║░██╔╝██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
╚█████╗░█████═╝░██║██████╔╝░░░██║░░░██████╔╝███████║██║░░╚═╝█████╗░░██████╔╝
░╚═══██╗██╔═██╗░██║██╔═══╝░░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔══╝░░██╔══██╗
██████╔╝██║░╚██╗██║██║░░░░░░░░██║░░░██║░░██║██║░░██║╚█████╔╝███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚═╝
                                                                Samuel20354

Please type the UK car plate in LOWERCASE (XXXXXX)

""")

try:                                                               
    num = str(input("OPTION : "))

    plate = (num)

except KeyboardInterrupt:
    print ("\nCanceled by user \n") 

url = "https://www.rapidcarcheck.co.uk/results?RegPlate="+plate

resp=requests.get(url)
soup=BeautifulSoup(resp.text,'html.parser')

p_lst = soup.select("p")
d_lst = soup.select("div")

for p in p_lst:
    match = re.match("Reg: (.*)",p.text)

    if match:
        reg = match.group(1)

for p in p_lst:
    match = re.match("Make: (.*)",p.text)

    if match:
        make = match.group(1)

for p in p_lst:
    match = re.match("Model: (.*)",p.text)

    if match:
        model = match.group(1)

for p in p_lst:
    match = re.match("Engine Size: (.*)",p.text)

    if match:
        engine_size = match.group(1)

for p in p_lst:
    match = re.match("Colour: (.*)",p.text)

    if match:
        colour = match.group(1)

for p in p_lst:
    match = re.match("Fuel Type: (.*)",p.text)

    if match:
        fuel_type = match.group(1)

for p in p_lst:
    match = re.match("Top Speed: (.*)",p.text)

    if match:
        top_speed = match.group(1)   
                
for p in p_lst:
    match = re.match("BHP: (.*)",p.text)

    if match:
        bhp = match.group(1)

for p in p_lst:
    match = re.match("AVG Yearly Mileage: (.*)",p.text)

    if match:
        yearly_mileage = match.group(1)

for p in p_lst:
    match = re.match("Vehicle Age: (.*)",p.text)

    if match:
        vehicle_age = match.group(1)

for p in p_lst:
    match = re.match("Registered Date: (.*)",p.text)

    if match:
        registered_date = match.group(1)


os.system("clear")  
print("""

\033[1;34;37m░██████╗██╗░░██╗██╗██████╗░████████╗██████╗░░█████╗░░█████╗░███████╗██████╗░
██╔════╝██║░██╔╝██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
╚█████╗░█████═╝░██║██████╔╝░░░██║░░░██████╔╝███████║██║░░╚═╝█████╗░░██████╔╝
░╚═══██╗██╔═██╗░██║██╔═══╝░░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔══╝░░██╔══██╗
██████╔╝██║░╚██╗██║██║░░░░░░░░██║░░░██║░░██║██║░░██║╚█████╔╝███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚═╝
                                                                Samuel20354

""")      
print("")
print(Fore.RED + "Vehicle Information:" + Fore.RESET)
print("")
print("Reg: "+(reg))
print("Make: "+(make))
print("Model: "+(model))
print("Colour: "+(colour))
print("Engine Size: "+(engine_size))
print("Feul Type: "+(fuel_type))
print("Top Speed: "+(top_speed))
print("BHP: "+(bhp))
print("AVG Yearly Mileage: "+(yearly_mileage))
print("Vehicle Age: "+(vehicle_age))
print("Registered Date: "+(registered_date))

print("")
print("")
print(Fore.RED + "MOT & Tax Infomation:" + Fore.RESET)
print("")



for p in p_lst:
    match = re.match("Previous MOT Records: (.*)",p.text)

    if match:
        pre_mot_records = match.group(1)

for p in p_lst:
    match = re.match("Last MOT Date: (.*)",p.text)

    if match:
        last_mot_date = match.group(1)

for p in d_lst:
  match = re.match("MOT Due Date: (.*)",p.text.strip())

  if match:
    mot_due_date = match.group(1)

for p in p_lst:
    match = re.match("TAX Due Date: (.*)",p.text)

    if match:
        tax_due_date = match.group(1)

for p in p_lst:
    match = re.match("Emissions: (.*)",p.text)

    if match:
        emissions = match.group(1)

  
print("Previous MOT Records: "+(pre_mot_records))
print("MOT Due Date: "+(mot_due_date))
print("Last MOT Date: "+(last_mot_date))
print("TAX Due Date: "+(tax_due_date))
print("Emissions: "+(emissions))

print("")
print("")
print(Fore.RED + "Mileage Stats:" + Fore.RESET)
print("")

for p in d_lst:
  match = re.match("Total Mileage Records: (.*)",p.text.strip())

  if match:
    total_mileage_rec = match.group(1)

for p in p_lst:
    match = re.match("Last Mileage Record: (.*)",p.text)

    if match:
        last_mileage_rec = match.group(1)

for p in p_lst:
    match = re.match("AVG Yearly Mileage: (.*)",p.text)

    if match:
        avg_yearly_mileage = match.group(1)

for p in p_lst:
    match = re.match("Estimated Total Mileage Now: (.*)",p.text)

    if match:
        est_total_mileage = match.group(1)

print("Total Mileage Records: "+(total_mileage_rec))
print("Last Mileage Record: "+(last_mileage_rec))
print("AVG Yearly Mileage: "+(avg_yearly_mileage))
print("Estimated Total Mileage Now: "+(est_total_mileage))

print("")
print("")
print(Fore.RED + "Latest MOT Records:" + Fore.RESET)
print("")
mot_lst = []
cur_dict = {}
for div in d_lst:
    date_match = re.match("TEST DATE(.*)",div.text.strip())
    if date_match:
        cur_dict["test date"] = date_match.group(1)

    result_match = re.match("RESULT(.*)",div.text.strip())
    if result_match:
        cur_dict["result"] = result_match.group(1)

    mileage_match = re.match("MILEAGE(.*)",div.text.strip())
    if mileage_match:
        if "test date" in cur_dict and "result" in cur_dict:
            cur_dict["mileage"] = mileage_match.group(1)
            mot_lst.append(cur_dict)
            cur_dict = {}

print(f'{"TEST DATE":^11} | {"RESULT":^6} | {"MILEAGE":^10} ')
for mot in mot_lst:
    print(f'{mot["test date"]:^11} | {mot["result"]:^6} | {mot["mileage"]:^10}')


print("")
print("")
print(Fore.GREEN + "Done!" + Fore.RESET)

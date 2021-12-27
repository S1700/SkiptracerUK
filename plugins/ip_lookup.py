import requests
from bs4 import BeautifulSoup
import json
from colorama import Fore
import sys
import time
import os


def lookup():

    os.system("clear")

    print("This is a script (made by me) that finds quite a lot of information about an IP address.")
    print("Remember you can never find someones exact location with their IP")
    print("Please type the target's IP address.")
    print("-")

    ip = input("IP address: ")
    print("-")

    agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    url = 'https://ipapi.co/' + ip + '/json'
    resp = requests.get(url, headers=agent)
    soup = BeautifulSoup(resp.text, 'html.parser')

    os.system("clear")


    print("\n")

    dict1 = json.loads(str(soup))
    print("")
    print(Fore.BLUE + "IP address info:" + Fore.RESET)
    print("")
    print(Fore.RED + "IP address: " + Fore.RESET + dict1["ip"])
    print(Fore.RED + "IP address version: " + Fore.RESET + dict1["version"])
    print(Fore.RED + "ASN: " + Fore.RESET + dict1["asn"])
    print(Fore.RED + "Organisation: " + Fore.RESET + dict1["org"])
    print("")
    print(Fore.BLUE + "IP address location info:" + Fore.RESET)
    print("")
    print(Fore.RED + "City: " + Fore.RESET + dict1["city"])
    print(Fore.RED + "Region: " + Fore.RESET + dict1["region"])
    print(Fore.RED + "Postal: " + Fore.RESET + dict1["postal"])
    latitude = str(dict1["latitude"])
    print(Fore.RED + "Latitude: " + Fore.RESET + latitude)
    longitude = str(dict1["longitude"])
    print(Fore.RED + "Longitude: " + Fore.RESET + longitude)
    print(Fore.RED + "Region Code: " + Fore.RESET + dict1["region_code"])
    print(Fore.RED + "Country: " + Fore.RESET + dict1["country"])
    print(Fore.RED + "Country name: " + Fore.RESET + dict1["country_name"])
    print(Fore.RED + "Country code: " + Fore.RESET + dict1["country_code"])
    print(Fore.RED + "Country code iso3: " + Fore.RESET + dict1["country_code_iso3"])
    print(Fore.RED + "Country capital: " + Fore.RESET + dict1["country_capital"])
    print(Fore.RED + "Country tld: " + Fore.RESET + dict1["country_tld"])
    print(Fore.RED + "Continent code: " + Fore.RESET + dict1["continent_code"])
    in_eu = str(dict1["in_eu"])
    print(Fore.RED + "In the EU: " + Fore.RESET + in_eu)
    country_area = str(dict1["country_area"])
    print(Fore.RED + "Country area: " + Fore.RESET + country_area)
    print("")
    print(Fore.BLUE + "Other info:" + Fore.RESET)
    print("")
    print(Fore.RED + "Timezone: " + Fore.RESET + dict1["timezone"])
    print(Fore.RED + "UTC offset: " + Fore.RESET + dict1["utc_offset"])
    print(Fore.RED + "Country calling code: " + Fore.RESET + dict1["country_calling_code"])
    print(Fore.RED + "Currency: " + Fore.RESET + dict1["currency"])
    print(Fore.RED + "Currency name: " + Fore.RESET + dict1["currency_name"])
    print(Fore.RED + "Languages: " + Fore.RESET + dict1["languages"])
    print(Fore.GREEN + "\nDone!\n" + Fore.RESET)
    input(Fore.BLUE + "Press Enter to continue..." + Fore.RESET)


if __name__ == "__main__":
    lookup()

import requests
import json
while True:
        city = input("Enter the name of city : ")
        url = f"https://api.weatherapi.com/v1/current.json?key=e2bb99e489c543ebb3634026230409&q={city}"
        if(city != "stop"):
            r = requests.get(url)
            # print(r.text)
            weatherDict = json.loads(r.text)
            print(weatherDict["current"]["temp_c"])
        else:
            print("Thank you for using.")
            break
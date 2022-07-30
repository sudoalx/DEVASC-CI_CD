from urllib import response
import requests

api_url = "https://ipapi.co/json/"


response = requests.get(api_url)
json_data = response.json()
json_status = response.status_code

if json_status == 200:
    print("\n****************************************************************")
    print("API reponse")
    print("API status code: " + str(json_status) +
          " = A successful route call.")
    print("****************************************************************\n")
    print("============ Datos de dirección IP ===========")
    print("IP Address:          " + str(json_data["ip"]))
    print("Version:             " + str(json_data["version"]))
    print("City:                " + str(json_data["city"]))
    print("Region:              " + str(json_data["region"]))
    print("Timezone:            " + str(json_data["timezone"]))
    print("Country name:        " + str(json_data["country_name"]))
    print("Country code:        " + str(json_data["country_code"]))
    print("Country capital:     " + str(json_data["country_capital"]))
    print("Continent code:      " + str(json_data["continent_code"]))
    print("Postal:              " + str(json_data["postal"]))
    print("Languages:           " + str(json_data["languages"]))
    print("Country area:        " + str(json_data["country_area"]))
    print("Country population:  " + str(json_data["country_population"]))
    print("ISP:                 " + str(json_data["org"]))
    print("Country calling code:" + str(json_data["country_calling_code"]))
    print("Currency name:       " + str(json_data["currency_name"]))
    print("=============================================")

elif json_status == 429:
    print("\n****************************************************************")
    print("Status Code: " + str(json_status) +
          "; Too many requests. " + str(json_data["reason"]) + ". Wait some time to make another request.\n" + str(json_data["message"]))
    print("****************************************************************\n")
    raise ValueError('Too many requests. ' +
                     str(json_data["reason"]) + '. Wait some time to make another request.')
else:
    print("\n************************************************************************")
    print("Status Code: " + str(json_status) + "; Refer to:")
    print("https://ipapi.co/api/" + str(json_data["message"]))
    print("************************************************************************\n")
    raise ValueError('Refer to: https://ipapi.co/api/')

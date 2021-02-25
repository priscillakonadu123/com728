import requests
resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()
for country in countries:
    if country["region"]==("Africa") or country["region"]==("Europe"):
        print(f"{country['name']} has a population of {country['population']}.{country['flag']}")






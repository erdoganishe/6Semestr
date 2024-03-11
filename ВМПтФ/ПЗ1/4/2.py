import requests


def get_data():
    url = 'https://restcountries.com/v3.1/all'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return None


def display_data(countries):
    if countries:
        for country in countries:
            print("Country:", country['name']['common'])
            if 'capital' in country:
                print("Capital:", country['capital'][0])
            else:
                print("Capital: Not available")
            print("Country Code:", country['cca3'])
            print("------------------------------------------")
    else:
        print("No data available")


if __name__ == "__main__":
    data = get_data()
    display_data(data)

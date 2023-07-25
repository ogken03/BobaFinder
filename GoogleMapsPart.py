import requests


class BobaSearch:


    def __init__(self,city,state,zip_code):
        api_key ='PLACE OWN KEY HERE -- Sorry :( --'
        self.search_boba_places(api_key, city, state, zip_code)


    def search_boba_places(self,api_key, city, state, zip_code):
        base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        query = f"boba places in {city}, {state} {zip_code}"
        params = {
            "key": api_key,
            "query": query
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if data.get("status") == "OK":
            results = data.get("results", [])
            for place in results:
                name = place["name"]
                formatted_address = place["formatted_address"]
                rating = place.get("rating", "N/A")
                price_level = place.get("price_level", "N/A")

                if price_level == 1:
                    price = "$"
                elif price_level == 2:
                    price = "$$"
                elif price_level == 3:
                    price = "$$$"
                else:
                    price = "N/A"

                print(f"Name: {name}")
                print(f"Address: {formatted_address}")
                print(f"Rating: {rating}"+"("+'\u2B50'+")")
                print(f"Price Level: "+price)
                print("=" * 30)
        else:
            print("Error:", data.get("status"))





import requests

def get_cities(skip: int=0, limit: int=50) -> list:
    url = f"http://climeat-api.safemoon.joshcorp.co/cities/?skip={skip}&limit={limit}"

    r = requests.get(url, verify=False)

    if r.status_code != 200:
        return None

    return r.json()

def get_city(city: str) -> dict:
    url = f"http://climeat-api.safemoon.joshcorp.co/cities/{city}"

    r = requests.get(url, verify=False)

    if r.status_code != 200:
        return None

    return r.json()

def get_meat_per_capita() -> list:
    #url = "http://localhost:8005/meatpercapita"
    url = "http://climeat-api.safemoon.joshcorp.co/meatpercapita"

    r = requests.get(url, verify=False)

    if r.status_code != 200:
        return None
    
    return r.json()

def get_meat_overconsumption() -> list:
    # url = "http://localhost:8005/meatoverconsumption"
    url = "http://climeat-api.safemoon.joshcorp.co/meatoverconsumption"

    r = requests.get(url, verify=False)

    if r.status_code != 200:
        return None
    
    return r.json()

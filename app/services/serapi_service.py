import requests
from app.config import Config

def fetch_tourist_spots(destination):
    url = "https://serpapi.com/search"
    params = {
        'q': f'tourist spots in {destination}',
        'api_key': Config.SERPAPI_KEY
    }
    response = requests.get(url, params=params)
    return response.json().get('organic_results', [])

def fetch_hotels(destination, budget, start_date, end_date):
    url = "https://serpapi.com/search"
    params = {
        'q': f'hotels in {destination} under {budget} from {start_date} to {end_date}',
        'api_key': Config.SERPAPI_KEY
    }
    response = requests.get(url, params=params)
    return response.json().get('organic_results', [])

def fetch_flights(source, destination, start_date):
    url = "https://serpapi.com/search"
    params = {
        'q': f'flights from {source} to {destination} on {start_date}',
        'api_key': Config.SERPAPI_KEY
    }
    response = requests.get(url, params=params)
    return response.json().get('organic_results', [])

def fetch_trains(source, destination, start_date):
    url = "https://serpapi.com/search"
    params = {
        'q': f'trains from {source} to {destination} on {start_date}',
        'api_key': Config.SERPAPI_KEY
    }
    response = requests.get(url, params=params)
    return response.json().get('organic_results', [])
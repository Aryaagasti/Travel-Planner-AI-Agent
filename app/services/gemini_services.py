import google.generativeai as genai
from app.config import Config

# Configure Gemini AI
genai.configure(api_key=Config.GEMINI_KEY)

def generate_travel_plan(source, destination, start_date, end_date, budget, interests, tourist_spots, hotels, flights, trains):
    """
    Generates a detailed travel plan based on user preferences.
    """
    # Extract names of tourist spots, hotels, flights, and trains
    tourist_spot_names = [spot.get('title', 'Unknown Spot') for spot in tourist_spots]
    hotel_names = [hotel.get('title', 'Unknown Hotel') for hotel in hotels]
    flight_names = [flight.get('title', 'Unknown Flight') for flight in flights]
    train_names = [train.get('title', 'Unknown Train') for train in trains]

    # Create the prompt for Gemini AI
    prompt = f'''
    Create a detailed and well-structured travel plan for a trip from {source} to {destination} from {start_date} to {end_date} with a budget of {budget}.
    Interests: {interests}.
    Tourist Spots: {", ".join(tourist_spot_names)}.
    Hotels: {", ".join(hotel_names)}.
    Flights: {", ".join(flight_names)}.
    Trains: {", ".join(train_names)}.

    The plan should include:
    - Overview of the destination
    - Itinerary with activities and timings
    - Hotel recommendations with booking links
    - Flight and train options with booking links
    - Budget breakdown
    - Tips for the traveler
    '''

    # Initialize the Gemini model
    model = genai.GenerativeModel('models/gemini-1.5-flash')  # Use 'gemini-pro' instead of 'gemini-1.5-flash'

    # Generate the travel plan
    response = model.generate_content(prompt)
    
    return response.text if response else "No travel plan generated."
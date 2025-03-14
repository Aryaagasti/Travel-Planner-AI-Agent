from flask import Blueprint, jsonify, request
from app.services.serapi_service import fetch_tourist_spots, fetch_hotels, fetch_flights, fetch_trains
import google.generativeai as genai
from app.services.gemini_services import generate_travel_plan

main_routes = Blueprint('main', __name__)

@main_routes.route('/api/generate-plan', methods=['POST'])
def generate_plan():
    data = request.json
    source = data.get('source')
    destination = data.get('destination')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    budget = data.get('budget')
    interests = data.get('interests')

    # Fetch tourist spots, hotels, flights, and trains
    tourist_spots = fetch_tourist_spots(destination)
    hotels = fetch_hotels(destination, budget, start_date, end_date)
    flights = fetch_flights(source, destination, start_date)
    trains = fetch_trains(source, destination, start_date)

    # Generate travel plan using Gemini
    travel_plan = generate_travel_plan(source, destination, start_date, end_date, budget, interests, tourist_spots, hotels, flights, trains)

    return jsonify({
        'travel_plan': travel_plan,
        'tourist_spots': tourist_spots,
        'hotels': hotels,
        'flights': flights,
        'trains': trains
    })
@main_routes.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')

    # Call Gemini AI to generate a response
    response = generate_chat_response(user_message)

    return jsonify({
        'response': response
    })

def generate_chat_response(user_message):
    # Initialize Gemini model
    model = genai.GenerativeModel('gemini-2.0-flash')

    # Define the system prompt for the chatbot
    system_prompt = """
    You are a friendly and helpful travel assistant. Your goal is to guide users with their travel plans, 
    answer their questions politely, and provide suggestions for destinations, hotels, flights, and activities.
    Be concise and helpful in your responses.
    """

    # Generate a response using Gemini AI
    response = model.generate_content([system_prompt, user_message])
    return response.text
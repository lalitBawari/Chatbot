from django.shortcuts import render
from django.http import JsonResponse

import random

patterns = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm good, thank you!", "I'm doing well.", "All is well."],
    "bye": ["Goodbye!", "Farewell!", "Take care!"],
    "what is your name": ["My name is ChatBot.", "You can call me ChatBot.", "I'm ChatBot, nice to meet you!"],
    "what is the time": ["I'm sorry, I don't have the ability to provide real-time information."],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!"],
    "thank you": ["You're welcome!", "No problem!", "My pleasure!"],
    "how old are you": ["I don't have an age. I'm a computer program!"],
    "what is the weather today": ["I'm sorry, I don't have access to real-time weather information."],
    "tell me about yourself": ["I am an AI chat bot designed to assist with various tasks.", "I'm here to help and provide information."],
    "how can I contact you": ["I'm an AI chat bot and don't have a direct contact method. But I'm here to assist you!"],
    "what is the meaning of life": ["The meaning of life is subjective and can vary from person to person."],
    "what is 2+2": ["2+2 is equal to 4."],
    "what is the capital of France": ["The capital of France is Paris."],
    "who is the first president of the United States": ["The first president of the United States is George Washington."],
    "what is the atomic number of oxygen": ["The atomic number of oxygen is 8."],
    "what is the boiling point of water": ["The boiling point of water is 100 degrees Celsius or 212 degrees Fahrenheit at sea level."],
    "tell me a random fact": ["Did you know that the world's tallest building is the Burj Khalifa in Dubai, United Arab Emirates?"],
    "what is the most abundant gas in the Earth's atmosphere": ["The most abundant gas in the Earth's atmosphere is nitrogen."],
    "what is the formula for the area of a circle": ["The formula for the area of a circle is A = π * r^2, where A is the area and r is the radius."],
    "what is the difference between Python 2 and Python 3": ["Python 2 and Python 3 are different versions of the Python programming language with various syntax and feature differences. Python 3 is the newer and recommended version for new projects."],
    "what is object-oriented programming": ["Object-oriented programming (OOP) is a programming paradigm that organizes data and code into reusable objects that can interact with each other."],
    "tell me a programming interview question": ["What is the difference between a list and a tuple in Python?"],
}


def generate_response(user_input):
    for pattern, responses in patterns.items():
        if pattern in user_input:
            return random.choice(responses)
    return "I'm sorry, I don't understand."


def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = generate_response(user_input)
        return JsonResponse({'response': response})
    return render(request, 'chatbot.html')

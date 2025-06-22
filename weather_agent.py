from openai import OpenAI
from dotenv import load_dotenv
import json
import requests


load_dotenv()


client = OpenAI()

import os

import os
import requests


import os
import requests

def get_weather(city: str):
    print("Tool called: get weather", city)

    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        condition = data["current"]["condition"]["text"]
        temp_c_raw = data["current"]["temp_c"]
        try:
            temp_c = float(temp_c_raw)
            return f"The weather in {city} is {condition} with a temperature of {temp_c:.1f} degree Celsius."
        except ValueError:
            return "Couldn't parse temperature properly."
    
    return "Something went wrong while fetching weather data."




available_tools = {
    'get_weather': {
        "fn": get_weather,  
        "description": "Takes a city name as input and returns the current weather as output for the city"
    }
}


system_prompt = f"""
You are a helpful AI Assistant who is specialized in resolving user queries.
You work on start, plan, action, observe mode.
For the given user query and available tools, plan the step by step execution,
based on the planning, select relevant tool from the available tools, and based 
on the tool selection you perform an action to call the tool.
Wait for the observation and based on that from the tool call resolve the query.

Rules:
- Follow the Output json format.
- Always perform one step at a time and wait for next input.
- Carefully analyze the user query

Output Json Format:
{{
    "step": "string",
    "content": "string", 
    "function": "The name of function if the step is action",
    "input": "The input parameter for the function"
}}

Available Tools:
- get_weather: Takes a city name as an input and returns the current weather for the city

Example:
User Query: What is the weather of new york?
Output: {{ "step": "plan", "content": "The user is interested in weather data of new york" }}
Output: {{ "step": "plan", "content": "From the available tools I should call get_weather" }}
Output: {{ "step": "action", "function": "get_weather", "input": "new york" }}
Output: {{ "step": "observe", "output": "12 Degree Cel" }}
Output: {{ "step": "output", "content": "The weather for new york seems to be 12 degrees." }}

Available tools:
- get_weather: Takes a city name as input and returns the current weather for the city
"""


messages = [
    { "role": "system", "content": system_prompt }
]

while True:
    user_query = input('> ')
    messages.append({ "role": "user", "content": user_query })
    
    while True:
        response = client.chat.completions.create(
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=messages
        )
        
        parsed_output = json.loads(response.choices[0].message.content)
        messages.append({ "role": "assistant", "content": json.dumps(parsed_output) })
        
        if parsed_output.get("step") == "plan":
            print(f"🧠: {parsed_output.get('content')}")
            continue
            
        if parsed_output.get("step") == "action":
            tool_name = parsed_output.get("function")
            tool_input = parsed_output.get("input")
            
            if available_tools.get(tool_name, False) != False:
                output = available_tools[tool_name].get("fn")(tool_input)
                messages.append({ "role": "user", "content": json.dumps({ "step": "observe", "output": output}) })
                continue
                
        if parsed_output.get("step") == "output":
            print(f"🤖: {parsed_output.get('content')}")
            break
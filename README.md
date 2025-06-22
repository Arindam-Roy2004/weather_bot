# 🌦️ Weather Bot – AI Assistant with Real-Time Weather Info

This is an AI-powered terminal chatbot that helps users get current weather updates using natural language. It uses **OpenAI GPT-4o** to understand queries and fetches weather data using the **WeatherAPI.com**.

---

## 🔧 Features

- 💬 Chat-based interaction with AI
- 🌍 Real-time weather information using WeatherAPI
- 🧠 Step-by-step planning using tool-calling logic
- 🔗 Easily extendable with more tools
- 🐍 Built with Python

---

## 📦 Tech Stack

- [Python 3.9+](https://www.python.org/)
- [OpenAI API](https://platform.openai.com/)
- [WeatherAPI.com](https://www.weatherapi.com/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Arindam-Roy2004/weather_bot.git
cd weather_bot
```

### 2. Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup `.env` File

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_api_key
WEATHER_API_KEY=your_weatherapi_key
```

---

## 🧪 Run the Project

```bash
python weather_agent.py
```

Then type something like:
```
> what's the weather in Silchar?
```

---

## 📁 Project Structure

```
weather_bot/
│
├── weather_agent.py         # Main script to run the assistant
├── requirements.txt         # Python dependencies
├── .env                     # Your API keys (not uploaded)
└── README.md                # Project info
```

---

## 🙋‍♂️ Author

Made with ❤️ by [Arindam Roy](https://github.com/Arindam-Roy2004)

# assistant/config.py
import os

# Load sensitive information from environment variables
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'cbc1be14fad0f0f8828a879cd20aac5b')

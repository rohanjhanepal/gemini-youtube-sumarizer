from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv() 
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

context = """Summarize this youtube video in points for ease of understanding, 
             highlighting important features. 
          """

model = genai.GenerativeModel('gemini-pro')

def generate_summary(prompt):
    if response := model.generate_content(f"{context} {prompt}"):
        return response.text
    return "Sorry, something went wrong. Please try again later."
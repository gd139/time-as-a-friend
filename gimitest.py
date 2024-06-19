# Import the Python SDK
import google.generativeai as genai
# Used to securely store your API key
#from google.colab import userdata

GOOGLE_API_KEY= "AIzaSyBe4XPGEjXmysot4rDMB8tmwDqy7QD1OtE" #userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("你能做什么？")
print(response.text)
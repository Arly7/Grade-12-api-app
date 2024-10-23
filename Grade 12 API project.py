import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyCwg59ci5AKCJC9aDLVWM4KAsB2Pq1XfAw")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Make me an recipe with disgns.")
print(response.text)
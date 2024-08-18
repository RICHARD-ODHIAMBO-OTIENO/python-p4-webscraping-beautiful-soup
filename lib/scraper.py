from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

# Save the HTML document
doc = BeautifulSoup(html.text, 'html.parser')

# Select the elements with the specified classes
courses = doc.select('.heading-60-black.color-black.mb-20')

# Print the content of each course element
for course in courses: 
  print(course.contents[0].strip())

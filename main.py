from bs4 import BeautifulSoup

with open("index.html", 'r') as file:
    html_str = file.read()

soup = BeautifulSoup(html_str, 'html.parser')

element = soup.body.next_element.next_element.next_element.next_element.get_text()

print(element)
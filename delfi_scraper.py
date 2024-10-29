from bs4 import BeautifulSoup
import requests
import csv

with open("delfi_naujienos.csv", 'w', encoding="UTF-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Title", "Category", "Link"])
    r = requests.get("https://www.delfi.lt/")
    soup = BeautifulSoup(r.text, 'html.parser')

    blocks = soup.find_all("article")
    for block in blocks:
        # print(block.prettify())
        try:
            print('-------------------------------------------')
            title = block.find(class_="headline-title").a.get_text().strip()
            try:
                category = block.find(class_="headline-labels__label").get_text().strip()
            except:
                category = ""
            link = block.find(class_="headline-title").a['href']
            if link.startswith("/"):
                link = "https://www.delfi.lt" + link
            print(title)
            print(category)
            print(link)
            csv_writer.writerow([title, category, link])
        except:
            ...
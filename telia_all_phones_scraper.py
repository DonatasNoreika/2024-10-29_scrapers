
from bs4 import BeautifulSoup
import requests
import csv


with open("telia_all_phone_telefonai.csv", 'w', encoding="UTF-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Phone model', "Price per month", "Full price"])
    page_num = 1

    while True:
        payload = {"page": page_num}
        r = requests.get("https://www.telia.lt/prekes/telefonai-ir-priedai/mobilieji-telefonai", params=payload)
        soup = BeautifulSoup(r.text, 'html.parser')
        page_num += 1

        blocks = soup.find_all(class_="mobiles-product-card card card__product card--anim js-product-compare-product")
        if not blocks:
            print("No more pages")
            break
        for block in blocks:
            phone_model = block.find(class_="mobiles-product-card__title js-open-product").get_text().strip()
            price_per_month = block.find_all(class_="mobiles-product-card__price-marker")[0].get_text().strip()
            price_per_month = price_per_month.replace(",", ".").replace(" €/mėn.", "")
            price = block.find_all(class_="mobiles-product-card__price-marker")[1].get_text().strip()
            price = price.replace(" ", "").replace(" €", "")
            csv_writer.writerow([phone_model, price_per_month, price])
            print(phone_model)
            print(price_per_month)
            print(price)
            print("----------------------------------")

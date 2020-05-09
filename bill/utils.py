import requests
from bs4 import BeautifulSoup
from .models import RetObject
from datetime import datetime


# THE AUTHENTIFICATION FUNCTION : login to the website
def authentification(email, password, session):
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,fr;q=0.8",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://app.factomos.com",
        "referer": "https://app.factomos.com/connexion",
        "x-requested-with": "XMLHttpRequest",
    }
    url = "https://app.factomos.com/controllers/app-pro/login-ajax.php"
    session.post(url, data="appAction=login&email=" + email + "&password=" + password, headers=headers)


# GET ALL INFORMATION OF THE HTML
def get_factures_elements(facture, email):
    soup = BeautifulSoup(facture.text, "html.parser")

    invoice = soup.findAll("td", class_="ITEM-NUMBER")
    date = soup.findAll("td", class_="ITEM-DATE")
    client_name = soup.findAll("td", class_="ITEM-CLIENT")
    total_ttc = soup.findAll("td", class_="ITEM-TOT-TTC")
    total_tva = soup.findAll("td", class_="ITEM-TOT-TVA")

    for i in range(len(invoice)):  # INSERT INTO THE SQL
        date_t = datetime.strptime(date[i].get_text().rstrip(), "%d/%m/%y")
        RetObject.objects.get_or_create(
            email=email,
            invoice_number=invoice[i].get_text().rstrip(),
            date=date_t.date(),
            client_name=client_name[i].get_text().rstrip(),
            total_ttc=total_ttc[i].get_text().rstrip(),
            total_vat=total_tva[i].get_text().rstrip()
        )


# THE MAIN FUNCTION
def back(email, password):
    session = requests.Session()
    authentification(email, password, session)
    factures = session.get("https://app.factomos.com/mes-factures")
    get_factures_elements(factures, email)

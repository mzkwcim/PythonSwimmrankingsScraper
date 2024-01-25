import requests
from bs4 import BeautifulSoup

url = ("https://www.swimrankings.net/index.php?page=rankingDetail&clubId=65773&gender=1"
       "&course=SCM&agegroup=0&stroke=0&season=-1")

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    time_text = soup.select('td.time')
    name_text = soup.select('td.fullname')

    for i in range(len(name_text)):
        if name_text[i].getText(strip=True) is not None:
            print(f"{str(name_text[i].getText(strip=True)).title().replace(',','')} {time_text[i].getText(strip=True)}")

else:
    print("Błąd przy pobieraniu strony. Status code:", response.status_code)

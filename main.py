import requests
from bs4 import BeautifulSoup


def contains(whole_text, text):
    if text in whole_text:
        return True
    else:
        return False


url = ("https://www.swimrankings.net/index.php?page=rankingDetail&clubId=65773&gender=1"
       "&course=SCM&agegroup=0&stroke=0&season=-1")

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    swimstyle_text = soup.select('td.swimstyle')
    time_text = soup.select('td.time')
    name_text = soup.select('td.fullname')

    for i in range(len(name_text)):
        if contains(swimstyle_text[i].getText(strip=True), "Lap") is False:
            print(f"{str(swimstyle_text[i].getText(strip=True)).title()} "
                  f"{str(name_text[i].getText(strip=True)).title().replace(',', '')} "
                  f"{time_text[i].getText(strip=True)}")

else:
    print("Error. Status code:", response.status_code)

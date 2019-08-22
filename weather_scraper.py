'''
This code pull data from the weather.com website and stores the current weather data in a dicstionary
'''

import requests
from bs4 import BeautifulSoup


def current_weather():
    page = requests.get("https://weather.com/en-IN/weather/today/l/97003:4:US")

    soup = BeautifulSoup(page.content,"html.parser")

    # Print all of the data from the Right Now field. 
    right_now = soup.find("div",{"class":"today_nowcard-sidecar component panel"})

    # Store data in a dictionary 
    data = {}
    for span_tag in right_now.find_all('th'):
        data[span_tag.text] = span_tag.next_sibling.text

    return data

    # for k, v in data.items():
    #     print(k, ": ", v)


if __name__ == "__main__":
    current_weather()

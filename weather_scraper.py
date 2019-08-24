'''
This code pull data from the weather.com website and stores the current weather data in a dictionary
'''

import requests
from bs4 import BeautifulSoup


def current_weather():
    page = requests.get("https://weather.com/en-IN/weather/today/l/97003:4:US")

    soup = BeautifulSoup(page.content,"html.parser")

    # Pull current weather and assign to variables
    weather_data = soup.find("div",{"class":"today_nowcard-section today_nowcard-condition"}).text
    temp = soup.find("div",{"today_nowcard-temp"}).text
    phrase = soup.find("div",{"today_nowcard-phrase"}).text
    feels = soup.find("div",{"today_nowcard-feels"}).text
    
    # hi = soup.find("div",{"deg-hilo-nowcard"})
    # lo = soup.find("div",{"today_nowcard-temp"})

    print("The current temperature is", temp, ".\n", "Today will be", phrase, ".\n", feels, ".")

    # Pull all of the data from the Right Now field. 
    right_now = soup.find("div",{"class":"today_nowcard-sidecar component panel"})

    # Store data in a dictionary 
    data = {}
    for span_tag in right_now.find_all('th'):
        data[span_tag.text] = span_tag.next_sibling.text

    # return data

    for k, v in data.items():
        print(k, ": ", v)


if __name__ == "__main__":
    current_weather()

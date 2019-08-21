import requests
from bs4 import BeautifulSoup

page = requests.get("https://weather.com/en-IN/weather/today/l/97003:4:US")

soup = BeautifulSoup(page.content,"html.parser")

all = soup.find("div",{"class":"today_nowcard-sidecar component panel"})

print(all)


'''
<div class="today_nowcard-sidecar component panel">
    <table>
        <caption>Right Now</caption>
        <tbody>
            <tr>
                <th>Wind</th>
                <td>
                    <span class="">WSW 10 km/h </span>
                </td>
            </tr>
            <tr>
                <th>Humidity</th>
                <td>
                    <span class="">
                        <span>63
                            <span class="Percentage__percentSymbol__2Q_AR">%</span>
                        </span>
                    </span>
                </td>
            </tr>
            <tr>
            <th>Dew Point</th>
                <td>
                    <span class="">12
                        <sup>°</sup>
                    </span>
                </td>
            </tr>
            <tr>
                <th>Pressure</th>
                <td>
                    <span class="">1,015.9 mb<!-- --> 
                        <span class="icon icon-font iconset-arrows icon-arrow-up-line" classname="icon icon-font iconset-arrows icon-arrow-up-line">
                        </span>
                    </span>
                </td>
            </tr>
            <tr>
                <th>Visibility</th>
                <td>
                    <span class="">16.1 km</span>
                </td>
            </tr>
        </tbody>
    </table>
</div>
'''
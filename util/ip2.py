import requests
import pandas as pd
from bs4 import BeautifulSoup

# 获取城市列表
url = "http://ip.yqie.com/china.aspx"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
city_list = soup.select("#site-nav > div:nth-child(3) > div > ul > li > a")
city_urls = [city["href"] for city in city_list]

# 爬取每个城市的IP地址范围
result = []
for city_url in city_urls:
    city_response = requests.get(city_url)
    city_soup = BeautifulSoup(city_response.content, "html.parser")
    ip_table = city_soup.select("#MainContent_dgIPAddress > tbody > tr")
    for tr in ip_table[1:]:
        td_list = tr.select("td")
        result.append({
            "start_ip": td_list[0].text.strip(),
            "end_ip": td_list[1].text.strip(),
            "location": td_list[2].text.strip()
        })

# 输出到Excel文件
df = pd.DataFrame(result)
df.to_excel("ip_address_list.xlsx", index=False)

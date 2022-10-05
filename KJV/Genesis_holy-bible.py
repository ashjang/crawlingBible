import requests
from bs4 import BeautifulSoup as bs
from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

interval = 2
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.holybible.or.kr/B_KJV/cgi/bibleftxt.php?VR=KJV&VL=1&CN=1&CV=99")
time.sleep(interval)

# 첫페이지 크롤링
page = requests.get("http://www.holybible.or.kr/B_KJV/cgi/bibleftxt.php?VR=KJV&VL=1&CN=1&CV=99")
soup = bs(page.text, "html.parser")

elements = soup.select('.tk4l')
# print(elements)
for i, element in enumerate(elements, 1):
    if i >= 2:
        print("{} {}".format(i-1, element.text))

page_num = 258
for index in range(49):
    # 페이지 이동
    driver.get("http://www.holybible.or.kr/B_KJV/cgi/bibleftxt.php?VR=4&CI={}&CV=99".format(page_num))
    time.sleep(1)
    driver.find_element('xpath','/html/body/table[3]/tbody/tr[2]/td/table/tbody/tr/td/input[2]').click()
    time.sleep(interval)

    # 현재 사이트 정보 가져오기
    curr_site = driver.current_url
    page = requests.get(curr_site)
    soup = bs(page.text, "html.parser")
    elements = soup.select('.tk4l')

    # 현사이트 크롤링
    for i, element in enumerate(elements, 1):
        if i >= 2:
            print("{} {}".format(i-1, element.text))
    
    # 다음 사이트를 위한 크롤링 설정
    page_num += 1
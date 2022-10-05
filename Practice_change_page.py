from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# 크롬창 열기
interval = 2
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.holybible.or.kr/B_KJV/cgi/bibleftxt.php?VR=KJV&VL=1&CN=1&CV=99")
time.sleep(interval)       # 페이지 넘길 경우 화면 불러오기 기다리는 시간: 2초

page_num = 258
driver.get("http://www.holybible.or.kr/B_KJV/cgi/bibleftxt.php?VR=4&CI={}&CV=99".format(page_num))
time.sleep(1)
driver.find_element('xpath','/html/body/table[3]/tbody/tr[2]/td/table/tbody/tr/td/input[2]').click()
time.sleep(interval)

# page_num += 1
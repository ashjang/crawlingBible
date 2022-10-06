import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import Workbook
import time

def main():
    # 크롬 열기
    driver = webdriver.Chrome(ChromeDriverManager().install())
    first_site = "http://www.holybible.or.kr/B_KJV/"
    driver.get(first_site)
    time.sleep(2)

    # 현재 사이트 정보 가져오기
    curr_site = driver.current_url
    page = requests.get(curr_site)
    soup = bs(page.text, "html.parser")
    elements = soup.select('.tk3 li a')

    # 성경(창,출,레...) 링크 및 title 뽑기
    address = []
    address_chapterNum = [
        50, 36, 12, 40, 10, 14,
        27, 13, 3, 36, 10, 9,
        34, 42, 1, 24, 150, 4,
        21, 31, 7, 4, 12, 3,
        31, 8, 3, 24, 66, 3,
        22, 52, 2, 25, 5, 14,
        29, 48, 4, 28, 6, 13,
        16, 4, 5, 24, 4, 5,
        21, 5, 3, 28, 3, 5,
        16, 6, 1, 16, 4, 1,
        13, 3, 1, 6, 1, 22
    ]
    address_urlNum = [
        257, 3585, 6913, 513, 3841, 7169,
        769, 4097, 7425, 1025, 4353, 7681,
        1281, 4609, 7937, 1537, 4865, 8193,
        1793, 5121, 8449, 2049, 5377, 8705,
        2305, 5633, 8961, 2561, 5889, 9217,
        2817, 6145, 9473, 3073, 6401, 9729,
        3329, 6657, 9985, 10241, 12545, 14849,
        10497, 12801, 15105, 10753, 13057, 15361,
        11009, 13313, 15617, 11265, 13569, 15873,
        11521, 13825, 16129, 11777, 14081, 16385,
        12033, 14337, 16641, 12289, 14593, 16897
    ]
    for i in elements:
        title = i.text
        title = title.replace(" ","")
        for ch in range(len(title)):
            if title[ch] == '(':
                title = title[0:ch]
                break
        address.append(title)
    # print(address)

    # 각 성경주소에 들어가서 
    for i in range(len(address)):
        url_Num = address_urlNum[i]
        # driver.get("http://www.holybible.or.kr/B_KJV/cgi/bibleftxt.php?VR=4&CI={}&CV=99".format(address_urlNum[i]))
        # time.sleep(1)
        # print("\n\n\n" + address[i])

        # 엑셀파일 생성
        excel = Workbook(write_only=True)
        excel_sheet = create_excel(address[i], excel)

        for chapter in range(address_chapterNum[i]):
            url = "http://www.holybible.or.kr/B_KJV/cgi/bibleftxt.php?VR=4&CI={}&CV=99"
            driver.get(url.format(url_Num))
            # print(url.format(url_Num))
            time.sleep(2)
            driver.find_element('xpath','/html/body/table[3]/tbody/tr[2]/td/table/tbody/tr/td/input[2]').click()
            
            # 현재 사이트: 각 장에서의 정보 가져오기
            curr_site = driver.current_url
            page = requests.get(curr_site)
            soup = bs(page.text, "html.parser")
            elements = soup.select('.tk4l')

            # 현사이트: 각 장의 구절들 크롤링
            for j, element in enumerate(elements, 1):
                if j >= 2:
                    row = [chapter+1, j-1, element.text]
                    excel_sheet.append(row)
                    # print("{} {}".format(j-1, element.text))
            url_Num += 1
        excel.save('{}.xlsx'.format(address[i]))


def create_excel(sheet_name, excel):
    # 엑셀파일
    excel_sheet = excel.create_sheet(sheet_name)
    columns = ['chapter', 'verse', 'word']
    excel_sheet.append(columns)
    return excel_sheet
    


main()
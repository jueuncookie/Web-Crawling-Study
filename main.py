
# This is a sample Python script.
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
#options.add_argument('--headless')        # Head-less 설정
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=options)

driver.get('https://korean.visitkorea.or.kr/main/main.do#home')

query_txt = input("키워드 입력")

element = driver.find_element(by=By.ID, value='inp_search').send_keys(query_txt)

driver.find_element(By.CLASS_NAME, "btn_search").click()


#학습목표 1: 텍스트를 추출하여 화면에 출력하기
#step4. 현재 페이지에 있는 내용을 화면에 출력하기

time.sleep(1)
full_html =  driver.page_source
soup = BeautifulSoup(full_html, "html.parser")
content_list = soup.find_all('ul', class_='list_thumType type1')

for i in content_list:
    print(i.text.strip());
    print("\n")
#
# #
# from bs4 import BeautifulSoup
# from selenium import webdriver
# import time
# import sys
#
# quary_txt = input('크롤링할 키워드')
# f_name = input('검색결과를 저장할 txt 파일 경로와 이름을 지정하세요(예c:\\data\\test_3.txt):')
# fc_name = input('검색결과를 저장할 txt 파일 경로와 이름을 지정하세요(예c:\\data\\test_3.txt):')
# fx_name=input('검색결과를 저장할 txt 파일 경로와 이름을 지정하세요(예c:\\data\\test_3.txt):')
# #step 2 크롬 들아ㅣ버를 사용해서 웹브라우저를 실행.
# path="c:/temp/chromedriver_240/chromedriver.exe"
# driver= webdriver.Chrome(path)
#
# driver.get('https://korean.visitkorea.or.kr/main/main.do#home')
# time.sleep(2)
#
# #step3. 검색창의 이름을 찾아서 검색어를 입력후 검색을 진행하기.
# driver.find_element_by_id("btnSearch").click()
# element=driver.find_element_by_id("inp_search")
# element.send.keys(quary_txt)
# driver.find_element_by_line_text("검색").click()

# #step4 현재 페이지에 있는 내용 화면에 출력하기
# time.sleep(1)
#
# html=driver.page_source
# soup= BeautifulSoup(html,'html.parser')
# content_list = soup.find('ui',  class_='list_thumType finon')
# print(content_list)
#
# #스텝5. 각 항목별로 분리하여 추출하고 변수에 할당하기
# no =1
# no2 = []
# content2=[]
# tags2=[]
#
# for i in content_list:
#     no2.append(no)
#     print('번호:'.no)
#
#     contents=i.find('div','tit').get_text()
#     content2.append(contents)
#     print('내용', contents.strip())
#
#     tag=i.find('p','tag').get_text()
#     tags2.append(tag)
#     print('태그:',tag.strip())
#     print('\n')
#
#     no+=1
#

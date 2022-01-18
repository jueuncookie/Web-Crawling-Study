

# Beutiful Soup활용 예제1

from bs4 import BeautifulSoup
ex1='''
<html>
    <head>
        <title> HTML 연습 </title>
    </head>
    <body>
        <p align="center"> text 1 </p>
        <img scr="c\\temp\\image\\솔개.png">
    </body>
</htnl> '''

soup = BeautifulSoup(ex1, 'html.parser')
soup.find('p')  # 파이썬 콘솔에서 실행가능 프린트 함수로 안묶으면 여기선 아무것도 안나옴,

soup.find('p', align='center')
soup.find('p', align='right')
soup.find('p', align='left')
soup.find_all(['p','img'])
txt = soup.find('p')
txt.string

txt2 = soup.find_all('p')
for i in txt2:
  print(i.get_text())   # i.string   =  get_text

  # select('.클래스명')
  # select('상위태그 > 중위태그 > 하위태그')
  # select('상위태그.클래스명  > 하위태그.클래스명')
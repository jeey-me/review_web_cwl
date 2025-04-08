import requests as req
from bs4 import BeautifulSoup as BS
import os

for page in range(100,106):
    url = "https://news.naver.com/section/100"


    # html 문서 요청
    html = req.get(url).text
    # print(type(html))

    # soup 객체 생성
    soup = BS(html, 'html.parser')
    # print(soup)
    # print(type(soup))

    # 뉴스 헤드라인을 싸고 있는 li요소의 셀렉터
    # #_SECTION_HEADLINE_LIST_gtf0r > li.sa_item

    # 셀렉터가 지정한 첫번째 요소값를 추출한다
    # datas = soup.select_one("ul.sa_list li.sa_item")

    # 셀렉터가 지정한 모든 요소값를 추출한다
    datas = soup.select(".sa_list li.sa_item")
    # print(datas)
    # print(len(datas))

    for data in datas:
        head_line = data.select_one('.sa_text_strong').get_text()
        img_tag = data.select_one('img[data-src]')
        # print(img_tag)
        if img_tag:
            img_src_value = img_tag['data-src']
            # print(img_src_value)
            print(img_src_value.split('?')[0])
        else :
            print("없습니다요")
        print(f"{head_line}; {img_tag}")
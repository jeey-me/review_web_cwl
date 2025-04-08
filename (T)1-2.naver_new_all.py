# https://news.naver.com/section/100

import requests as req
from bs4 import BeautifulSoup as BS
import os

# 뉴스 모든 페이지의 헤드라인 추출
# 함수로 만들어 보기
# csv 파일에 저장(헤드라인, 이미지url)

# https://news.naver.com/section/100
# https://news.naver.com/section/101
# https://news.naver.com/section/102
# https://news.naver.com/section/105

# 페이지마다 데이터를 크롤링해야됨(함수 정의)
def data_scraping(page):
    # 페이지마다 데이터를 크롤링해야됨(함수 정의)
    url = f"https://news.naver.com/section/{page}"

    # html 문서 요청
    html = req.get(url).text
    # print(type(html))

    # soup 객체 생성
    soup = BS(html, 'html.parser')
    # print(soup)
    # print(type(soup))
    # new head line을 싸고있는 li요소의 셀렉터

    # 셀렉터가 지정한 첫번째 요소 추출
    # datas = soup.select_one("ul.sa_list li.sa_item")

    # 셀렉터가 지정한 모든 요소 추출
    datas = soup.select(".sa_list li.sa_item")
    # print(datas)
    # print(type(datas))

    data_list = [] #한 페이지 안에 모든 데이터 저장하는 변수

    # 한 페이지 안에 있는 헤드라인&이미지url for문으로 추출
    for data in datas:
        row_data = []
        head_line = data.select_one('.sa_text_strong').get_text()
        img_tag = data.select_one('img[data-src]')

        if img_tag:
            img_src_value = img_tag['data-src']
            # print(img_src_value)
            img_tag = img_src_value.split('?')[0]
        else:
            print("data-src 속성을 가진 img 태그를 찾을 수 없습니다.")
            continue
        row_data.append(head_line)
        row_data.append(img_tag)
        # print(row_data)

        data_list.append(row_data)
        # print(data_list)
        # print("-"*50)
        # print(f"{head_line}, {img_tag}")
    return data_list

# 뉴스 페이지 반복
def main():
    total_list = []
    for page in range(100,106):
        # 페이지별 데이터 수집 함수 호출
        # print(f"{page} 입니다.")
        data_list = data_scraping(page)
        # print(data_list)
        # print("-"*50)
        # 페이지별 데이터 누적함
        total_list.extend(data_list)
        print(total_list)
# 파일로 저장하기 위해서는 data를 아래와 같은 튜플?형태로 해야된다
# !!!!!!! data = [[헤드라인1],[이미지URL1],[헤드라인2],[이미지URL2]] !!!!!!!!!

# 데이터 저장
    import csv 

    with open("news_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # 데이터 헤더 먼저 작성 
        writer.writerow(['헤드라인','이미지url'])
        # 전체 데이터를 한 번에 쓰기
        writer.writerows(total_list) # 여러 줄을 한꺼번에 쓰기(2차원리스트)

if __name__ == "__main__" : 
    main()
import requests as req
from bs4 import BeautifulSoup as BS
import csv
import os

# 저장할 CSV 파일 경로
save_path = 'save.csv'

# CSV 파일을 새로 열고 헤더 작성
with open(save_path, mode='w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['뉴스 제목', '이미지 링크'])

    # 섹션 번호 범위 반복 (100 ~ 105)
    for page in range(100, 106):
        url = f"https://news.naver.com/section/{page}"
        html = req.get(url).text
        soup = BS(html, 'html.parser')

        datas = soup.select(".sa_list li.sa_item")

        for data in datas:
            head_line_tag = data.select_one('.sa_text_strong')
            head_line = head_line_tag.get_text(strip=True) if head_line_tag else '제목 없음'

            img_tag = data.select_one('img[data-src]')
            img_src = img_tag['data-src'].split('?')[0] if img_tag else '이미지 없음'

            print(f"{head_line}; {img_src}")
            writer.writerow([head_line, img_src])

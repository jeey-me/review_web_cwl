import requests as req
from bs4 import BeautifulSoup as BS
import csv

def crawl_naver_news_section(section_code, save_path='save.csv'):
    """
    주어진 섹션 번호의 네이버 뉴스를 크롤링하여 save.csv에 저장하는 함수

    Parameters:
        section_code (int): 뉴스 섹션 번호 (예: 100은 정치, 101은 경제 등)
        save_path (str): 저장할 CSV 파일 경로
    """

    # CSV 파일 열기 (쓰기 모드)
    with open(save_path, mode='w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['뉴스 제목', '이미지 링크'])

        url = f"https://news.naver.com/section/{section_code}"
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

# ✅ 2. 함수 호출 (아래에 작성)
# 이 부분이 실제 실행되는 부분입니다!
crawl_naver_news_section(100)  # 정치 뉴스 저장
crawl_naver_news_section(101, save_path='economy_news.csv')  # 경제 뉴스 저장
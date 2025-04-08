from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager #웹드라이브 매니저 안에 크롬모듈 안에크롬 드라이버 클래스 사용 
import time

### 1. 크롬(웹) 드라이버 옵션 및 객체생성 ###

# 크롬브라우저 옵션
options = webdriver.ChromeOptions()
# options.add_argument('headless') # 브라우저 안띄우기
options.add_argument('lang=ko_KR') # KR 언어
options.add_experimental_option("excludeSwitches", ["enable-logging"])

#드라이버 통해 url 요청을 보냄 
chrome = webdriver.Chrome(options = options) 
url = "https://map.kakao.com/" 
chrome.get(url)

title = chrome.title
print(title) # 이 두줄은 time.sleep 으로 할때는 앞에 최대5초짜리로 할때는 뒤에 와야함.

#chrome.implicitly_wait(5) # 이후부터 요소가 나타날 때까지 최대 5초까지 기다림 (빠르게 동작하는경우 5초안되어도 다음거 진행)
time.sleep(5) # cpu 무조건 5초동안 슬립(제어를 멈춤)



### 2. 카카오 맵에서 자동 검색 기능 ###

# 검색 키워드 
place = "스타벅스"

# 검색어(place)입력
search_area = chrome.find_element(By.XPATH, '//*[@id="search.keyword.query"]') #x패스는 반드시 문자열로! 
search_area.send_keys(place) #검색어 입력

# 엔터키 키인
chrome.find_element(By.XPATH, '//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER)
time.sleep(5) # 자동으로 스타벅스 입력+검색 확인 



### 3. BS로 정보를 파싱해서 데이터 추출 ###
#현재 브라우저의 html 코드(DOM트리)를 html 변수에 저장
html = chrome.page_source

soup = BeautifulSoup(html,'html.parser')
# print(soup)
time.sleep(2)

# 장소의 li목록
# ul.placelist > li.PlaceItem 
# cafe_list = soup.select('.placelist .PlaceItem')
cafe_list = soup.select('ul.placelist li.clickArea')
# time.sleep(2)
print(len(cafe_list))

# 매장별 리뷰 저장
#{
# "매장1" : ["리뷰1", "리뷰2", ...],
# "매장2" : ["리뷰1", "리뷰2", ...],
# "매장3" : ["리뷰1", "리뷰2", ...],
# ...}
# place_reviews[매장1] = ["리뷰1", "리뷰2", ...]
place_reviews = {}
for i, cafe in enumerate(cafe_list):
    pass
    # print(i, cafe)
    # print("-"*50)
    # place_name = cafe.select_one('.head_item .link_name').text
    # print(place_name)



    ### 4. 리뷰 수집 ### 
    ## 1) 상세보기 클릭 
    #상세보기 키 xpath 패턴확인하기 -> li인덱스값 증가 
    # //*[@id="info.search.place.list"]/li[1]/div[5]/div[4]/a[1] 
    # //*[@id="info.search.place.list"]/li[2]/div[5]/div[4]/a[1]
    # //*[@id="info.search.place.list"]/li[3]/div[5]/div[4]/a[1] 
    # -> i값은 0부터 시작이지만 상세보기 인덱스 값은 1부터 시작 그러므로 f"{i+1}"로 만들어주기
     
    X_PATH = f'//*[@id="info.search.place.list"]/li[{i+1}]/div[5]/div[4]/a[1]'
    chrome.find_element(By.XPATH, X_PATH).send_keys(Keys.ENTER)
    time.sleep(2)
    chrome.switch_to.window(chrome.window_handles[-1]) #열려있는 마지막 탭으로 이동 
    #데이터수집
    time.sleep(2)
    chrome.close()
    chrome.switch_to.window(chrome.window_handles[0]) #열려있는 가장 처음 탭으로 이동
    time.sleep(2)


# 현재 열린 브라우저 창 닫기
chrome.close() 
# 모든 창 다 닫기
chrome.quit()
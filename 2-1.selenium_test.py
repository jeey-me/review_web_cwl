from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #웹드라이브 매니저 안에 크롬모듈 안에크롬 드라이버 클래스 사용 
import time
#실행할 때 마다 chrome 현재 브라우저와 동일한 버전의 드라이버 다운로드해서 메모리에 올려두고 드라이버 변수가 식별
# driver = webdriver.Chrome(ChromeDriverManager().install())#원래 이렇게 각각 해줘야하지만 자동화로 변한듯!? 하단처럼 하니까 됨

#드라이버 통해 url 요청을 보냄 
driver = webdriver.Chrome() 
url = "https://www.naver.com/"
driver.get(url)

title = driver.title
print(title)

driver.implicitly_wait(5) # 이후부터 요소가 나타날 때까지 최대 5초까지 기다림 (빠르게 동작하는경우 5초안되도 다음거 진행)
# time.sleep(5) # cpu 무조건 5초동안 슬립(제어를 멈춤)
driver.close() 
  



import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

#크롬 옵션
chrome_options=Options()
#Headless 브라우저 실행x
chrome_options.add_argument('--headless')
#브라우저 음소거
chrome_options.add_argument('--mute-audio')

#webdriver 설정(Chrome) - Headless 모드
#browser=webdriver.Chrome('c:/PythonApp/Section7/chromedriver.exe',options=chrome_option,)

#일반 모드
browser=webdriver.Chrome('c:/PythonApp/Section7/chromedriver.exe')

#크롬 브라우저 내부 대기
browser.implicitly_wait(5) #Second 단위

#브라우저 사이즈 조정
#minimize_window() 최소화
#maxmize_window() 최대화
browser.set_window_size(1000,1000)

#페이지 이동
browser.get('https://www.youtube.com/watch?v=jUlKTDr_uTY')

#5초 대기
time.sleep(5)

#html 포커스 주기 위한 코드
#Explicitly wait(명시적 대기)
WebDriverWait(browser,5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'html'))).send_keys(Keys.PAGE_DOWN)

#2초간 대기
time.sleep(2)

#페이지 내용
#print('Before Page Contents= {}'.format(browser.page_source))

#페이지 이동 시 새로운 데이터 수신 완료위한 대기 시간
scroll_pause_time=4

#현재 페이지 높이
last_height=browser.execute_script('return document.documentElement.scrollHeight')

print()

#모든 댓글 데이터가 렌더링 완료되기 까지 반복
while True:
    # 스크롤바 이동
    browser.execute_script('window.scrollTo(0,document.documentElement.scrollHeight)')

    #대기
    time.sleep(scroll_pause_time)

    # 스크롤바 이동 -> 새로운 데이터 랜더링 -> 현재 높이를 구한다.
    new_height=browser.execute_script('return document.documentElement.scrollHeight')

    # 새로운 렌더링 없으면 종료
    if new_height==last_height:
        break

    #높이 변경
    last_height=new_height

#bs4 초기화
soup=BeautifulSoup(browser.page_source,'html.parser')

#통계리스트
top_level=soup.select('div#menu-container yt-formatted-string#text')
#댓글리스트
comment=soup.select('ytd-comment-renderer#comment')

print('Total Like Count: {}'.format(top_level[0].text.strip()))
print('Total Dislike Count: {}'.format(top_level[1].text.strip()))

# Dom반복
for dom in comment:
    print()
    #이미지 URL 정보
    img_src=dom.select_one('#img').get('src')
    print('Thumbnail Image URLS : {}'.format(img_src if img_src else 'None'))
    #작성자
    print('Author : {}'.format(dom.select_one('#author-text > span').text.strip()))
    #댓글 본문
    print('Author : {}'.format(dom.select_one('#content-text').text.strip()))
    #좋아요
    print('Vote Positive : {}'.format(dom.select_one('#vote-count-middle').text.strip()))








#브라우저 종료
browser.quit()

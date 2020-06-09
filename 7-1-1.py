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



#브라우저 종료
browser.quit()

#모듈가져오기
#pip install selenium
from selenium import webdriver as wd
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
#명시적대기를위해
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time



#사전에 필요한 정보를 로드 -> 디비혹스 쉘, 배ㅣ파일에서 인자로 받아서 세팅
main_url = 'http://tour.interpark.com/'
keyword = '로마'

#드라이버
driver = wd.Chrome(ChromeDriverManager().install())

#차후 옵션부여하여 (프록시 , 에이전트 조작, 이미지를 배제)
#크롤링을 오래돌리면 -> 임시파일들이 쌓인다 -> temp파일삭제

#사이트 접속(get)
driver.get(main_url)

#검색창을 찾아서 검색어를 입력
#검색창 Id SearchGNBText
driver.find_element_by_id('SearchGNBText').send_keys(keyword)
#수정할경우 -> 뒤에 내용이 붙어버림 -> .clear() -> send_keys('내용')


#검색버튼 클릭
#driver.find_element_by_class_name('search-btn').click()
driver.find_element_by_css_selector('button.search-btn').click()

#잠시대기 ->페이지가 로드되고 나서 즉각적으로 데이터를 획득하는 행위는
#자제하시길,,

#명시적대기 -> 특정요소가 로케이트(발견될때까지)대기
try:
    element = WebDriverWait(driver, 10).until(
        #지정한 한개 요소가 올라오면 웨이트종료
        EC.presence_of_element_located((By.CLASS_NAME, 'oTravelBox'))
        )
except Exception as e:
    print('오류발생', e)
#암묵적대기 -> DOM이 다 로드될때까지 대기하고 먼저 로드되면 바로진행
#driver.implicitly_wait(10)

#해외여행 더보기클릭
driver.find_element_by_css_selector('body > div.container > div > div > div.panelZone > div.oTravelBox > ul > li.moreBtnWrap > button').click()
#절대적대기 -> time.sleep(10) 10초간 무조건 기다림 ->클라우드페어(디도스방어 솔루션)
#게시판에서 데이터를 가져올때
#데이터가 많으면 세션(혹시 로그인을 해서 접근되는 사이트일 경우)관리
#특정단위별 로그아웃 로그인 계속 시도
#특정 게시물이 사라질경우 -> 팝업발생(없는..)->팝업처리검토
#게시판 스캔시 -> 임계점을 모름!!
#게시판 스캔 -> 메타정보 획득 -> loop돌려서 일괄적으로 방문

#스크립트 실행
#onclick="searchModule.SetCategoryList(1, '')"
#16은 임시값 게시물 넘어갔을때 현상 확인차
for page in range(1, 2):
    try:
        #자바스크립트 구동하기
        driver.execute_script("searchModule.SetCategoryList(%s, '')" %page)
        time.sleep(2)

        #####
        #상품명 코멘트 기간1 기간2, 가격, 평점, 썸네일, 링크(실제상품 상세정보)
        boxItems = driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[5]/div[3]/ul/li')
        
        #li 하나 하나에 접근
        for li in boxItems:
            print('상품명', li.find_element_by_css_selector('h5.proTit').text)
            print('코멘트', li.find_element_by_css_selector('p.proSub').text)
            print('기간1', li.find_element_by_css_selector('div > div.info-row > div:nth-child(1) > p:nth-child(1)').text)
            print('기간2', li.find_element_by_css_selector('div > div.info-row > div:nth-child(1) > p:nth-child(2)').text)
            print('가격', li.find_element_by_css_selector('div > div.title-row > div:nth-child(2) > strong').text)
            print('평점', li.find_element_by_css_selector('div > div.info-row > div:nth-child(2) > p:nth-child(2)').text)
            print('썸네일', li.find_element_by_css_selector('a > img').get_attribute('src'))
            print('링크_상세정보', li.find_element_by_css_selector('a').get_attribute('onclick'))

    except Exception as e1:
        print('오류', e1)

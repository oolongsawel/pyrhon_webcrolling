#모듈가져오기
#pip install selenium
from selenium import webdriver as wd
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
#명시적대기를위해
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


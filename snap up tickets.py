import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


name = '邱柏鈞'
phone_number = '0975043570'
gmail = 'm231860820@gmail.com'


options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)
driver.implicitly_wait(0.8)
driver.get('https://inline.app/booking/-MeNcbDasiIykiow2Hfb:inline-live-2/-NLRXZWFIRJBhOSk1d_h')


#https://inline.app/booking/-MeNcbDasiIykiow2Hfb:inline-live-2/-N3JQxh1vIZe9tECk0Pg
lst_time = ['19', '17', '13', '11']#可選擇的時間
i = 0

while 1:
    try: 
        
        loc_button = WebDriverWait(driver, 1, 0.3).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-dmRaPn.GmkPw')))#找到定位的位置
        
        driver.execute_script('arguments[0].scrollIntoView()', loc_button)#下滑
        sleep(0.3)#等一下
        driver.execute_script('arguments[0].scrollIntoView()', loc_button)#下滑X2
        sleep(0.3)#再等一下

        
        while 1:
            
            try: 
                time_button = WebDriverWait(driver, 0.3).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-bZnhIo.gKUXOr.time-slot.time-slot-{}-00'.format(lst_time[i]))))
                break
            except:
                i += 1
            
            
        time_button.click() #點選時間按鈕
        print('訂位時間為{}點'.format(lst_time[i]))
        break
    except:
        driver.refresh() # 重整頁面
        i = 0
        
WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-gsnTZi.gFJNgI'))).click()#點擊完成預定

WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-kgflAQ.jyOblS'))).send_keys(name)#輸入姓名

WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-kgflAQ.bPketa'))).send_keys(phone_number)#輸入電話

WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-kgflAQ.efemDB'))).send_keys(gmail)#輸入電子信箱

WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-gsnTZi.eosxOG'))).click()#選擇聚會目的

#WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-gsnTZi.gFJNgI'))).click()#送出


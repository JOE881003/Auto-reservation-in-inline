import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


name = '邱筠臻'
phone_number = '0975043571'
gmail = 'm231860821@gmail.com'


options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument('--disable-images') 
driver = uc.Chrome(options=options)
#driver.implicitly_wait(0.8)
driver.get('https://inline.app/booking/-MeNcbDasiIykiow2Hfb:inline-live-2/-N3JQxh1vIZe9tECk0Pg')



#https://inline.app/booking/-MeNcbDasiIykiow2Hfb:inline-live-2/-N3JQxh1vIZe9tECk0Pg
lst_time = ['19', '17', '13', '11', '15']#可選擇的時間


while True:
    try: 
        i = 0

        while True:
            try: 
                time_button = WebDriverWait(driver, 0.1, 0.05).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-bZnhIo.gKUXOr.time-slot.time-slot-{}-00'.format(lst_time[i]))))
                driver.execute_script("arguments[0].click();", time_button)
                
                break
            except:
                if i == 4:
                    break
                i += 1

        driver.execute_script("arguments[0].scrollIntoView();", time_button) 
        WebDriverWait(driver,5, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-gsnTZi.gFJNgI'))).click()#點擊完成預定
        
        WebDriverWait(driver,5, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-kgflAQ.jyOblS'))).send_keys(name)#輸入姓名
        
        WebDriverWait(driver,5, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-kgflAQ.bPketa'))).send_keys(phone_number)#輸入電話
        
        WebDriverWait(driver,5, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-kgflAQ.efemDB'))).send_keys(gmail)#輸入電子信箱
        
        WebDriverWait(driver,5, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-gsnTZi.eosxOG'))).click()#選擇聚會目的
        
        #WebDriverWait(driver,5, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-gsnTZi.gFJNgI'))).click()#送出

        print('訂位時間為{}點'.format(lst_time[i]))
        
        sleep(4)
        
    except:

        driver.refresh() # 重整頁面
        



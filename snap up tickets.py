import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import monotonic, sleep


name = '邱筠臻'
phone_number = '0989320707'
gmail = 'm231860821@gmail.com'


options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument('--disable-images') 
driver = uc.Chrome(options=options)
#driver.implicitly_wait(0.8)
driver.get('https://inline.app/booking/-MeNcbDasiIykiow2Hfb:inline-live-2/-N3JQxh1vIZe9tECk0Pg')

zoom_out = "document.body.style.zoom='0.3'"


#https://inline.app/booking/-MeNcbDasiIykiow2Hfb:inline-live-2/-N3JQxh1vIZe9tECk0Pg
lst_time = ['19', '17', '13', '11', '15']#可選擇的時間

while 1:
    try: 
        i = 0
        #start = monotonic()
        #loc_button = WebDriverWait(driver, 1, 0.3).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-dmRaPn.GmkPw')))#找到定位的位置
        
        #driver.execute_script('arguments[0].scrollIntoView()', loc_button)#下滑
        #sleep(0.3)#等一下
        #driver.execute_script('arguments[0].scrollIntoView()', loc_button)#下滑X2
        #sleep(0.3)#再等一下
        
        #driver.find_element(By.CLASS_NAME, 'sc-bZnhIo.gKUXOr.time-slot.time-slot-19-00').click() #點選時間按鈕
        driver.execute_script(zoom_out)
        
        while 1:
            
            try: 
                #time_button = driver.find_element(By.CLASS_NAME, 'sc-bZnhIo.gKUXOr.time-slot.time-slot-{}-00'.format(lst_time[i]))
                time_button = WebDriverWait(driver, 0.2, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-bZnhIo.gKUXOr.time-slot.time-slot-{}-00'.format(lst_time[i]))))

                break
            except:
                if i == 4:
    
                    break
                i += 1

        time_button.click()

        '''
        try:
            time_button = driver.find_element(By.CLASS_NAME, 'sc-bZnhIo.gKUXOr.time-slot.time-slot-19-00')
            #WebDriverWait(driver, 0.3, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-bZnhIo.gKUXOr.time-slot.time-slot-19-00')))
        except:
            #print('19點沒位置')
            end = monotonic()
            pass
        
        try:
            time_button = driver.find_element(By.CLASS_NAME, 'sc-bZnhIo.gKUXOr.time-slot.time-slot-17-00')
            #WebDriverWait(driver, 0.3, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-bZnhIo.gKUXOr.time-slot.time-slot-17-00')))
        except:
            #print('17點沒位置')
            end = monotonic()
            pass
        
        try:
            time_button = driver.find_element(By.CLASS_NAME, 'sc-bZnhIo.gKUXOr.time-slot.time-slot-13-00')
            #WebDriverWait(driver, 0.3, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-bZnhIo.gKUXOr.time-slot.time-slot-13-00')))
        except:
            #print('13點沒位置')
            end = monotonic()
            pass
        
        try:
            time_button = driver.find_element(By.CLASS_NAME, 'sc-bZnhIo.gKUXOr.time-slot.time-slot-11z-00')
            #WebDriverWait(driver, 0.3, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-bZnhIo.gKUXOr.time-slot.time-slot-11-00')))
        except:
            #print('11點沒位置')
            end = monotonic()
            pass
        '''         
            

        #end = monotonic()
        
        WebDriverWait(driver,5, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-gsnTZi.gFJNgI'))).click()#點擊完成預定
        
        WebDriverWait(driver,5, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-kgflAQ.jyOblS'))).send_keys(name)#輸入姓名
        
        WebDriverWait(driver,5, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-kgflAQ.bPketa'))).send_keys(phone_number)#輸入電話
        
        WebDriverWait(driver,5, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-kgflAQ.efemDB'))).send_keys(gmail)#輸入電子信箱
        
        WebDriverWait(driver,5, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-gsnTZi.eosxOG'))).click()#選擇聚會目的
        
        WebDriverWait(driver,5, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-gsnTZi.gFJNgI'))).click()#送出
        
       #print(end - start)
        print('訂位時間為{}點'.format(lst_time[i]))
        
        sleep(4)
        #break
    except:
        #print(end - start)
        driver.refresh() # 重整頁面
        



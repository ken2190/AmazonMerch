import selenium
import my_gologin.gologinSelenium as gologinSelenium
import threading,time,datetime,os

import script.merchAmazon as my_script
import my_mongo.my_mongo as my_mongo
import data.data_amz_merch as data_amz_merch
import my_selenium.get as my_selenium_get
import my_selenium.generation as my_selenium_generation


def divide_chunks(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

def _run(profile,port):
    # Khởi tạo selenium
    (gl,driver)= gologinSelenium.createSelenium(profile,port)
    # Lấy data hàng ngày
    try:
        (data_info_upload,analyze,manage) = my_script.check_data_daily(my_selenium_get,driver,my_selenium_generation)
        data_amz_merch.updateManage(my_mongo,profile,manage)
        submitTime = datetime.datetime.now()
        dataSet = {
            "updateTime": submitTime,
            "publish": data_info_upload,
            "analyze": {},
        }
        data_amz_merch.updateAccount(my_mongo,profile["id"],dataSet)
        data_amz_merch.update_sale(my_mongo,analyze,profile["name"])
        print("time.sleep")
        time.sleep(1)
    except:
        dataSet = {"countError": profile['countError']+1}
        data_amz_merch.updateAccount(my_mongo,profile["id"],dataSet)

    driver.close()
    gl.stop()
    print("gl.stop()")

class myThread (threading.Thread):
    def __init__(self, profile,indexThread):
        threading.Thread.__init__(self)
        self.profile = profile
        self.indexThread = indexThread
        

    def run(self):
        _run(profile,5100+indexThread)

while True:
    # Lấy Danh sách Store
    dataStore = data_amz_merch.getAccount(my_mongo)
    # dataStore = data_amz_merch.getAccount(my_mongo,listStore=["M141"])
    #Chia danh sách thành nhóm 10 store
    dataStore = list(divide_chunks(dataStore,10))
    for indexList,list_data in enumerate(dataStore):
        threads=[]
        for indexThread,profile in enumerate(list_data):
            indexThread +=indexList*10
            thread = myThread(profile=profile,indexThread=indexThread)
            thread.start()
            threads.append(thread)

        for t in threads:
            t.join()
            print("Finish ",t.profile["id"])
        print("time.sleep(3)")
        time.sleep(3)
        # os.system("TASKKILL /F /IM chromedriver.exe")
    print("time.sleep(60)")
    time.sleep(60)
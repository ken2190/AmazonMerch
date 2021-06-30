import time,json,os
import requests,datetime

def get_time_query():
    time_from = datetime.datetime.now() - datetime.timedelta(weeks=6)
    now = datetime.datetime.now() - datetime.timedelta(hours=6)


    time_from_str = str(time_from.timestamp()).split(".")[0]+"000"
    time_to_str = str(now.timestamp()).split(".")[0]+"000"

    return (time_from_str,time_to_str)
    time_from = now.replace(hour=0, minute=0, second=0, microsecond=0)
    time_to = time_from + datetime.timedelta(days=1) -datetime.timedelta(milliseconds=1)

    time_from_str = str(time_from.timestamp()).replace(".0","000")
    time_to_str = str(time_to.timestamp()).replace(".","")

    return (time_from_str,time_to_str)

def get_product_status(driver, cookie,accountId):
    str_request = 'var data = \'{"pageSize":250,"pageToken":[],"sortField":"DateCreated","sortOrder":"Descending","status":["DRAFT","REVIEW","AMAZON_REJECTED","PUBLISHING","TIMED_OUT","PUBLISHED","DELETED"],"marketplaces":null,"productTypes":["PHONE_CASE_APPLE_IPHONE","PHONE_CASE_SAMSUNG_GALAXY","RAGLAN","ZIP_HOODIE","STANDARD_SWEATSHIRT","TOTE_BAG","STANDARD_TSHIRT","STANDARD_LONG_SLEEVE","VNECK","THROW_PILLOW","STANDARD_PULLOVER_HOODIE","PREMIUM_TSHIRT","POP_SOCKET","TANK_TOP"],"searchableOnRetail":null,"deleteReasonType":["","CONTENT_POLICY_VIOLATION","INACTIVE_NO_SALES"],"accountId":"'+str(accountId)+'","__type":"com.amazon.merch.search#FindListingsRequest"}\'; var xhr = new XMLHttpRequest(); xhr.withCredentials = true; xhr.addEventListener("readystatechange", function() { if(this.readyState === 4) { var response = xhr.response; document.querySelector(".manage-link [href=\'/manage/designs\']").setAttribute("data",response); } }); xhr.open("POST", "https://merch.amazon.com/api/ng-amazon/coral/com.amazon.merch.search.MerchSearchService/FindListings"); xhr.setRequestHeader("Accept", "application/json, text/plain, */*"); xhr.setRequestHeader("Cookie", \''+cookie+'\'); xhr.send(data);'
    driver.execute_script(str_request)
    print("execute_script manage")

def get_sale(driver, cookie):
    # (time_from_str,time_to_str) = get_time_query()
    (time_from_str,time_to_str) = get_time_query()
    str_request = 'var xhr = new XMLHttpRequest(); xhr.withCredentials = true; xhr.addEventListener("readystatechange", function() { if(this.readyState === 4) { console.log(this.responseText); } }); xhr.open("GET", "https://merch.amazon.com/api/reporting/purchases/report?marketplaceId=ATVPDKIKX0DER&marketplaceId=A1F83G8C2ARO7P&marketplaceId=A1PA6795UKMFR9&marketplaceId=A13V1IB3VIYZZH&marketplaceId=APJ6JRA9NG5V4&marketplaceId=A1RKKUPIHCS9HS&marketplaceId=A1VC38T7YXB528&fromDate='+str(time_from_str)+'&toDate='+str(time_to_str)+'"); xhr.setRequestHeader("Accept", "application/json, text/plain, */*"); xhr.setRequestHeader("Cookie", \''+cookie+'\'); xhr.send(); xhr.onreadystatechange = function() { if (xhr.readyState === 4) { var response = xhr.response; document.querySelector(".analyze-link [href=\'/analyze\']").setAttribute("data",response); } }'
    print("==\n",str_request,"\n")
    driver.execute_script(str_request)
    print("execute_script analyze")

def getPublishingEligibility(driver, cookie):
    str_request = 'var url = "https://merch.amazon.com/api/ng-amazon/coral/com.amazon.gear.merchandiseservice.GearMerchandiseService/GetPublishingEligibility"; var xhr = new XMLHttpRequest(); xhr.open("POST", url); xhr.setRequestHeader("Accept", "application/json, text/plain, */*"); xhr.setRequestHeader("Cookie", \''+cookie+'\'); xhr.onreadystatechange = function () { if (xhr.readyState === 4) { var response = xhr.response; document.querySelector(".dashboard-link [href=\'/dashboard\']").setAttribute("data", response); } }; var data = \'{"accountId":"504154114","__type":"com.amazon.gear.merchandiseservice#GetPublishingEligibilityInput"}\'; xhr.send(data);'
    driver.execute_script(str_request)
    print("execute_script")

def get_cookies(driver):
    return driver.get_cookies() 

def get_value(driver,css_selector,value_type):
    count_error = 0
    while True:
        try:
            count_error +=1
            if value_type == "text":
                print("Return 1")
                return driver.find_element_by_css_selector(css_selector).text
            elif value_type == "data":
                x = driver.find_element_by_css_selector(css_selector).get_attribute("data")
                if x is not None:
                    print("Return 2")
                    return x
                else:
                    time.sleep(2)
                    print("Sleep",count_error,"m")
                    if count_error > 60:
                        os.system("TASKKILL /F /IM chrome.exe")
                        print("exit 1")
                        exit(0)
                    pass                
        except:
            time.sleep(2)
            count_error +=1
            print("wait...1")
            

            if count_error > 20:
                print("Error ",css_selector,value_type)
                print("exit 1")
                exit(0)

def get_analyze(driver, my_selenium_generation):
    cookies = get_cookies(driver)
    cookies_str = my_selenium_generation.gen_str_cookies(cookies)
    get_sale(driver,cookies_str)
    analyze = get_value(driver,".analyze-link [href='/analyze']","data")

    print("Data Sale:\n\n",json.loads(analyze),"\n",driver,"\n==")
    return json.loads(analyze)

def get_manage(driver, my_selenium_generation,accountId):
    cookies = get_cookies(driver)
    cookies_str = my_selenium_generation.gen_str_cookies(cookies)
    get_product_status(driver,cookies_str,accountId)
    manage = get_value(driver,".manage-link [href=\'/manage/designs\']","data")
    return json.loads(manage)

    

import time,json

def get_info_upload(driver, my_selenium_get):
    driver.get("https://merch.amazon.com/dashboard")
    temp = {
        'AVAILABLE SUBMISSIONS': my_selenium_get.get_value(driver,"account-status-v2 div.card-body > div > div:nth-child(1) .progress-summary span","text"),
        'PUBLISHED PRODUCTS': my_selenium_get.get_value(driver,"account-status-v2 div.card-body > div > div:nth-child(2) .progress-summary span","text"),
        'TIER': my_selenium_get.get_value(driver,"account-status-v2 div.card-body > div > div:nth-child(3) .progress-summary span","text"),
    }
    return temp

def check_data_daily(my_selenium_get, driver,my_selenium_generation):
    #Get info_upload
    data_info_upload = get_info_upload(driver, my_selenium_get)
    print("data_info_upload",data_info_upload)

    #Get Sales
    analyze = my_selenium_get.get_analyze(driver,my_selenium_generation)

    accountId = get_account_id(driver)
    print("accountId",accountId)
    
    #Get Design Status
    manage = my_selenium_get.get_manage(driver,my_selenium_generation,accountId)
    return (data_info_upload,analyze,manage)

def get_account_id(driver):
    for item in driver.find_elements_by_css_selector("script"):
        if "accountId" in item.get_attribute('innerHTML'):
            accountIdText = item.get_attribute('innerHTML')
            accountId = accountIdText.split('accountId":')[1].split('"')[1]
            return accountId

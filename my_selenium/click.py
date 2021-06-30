import time

def click_elem(driver,css_selector,time_delay):
    count_error = 0
    count_error_submit = 0

    while True:
        try:
            #Check Error
            if css_selector == ".text-right.mt-large #submit-button" and driver.find_element_by_css_selector(".text-right.mt-large #submit-button").is_enabled() == False:
                time.sleep(time_delay)
                try:
                    count_error_submit+=1
                    alert = driver.find_element_by_css_selector("#STANDARD_TSHIRT-card .alert-danger div[ngatranslatedtext]").text
                    print("alert", alert)
                    if alert == "Please upload a valid PNG.":
                        return alert

                    if count_error_submit > 120:
                        return "Timeout Upload Image"
                except:
                    count_error +=1
                pass
            #Ready submit
            else:
                driver.find_element_by_css_selector(css_selector).click()
                time.sleep(time_delay)
                return 1
                          
        except:
            time.sleep(2)
            count_error +=1
            #print("wait...")
            pass
            try:
                driver.find_element_by_css_selector("#login_btn_e").click()
            except:
                pass


            if count_error > 3:
                print("Error ",css_selector)
                exit(0)
def click_item(driver,item):
    count_error = 0
    while True:
        try:
            item.click()
            time.sleep(1)
            return 1
                          
        except:
            time.sleep(2)
            count_error +=1
            print("wait...")
            pass

            if count_error > 20:
                print("Error ",item)
                exit(0)

def click_elems(driver,css_selector):
    count_error = 0
    while True:
        try:
            like = driver.find_element_by_css_selector(css_selector)
            for x in range(0,len(like)):
                if like[x].is_displayed():
                    click_item(driver,like[x])
            return 1
        except:
            time.sleep(2)
            count_error +=1
            print("wait...")
            pass

            if count_error > 20:
                print("Error ",css_selector)
                exit(0)

def click_color(driver,select_color):
    data_color_div = {
        "light_color" : ["baby_blue-checkbox","black-checkbox","heather_grey-checkbox","lemon-checkbox","orange-checkbox","pink-checkbox","red-checkbox","white-checkbox","grass-checkbox","silver-checkbox"],
        "dark_color" : ["asphalt-checkbox","heather_grey-checkbox","kelly_green-checkbox","navy-checkbox","purple-checkbox","brown-checkbox","dark_heather-checkbox","silver-checkbox","slate-checkbox"]
    }
    
    for color in data_color_div[select_color]:
        click_elem(driver,".color-group-container ."+color,0)



    


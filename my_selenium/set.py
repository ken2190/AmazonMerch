import time

def set_elem(driver,css_selector, type_action, value):
    count_error = 0
    while True:
        try:
             if type_action == "send_keys":
                driver.find_element_by_css_selector(css_selector).send_keys(value)
                return 1
            # if value_type == "text":
            #     return driver.find_element_by_css_selector(css_selector).text
            # elif value_type == "data":
            #     x = driver.find_element_by_css_selector(css_selector).get_attribute("data")
            #     if x is not None:
            #         return x
            #     else:
            #         time.sleep(2)
            #         pass                
        except:
            time.sleep(2)
            count_error +=1
            print("wait...")
            pass

            if count_error > 4:
                print("Error ",css_selector,type_action)
                exit(0)

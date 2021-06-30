import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from my_gologin.gologin import GoLogin

def createSelenium2(profile,port):
    profile_id = profile["id"]
    print("profile_id",profile_id,"==",profile["name"])
    gl=None

    if platform == "linux" or platform == "linux2":
        chrome_driver_path = './chromedriver'
    elif platform == "darwin":
        chrome_driver_path = './mac/chromedriver'
    elif platform == "win32":
        chrome_driver_path = './my_gologin/chromedriver'
        

    # debugger_address = gl.start()
    debugger_address ="127.0.0.1:"+str(port)
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", debugger_address)
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    # driver.minimize_window()
    # driver.maximize_window()

    return (gl,driver)

def createSelenium(profile,port):
    profile_id = profile["id"]
    print("profile_id",profile_id,"==",profile["name"])
    gl = GoLogin({
        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MDZkN2JiZDM1ZDlmNjdiNTA4NTFkMDUiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MDZlYjY5ODhmMzVmZDBiNDlhOTIyOWYifQ.tAKGj3135i7pAYbALnbWqGlWbvqvzWCX666-DTQhy3U',
        'profile_id': str(profile_id),
        'port':port
        })

    if platform == "linux" or platform == "linux2":
        chrome_driver_path = './chromedriver'
    elif platform == "darwin":
        chrome_driver_path = './mac/chromedriver'
    elif platform == "win32":
        chrome_driver_path = './my_gologin/chromedriver'
        

    debugger_address = gl.start()
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", debugger_address)
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    # driver.minimize_window()
    driver.maximize_window()
    return (gl,driver)

import data.data_merchImport as data_merchImport
import script.merchImportAmazon as my_script
import my_mongo.my_mongo as my_mongo
import my_gologin.gologinSelenium as gologinSelenium

import my_selenium.click as my_selenium_click
import my_selenium.set as my_selenium_set

import os,time

def _run_product_data(profile,port,product):
    # Khởi tạo selenium
    try:
        (gl,driver)= gologinSelenium.createSelenium(profile,port)
    except:
        statusImportProduct = "Error Gologin Profile"
        data_merchImport.upadteProduct(my_mongo,{"_id":product["_id"]},{"status": statusImportProduct})
        print("Update",{"_id":product["_id"]},{"status": statusImportProduct})
        return None
    rootPath = str(os.getcwd()).replace("\\","/")

    statusImportProduct = my_script.importProductMerch(driver,product,rootPath,my_selenium_click,my_selenium_set)
    data_merchImport.upadteProduct(my_mongo,{"_id":product["_id"]},{"status": statusImportProduct})
    print("Update",{"_id":product["_id"]},{"status": statusImportProduct})
    driver.close()
    gl.stop()
    print("gl.stop()")

query = {}
data_products = data_merchImport.getProducts(my_mongo,query=query)

for index_product,product in enumerate(data_products):
    print(index_product+1,"/",len(data_products),product['_id'],product['store_name'])

    profile = data_merchImport.getIdByNameAccount(my_mongo,product['store_name'])
    print(profile)

    port = 8000
    _run_product_data(profile,port,product)

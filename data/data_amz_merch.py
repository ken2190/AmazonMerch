import datetime
#GET
def insertAccountBigo(my_mongo,list_products):
    myclient = my_mongo.create_mongo()
    my_mongo.insert(myclient,"Bigo","Account",list_products,multi=True)
    my_mongo.close_mongo(myclient)

def getAccountBigo(my_mongo,listStore=None,limit=0):
    myclient = my_mongo.create_mongo()
    if listStore is None:
        query = {
        }
    else:
        query = {
            "name": {"$in":listStore},
        }

    # query = {}
    data = my_mongo.find(myclient,"Bigo","Account",query,{"name":1,"id":1,"_id":0,"email":1},limit=limit)
    # data = my_mongo.find(myclient,"amz_merch","Account",{"status":"Active","name":'M75',"dataTimeZone":{"$exists":1}},{"name":1,"id":1,"_id":0,"dataTimeZone":1})
    my_mongo.close_mongo(myclient)

    return data

def getAccount(my_mongo,listStore=None):
    myclient = my_mongo.create_mongo()
    if listStore is None:
        query = {
            # "countError":{"$lt": 20},
            "status":"Active",
        }
    else:
        query = {
            "name": {"$in":listStore},
            # "countError":{"$lt": 20},
            "status":"Active",
        }
    data = my_mongo.find(myclient,"amz_merch","Account",query,{"name":1,"id":1,"_id":0,"countError":1})
    # data = my_mongo.find(myclient,"amz_merch","Account",{"status":"Active","name":'M75',"dataTimeZone":{"$exists":1}},{"name":1,"id":1,"_id":0,"dataTimeZone":1})
    my_mongo.close_mongo(myclient)

    return data

def getProducts(my_mongo,limit=0):
    myclient = my_mongo.create_mongo()
    data = my_mongo.find(myclient,"amz_merch","Product",{"status":"New"},{},limit=limit)
    my_mongo.close_mongo(myclient)

    return data

def getProductsByStore(my_mongo,store_name):
    myclient = my_mongo.create_mongo()
    data = my_mongo.find(myclient,"amz_merch","Product",{"store_name":store_name},{"_id":0,"title":1,"store_name":1})
    my_mongo.close_mongo(myclient)

    return data

def getIdByNameAccount(my_mongo,name):
    myclient = my_mongo.create_mongo()
    data = my_mongo.find(myclient,"amz_merch","Account",{"name":name,"dataTimeZone":{"$exists":1}},{"name":1,"id":1,"_id":0,"dataTimeZone":1},limit=1)
    my_mongo.close_mongo(myclient)
    if len(data) == 0:
        return None
    else:
        return data[0]

#SET
def updateAccount(my_mongo,profile_id,dataSet):
    myclient = my_mongo.create_mongo()
    my_mongo.update(myclient,"amz_merch","Account",{"id":profile_id},dataSet)
    my_mongo.close_mongo(myclient)

def setPublish(my_mongo,profile_id,data_publish):
    myclient = my_mongo.create_mongo()
    my_mongo.update(myclient,"amz_merch","Account",{"id":profile_id},{"publish":data_publish})
    my_mongo.close_mongo(myclient)

def setAnalyze(my_mongo,profile_id,analyze):
    myclient = my_mongo.create_mongo()
    my_mongo.update(myclient,"amz_merch","Account",{"id":profile_id},{"analyze":analyze})
    my_mongo.close_mongo(myclient)

def upadteProduct(my_mongo,query,dataSet):
    myclient = my_mongo.create_mongo()
    my_mongo.update(myclient,"amz_merch","Product",query,dataSet)
    my_mongo.close_mongo(myclient)

def update_sale(my_mongo,analyze,storeName):
    myclient = my_mongo.create_mongo()
    a = list(analyze.keys())
    if len(a)> 0:
        a = a[0]
        list_items = analyze[a]
        for item in list_items:
            dataSet = {
                'revenue': item['revenue']['value'],
                'revenueExclTax': item['revenueExclTax']['value'],
                'royalties': item['royalties']['value'],
                'unitsSold': item['unitsSold'],
                'unitsReturned': item['unitsReturned'],
                'title': item['asinName'],
                'productType': item['productType'],
                'variationInfo': item['variationInfo'],
                'asin': item['asin'],
                'unitsCancelled': item['unitsCancelled'],
                'store_name': storeName,
                'dateCreated': datetime.datetime.strptime(item['period'].split(".")[0], '%Y-%m-%dT%H:%M:%S'),
                'key': storeName+"_"+item['asin']
            }

            query = {
                "asin":dataSet['asin'],
                "store_name":dataSet['store_name'],
                "dateCreated":dataSet['dateCreated'],
                "variationInfo":dataSet['variationInfo']
            }
            my_mongo.update(myclient,"amz_merch","Order",query,dataSet,upsert=True)
    my_mongo.close_mongo(myclient)

def updateManage(my_mongo,profile,manage):
    data_manage = {}
    for item in manage['results']:
        title = item['productTitle']
        status = item['status']
        data_manage[title] = status

    list_products = getProductsByStore(my_mongo,profile["name"])
    for product in list_products:
        if product['title'] in data_manage:
            submitTime = datetime.datetime.now()

            upadteProduct(my_mongo,{'title':product['title'],'store_name':profile["name"]},{"status":data_manage[product['title']],"statusTime":submitTime}) 


def update_sale_all(my_mongo,storeName):
    myclient = my_mongo.create_mongo()

    query = {
        "name": storeName
    }

    for i in my_mongo.find(myclient,"amz_merch","Account",query,{"_id":0,"analyze":1,"name":1}):
        a = list(i['analyze'].keys())[0]
        list_items = i['analyze'][a]
        for item in list_items:
            dataSet = {
                'revenue': item['revenue']['value'],
                'revenueExclTax': item['revenueExclTax']['value'],
                'royalties': item['royalties']['value'],
                'unitsSold': item['unitsSold'],
                'unitsReturned': item['unitsReturned'],
                'title': item['asinName'],
                'productType': item['productType'],
                'variationInfo': item['variationInfo'],
                'asin': item['asin'],
                'unitsCancelled': item['unitsCancelled'],
                'store_name': i['name'],
                'dateCreated': datetime.datetime.strptime(item['period'].split(".")[0], '%Y-%m-%dT%H:%M:%S'),
                'key': i['name']+"_"+item['asin']
            }

            query = {
                "asin":dataSet['asin'],
                "store_name":dataSet['store_name'],
                "dateCreated":dataSet['dateCreated'],
                "variationInfo":dataSet['variationInfo']
            }
            # print("query",query)
            my_mongo.update(myclient,"amz_merch","Order",query,dataSet,upsert=True)

    my_mongo.close_mongo(myclient)

#INSERT
def insertProduct(my_mongo,list_products):
    myclient = my_mongo.create_mongo()
    my_mongo.insert(myclient,"amz_merch","Product",list_products,multi=True)
    my_mongo.close_mongo(myclient)

import pymongo

def create_mongo():
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    return myclient

def close_mongo(myclient):
    myclient.close()

def find(myclient,db_str,col_str,query,projection={"_id":0},limit=0,skip=0):
    mydb = myclient[db_str] 
    data=[]
    if projection == {}:
        for i in mydb[col_str].find(query).skip(skip).limit(limit):
            data.append(i)
    else:
        for i in mydb[col_str].find(query,projection).skip(skip).limit(limit):
            data.append(i)

    return data

def update(myclient,db_str,col_str,query,dataSet,multi=False,upsert=False):
    mydb = myclient[db_str] 

    mydb[col_str].update(query,{"$set":dataSet},multi=multi,upsert=upsert)

def insert(myclient,db_str,col_str,dataSet,multi=False):
    mydb = myclient[db_str]
    if multi == False:
        mydb[col_str].insert_one(dataSet)
    else:
        mydb[col_str].insert_many(dataSet)
    


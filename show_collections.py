import pymongo 

if __name__=='__main__':
    print('welcome to mongodb')
    client=pymongo.MongoClient("mongodb://localhost:27017/") 
    print(client) 
    dbs_names=client.list_database_names()
    print(dbs_names) 
    
    print('======================================================================')
    db=client['students']
    print(db.list_collection_names())
  
  
  # if you want to find the collection names in dbs 
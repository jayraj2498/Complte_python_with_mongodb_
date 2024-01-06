import pymongo 

if __name__=='__main__':
    print('welcome to mongodb')
    client=pymongo.MongoClient("mongodb://localhost:27017/") 
    print(client)
    all_databases=client.list_database_names() 
    for i in all_databases:
        print(i)

        # if you wanrt to see your database you have to write tht code 
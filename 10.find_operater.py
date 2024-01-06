import pymongo 

if __name__=='__main__' :
    print("welcome to mongodb") 
    
    client=pymongo.MongoClient("mongodb://localhost:27017/") 
    print(client)
    
    db=client['students'] 
    collections =db['football']  
    
    
    two = collections.find({ 'name': 'Antoine Griezmann'   ,'age': {"$gt": 28}})
    
    # Iterate over the documents
    for document in two:
        print(document)  
        
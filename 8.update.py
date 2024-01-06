import pymongo 

if __name__=='__main__' :
    print("welcome to mongodb") 
    
    client=pymongo.MongoClient("mongodb://localhost:27017/") 
    print(client)
    
    db=client['students'] 
    collections =db['football']  
    
    collections.update_one({'name':'Bruno Fernandes'} ,{"$set":{'city': 'Mumbai'}} )
    print("upadate completed ")
    
    
    
    
    ## another Method 
    
# import pymongo 

# if __name__=='__main__' :
#     print("welcome to mongodb") 
    
#     client=pymongo.MongoClient("mongodb://localhost:27017/") 
#     print(client)
    
#     db=client['students'] 
#     collections =db['football'] 
    
#     prev={'name':'Antoine Griezmann'} 
#     sett={"$set":{'age':30}}
    
#     collections.update_one(prev,sett)
    
    
      
    
    ### another ex 
    
#     import pymongo  

# if __name__ == '__main__':
#     print("Welcome to MongoDB")
    
#     # Connect to MongoDB
#     client = pymongo.MongoClient("mongodb://localhost:27017/") 
    
#     # Select the database and collection
#     db = client['financedb']
#     trans = db['transactions']  
    
#     # Update the document where 'description' is 'Salary'
#     trans.update_one({'description': 'Salary'}, {"$set": {'category': 'Home_Loan'}})

#     print("Update completed.")

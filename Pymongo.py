import pymongo  


if __name__== "__main__" :
    print("welcome to pymongo") 
    
    client=pymongo.MongoClient("mongodb://localhost:27017/") 
    print(client)
    db=client['education']
    collections=db['school']
    
    
    
    dictionary=({ 'student_name':'akash_jade' , 'marks':89 , 'age':24 })
    collections.insert_one(dictionary)
    
    dictionary2=({ 'student_name':'rushi_sonar' , 'marks':95, 'age':21 })
    collections.insert_one(dictionary2) 
    
    dictionary3=({ 'student_name':'om_dusane' , 'marks':80 , 'age':20 })
    collections.insert_one(dictionary3)
    
    
    
    
# if __name__== "__main__" :
#     print("welcome to pymongo")
    
#     client= pymongo.MongoClient("mongodb://localhost:27017/")
#     print(client)
#     db=client['jayrajdb'] 
#     collections=db['criecket']
    
    
    
#     dictionary={'player_name':'surya_yadav', 'runs':3250}
#     collections.insert_one(dictionary)
    
#     dictionary={'player_name':'jadeja', 'runs':1250}
#     collections.insert_one(dictionary) 
    
    
    
    
#     dictionary=[{'name':'kireon_pollard' , 'runs':4356 , 'age':38}  ,
#                  {'name':'steave_smih' , 'runs':9820, 'country':'austrilia'} ,
#                  {'world_cup':'autrilia' , 'wining_team':'AUS', 'final':'AUS'}
#                 ]

#     collections.insert_many(dictionary)




# import pymongo
# from bson import ObjectId  # Import ObjectId from bson module

# if __name__ == "__main__":
#     print("Welcome to pymongo") 
    
#     # Connect to MongoDB
#     client = pymongo.MongoClient("mongodb://localhost:27017/") 
#     print(client)
    
#     # Select the database and collection
#     db = client['students'] 
#     collections = db['football'] 
    
#     # Create a document with ObjectId
#     dictionary = {
#         '_id': ObjectId("6512b21681d9602431b74202"),
#         'name': 'Bruno Fernandes',
#         'age': 28,
#         'salary': 760000,
#         'city': 'Mumbai',
#         'club': 'Manchester United',
#         'income': 320000
#     }

#     # Insert the document into the collection
#     collections.insert_one(dictionary) 
    
#     print("Update completed")











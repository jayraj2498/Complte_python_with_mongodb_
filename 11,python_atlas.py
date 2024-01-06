# here we are sending collection documents  to 'jayrajAtlas' database  by using python code 
# we just have to do join string with passward 


import pymongo  

if __name__=='__main__':
    print("welcome to MongoDB")
    
    client= pymongo.MongoClient("mongodb+srv://jayraj123:UzsSQJERuYdeho8Y@tutorial.qvm4znp.mongodb.net/")
    print(client) 
    db=client['jayrajAtlas']
    trans=db['road_transport'] 
    
    # Insert some data
    data = [
        {"vehicle": "Truck", "load_capacity": 5000, "destination": "City A"},
        {"vehicle": "Van", "load_capacity": 2000, "destination": "City B"},
        {"vehicle": "Car", "load_capacity": 1000, "destination": "City A"},
        {"vehicle": "Bus", "load_capacity": 3000, "destination": "City C"},
    ]

    trans.insert_many(data)

    print("Data inserted successfully.")

   
   
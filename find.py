import pymongo 

if __name__ == '__main__':
    print(' welcome in pymongo')
    
    client= pymongo.MongoClient("mongodb://localhost:27017/") 
    print(client)  
    db=client['financedb']
    trans=db['transactions'] 
    one=trans.find_one({'amount': -200})
    print(one)
    
    print("====================================================")
    # second way to by ittreative method from these you will get all record
    # rather than find_one it will give you only one record 
    
    two=trans.find({'category': 'Expense'} , )
    for i in two:
        print(i)
    
    
    
    
    
    
    
    # if you select Id = o then it will not select that id part  
    # & if you select id = 1 that condition will be true and only tht part will get run 
    
    
    # two=trans.find({'category': 'Expense'} , {'_id':0})  
    # for i in two:
    #     print(i)
    
#     you op will be like without id 
#     {'date': '2023-09-25', 'description': 'Rent', 'amount': -1500, 'category': 'Expense'}
#     {'date': '2023-09-26', 'description': 'Groceries', 'amount': -200, 'category': 'Expense'}
#     {'date': '2023-09-28', 'description': 'Dining Out', 'amount': -50, 'category': 'Expense'}
#     {'date': '2023-09-30', 'description': 'Utilities', 'amount': -100, 'category': 'Expense'}
#      {'date': '2023-10-02', 'description': 'Shopping', 'amount': -300, 'category': 'Expense'}
    
    
    
    
#   # Find documents where the amount is -200
#     two = trans.find({'amount': -200})
#     print("Documents with amount -200:")
#     for document in two:
#         print(document)





# ## another example 

# import pymongo 

# if __name__=='__main__' :
#     print("welcome to mongodb") 
    
#     client=pymongo.MongoClient("mongodb://localhost:27017/") 
#     print(client)
    
#     db=client['students'] 
#     collections =db['football']  
    
    
#     two=collections.find({'name': 'Cristiano Ronaldo'}  )
#     for i in two:
#         print(i)
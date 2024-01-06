import pymongo 

if __name__ == '__main__':
    print(' welcome in pymongo')
    
    client= pymongo.MongoClient("mongodb://localhost:27017/") 
    print(client)  
   
    db=client['financedb']
    trans=db['transactions'] 
    all_doc=trans.find({'amount': -200} , {'_id':0}) 
    print(all_doc.count()) 
    for i in all_doc:
        print(i)
         
      
      
      
      
    
    
    
    
    
    
  
# two=trans.find({'category': 'Expense'} , )
#     for i in two:
#         print(i)
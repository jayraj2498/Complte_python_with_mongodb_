import pymongo  

if __name__=='__main__':
    print("welcome to MongoDB")
    
    client= pymongo.MongoClient("mongodb://localhost:27017/") 
    
    db=client['financedb']
    trans=db['transactions'] 
    
    documents=[
    {'date': '2023-09-25', 'description': 'Salary', 'amount': 5000, 'category': 'Income'},
    {'date': '2023-09-25', 'description': 'Rent', 'amount': -1500, 'category': 'Expense'},
    {'date': '2023-09-26', 'description': 'Groceries', 'amount': -200, 'category': 'Expense'},
    {'date': '2023-09-27', 'description': 'Bonus', 'amount': 1000, 'category': 'Income'},
    {'date': '2023-09-28', 'description': 'Dining Out', 'amount': -50, 'category': 'Expense'},
    {'date': '2023-09-29', 'description': 'Investment', 'amount': 2000, 'category': 'Income'},
    {'date': '2023-09-30', 'description': 'Utilities', 'amount': -100, 'category': 'Expense'},
    {'date': '2023-10-01', 'description': 'Freelance Work', 'amount': 800, 'category': 'Income'},
    {'date': '2023-10-02', 'description': 'Shopping', 'amount': -300, 'category': 'Expense'},
    {'date': '2023-10-03', 'description': 'Dividends', 'amount': 150, 'category': 'Income'},
    ]
    
    trans.insert_many(documents) 
    
    
    
print("Sample financial data inserted into the 'documents' ")


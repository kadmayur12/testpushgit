import pymongo
client = pymongo.MongoClient("mongodb+srv://Mayur:839017@cluster0.retuvxy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
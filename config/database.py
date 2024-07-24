from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:1234@cluster0.feo3fu4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.AccidentReport_db

collection_name = db["AccidentReportDetails"]

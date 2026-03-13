from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["alumni_network"]

students = db["students"]
alumni = db["alumni"]
mentorship_requests = db["mentorship_requests"]
sessions = db["sessions"]
feedback = db["feedback"]
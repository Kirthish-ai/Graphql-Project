# Alumni Mentorship Network – GraphQL API

## 📌 Project Description

The Alumni Mentorship Network is a GraphQL API project built using Python, FastAPI, Strawberry GraphQL, and MongoDB.
This system connects students with alumni mentors, allows mentorship requests, session scheduling, and feedback tracking.

The API is tested using Altair GraphQL Client.

Technologies used:

* Python
* FastAPI
* Strawberry GraphQL
* MongoDB
* Altair GraphQL Client

---

## 📌 Features

* Fetch alumni by domain
* Request mentorship
* Approve mentorship request
* Create mentoring session
* Add feedback with rating
* Maintain mentorship history in MongoDB

---

## 📌 Project Structure

alumni-graphql/
│
├── main.py
├── schema.py
├── models.py
├── database.py
├── requirements.txt
└── README.md

---

## 📌 Step 1 – Download the Project

Download the project folder from GitHub or copy the files manually.

If using git:

git clone <repository_link>

Open terminal inside project folder.

cd alumni-graphql

---

## 📌 Step 2 – Create Virtual Environment

python3 -m venv venv

Activate virtual environment

Mac / Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate

---

## 📌 Step 3 – Install Required Libraries

pip install fastapi strawberry-graphql pymongo uvicorn

or

pip install -r requirements.txt

---

## 📌 Step 4 – Install MongoDB

Download MongoDB Community Edition

https://www.mongodb.com/try/download/community

Start MongoDB service.

Default connection used in project:

mongodb://localhost:27017

Database name:

alumni_network

---

## 📌 Step 5 – Insert Sample Data

Open MongoDB Compass.

Create database:

alumni_network

Create collection:

alumni

Insert document:

{
"id":1,
"name":"Rahul Sharma",
"company":"Infosys",
"domain":"IT"
}

Insert student:

{
"id":1,
"name":"Amit Patil",
"email":"[amit@gmail.com](mailto:amit@gmail.com)",
"year":2024
}

---

## 📌 Step 6 – Run the Server

Run:

uvicorn main:app --reload

Server will start at:

http://127.0.0.1:8000/graphql

---

## 📌 Step 7 – Install Altair GraphQL Client

Download Altair GraphQL Client:

https://altairgraphql.dev

Install and open Altair.

Endpoint:

http://127.0.0.1:8000/graphql

Paste endpoint in Altair URL bar.

Click SEND after writing queries.

---

## 📌 Step 8 – Test Queries

Query alumni by domain

query {
alumni(domain:"IT"){
name
company
}
}

---

## 📌 Step 9 – Test Mutations

Request mentorship

mutation {
requestMentorship(input:{
studentId:1
alumniId:1
}){
id
status
}
}

Approve mentorship

mutation {
approveMentorship(requestId:1){
id
status
}
}

Create session

mutation {
createSession(input:{
mentorId:1
studentId:1
scheduledTime:"2026-04-10 10:00"
notes:"Career guidance"
}){
id
}
}

Add feedback

mutation {
addFeedback(input:{
sessionId:1
rating:5
comment:"Very helpful session"
}){
id
rating
}
}

---

## 📌 Test Cases Covered

1. Domain filter
2. Mentorship request flow
3. Approval flow
4. Session creation
5. Feedback tracking
6. History stored in MongoDB

Collections used:

students
alumni
mentorship_requests
sessions
feedback

---

## 📌 Conclusion

This project demonstrates how GraphQL APIs can be used to build a mentorship system where students connect with alumni mentors.
MongoDB is used to store data, FastAPI runs the server, and Altair GraphQL Client is used to test queries and mutations.

This system shows how modern API design can be used for real-world applications.

import strawberry
from database import students, alumni, mentorship_requests, sessions, feedback
from models import Student, Alumni, MentorshipRequest, Session, Feedback

# -------- INPUT TYPES --------

@strawberry.input
class MentorshipRequestInput:
    studentId: int
    alumniId: int


@strawberry.input
class SessionInput:
    mentorId: int
    studentId: int
    scheduled_time: str
    notes: str


@strawberry.input
class FeedbackInput:
    session_id: int
    rating: int
    comment: str


# -------- QUERIES --------

@strawberry.type
class Query:

    @strawberry.field
    def alumni(self, domain: str = None) -> list[Alumni]:

        if domain:
            result = alumni.find({"domain": domain})
        else:
            result = alumni.find()

        return [
            Alumni(
                id=i["id"],
                name=i["name"],
                company=i["company"],
                domain=i["domain"],
            )
            for i in result
        ]


# -------- MUTATIONS --------

@strawberry.type
class Mutation:

    @strawberry.mutation
    def requestMentorship(self, input: MentorshipRequestInput) -> MentorshipRequest:

        new_id = mentorship_requests.count_documents({}) + 1

        data = {
            "id": new_id,
            "student_id": input.studentId,
            "alumni_id": input.alumniId,
            "status": "requested",
        }

        mentorship_requests.insert_one(data)

        # fetch document again
        doc = mentorship_requests.find_one({"id": new_id})
    
        # remove MongoDB automatic field
        doc.pop("_id", None)
    
        return MentorshipRequest(**doc)


    @strawberry.mutation
    def approveMentorship(self, requestId: int) -> MentorshipRequest:

        mentorship_requests.update_one(
            {"id": requestId},
            {"$set": {"status": "approved"}}
        )

        doc = mentorship_requests.find_one({"id": requestId})

        if doc:
            doc.pop("_id", None)
    
        return MentorshipRequest(**doc)


    @strawberry.mutation
    def createSession(self, input: SessionInput) -> Session:

        new_id = sessions.count_documents({}) + 1

        data = {
            "id": new_id,
            "mentor_id": input.mentorId,
            "student_id": input.studentId,
            "scheduled_time": input.scheduled_time,
            "notes": input.notes
        }

        sessions.insert_one(data)
        doc = sessions.find_one({"id": new_id})

        # remove MongoDB automatic field
        doc.pop("_id", None)
    
        return Session(**doc)


    @strawberry.mutation
    def addFeedback(self, input: FeedbackInput) -> Feedback:

        new_id = feedback.count_documents({}) + 1

        data = {
            "id": new_id,
            "session_id": input.session_id,
            "rating": input.rating,
            "comment": input.comment,
        }

        feedback.insert_one(data)

        doc = feedback.find_one({"id": new_id})

        # remove MongoDB automatic field
        doc.pop("_id", None)
    
        return Feedback(**doc)


schema = strawberry.Schema(query=Query, mutation=Mutation)
import strawberry

@strawberry.type
class Student:
    id: int
    name: str
    email: str
    year: int


@strawberry.type
class Alumni:
    id: int
    name: str
    company: str
    domain: str


@strawberry.type
class MentorshipRequest:
    id: int
    student_id: int
    alumni_id: int
    status: str


@strawberry.type
class Session:
    id: int
    mentor_id: int
    student_id: int
    scheduled_time: str
    notes: str


@strawberry.type
class Feedback:
    id: int
    session_id: int
    rating: int
    comment: str
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from model.base import db
from model.associations import course_user_link

class Course(db.Model):
    __tablename__ = 'course'

    class_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, primary_key=False)
    section_id = Column(Integer, primary_key=False)
    course_title = Column(String(100), nullable=False)
    department = Column(String(50), nullable=False)
    campus = Column(String(20), nullable=False)
    term = Column(String(5), nullable=False)
    days_offered = Column(String(30), nullable=False)
    times_offered = Column(String(30), nullable=False)
    enroll_status = Column(Integer, nullable=False)
    # technically has tinyint(1) datatype, SQLite might try to interpret that as a boolean
    # enroll_status should support values of 0, 1, 2.
    credits = Column(Integer, nullable=False)

    users = relationship("User", secondary=course_user_link, back_populates='courses')

    def json(self):
        return {'class_id': self.class_id,
                'course_id': self.course_id,
                'section_id': self.section_id,
                'course_title': self.course_title,
                'department': self.department,
                'campus': self.campus,
                'term': self.term,
                'days_offered': self.days_offered,
                'times_offered': self.times_offered,
                'enroll_status': self.enroll_status,
                'credits': self.credits
                }

    def __repr__(self):
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"
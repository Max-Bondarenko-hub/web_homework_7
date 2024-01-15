from sqlalchemy import func, desc, and_
from connection import session
from create_tables import GroupNames, Disceplines, Students, Professors, Grades
from pprint import pprint


def select_1():
    s1 = (
        session.query(Students.name.label("Student"), func.round(func.avg(Grades.grade), 1).label("AvgGrade"))
        .select_from(Grades)
        .join(Students)
        .group_by(Students.id)
        .order_by(desc("AvgGrade"))
        .limit(5)
        .all()
    )
    return s1


def select_2():
    s2 = (
        session.query(
            Grades.student_name, Grades.discepline_name, func.round(func.avg(Grades.grade), 1).label("AvgGrade")
        )
        .select_from(Grades)
        .filter(Grades.discepline_name == "Biology")
        .group_by(Grades.student_name, Grades.discepline_name)
        .order_by(desc("AvgGrade"))
        .limit(1)
        .all()
    )
    return s2


def select_3():
    s3 = (
        session.query(
            Grades.discepline_name, GroupNames.name, func.round(func.avg(Grades.grade), 1).label("AvgGrade")
        )
        .select_from(Grades)
        .join(Students)
        .join(GroupNames)
        .filter(Grades.discepline_name == "Math")
        .group_by(Grades.discepline_name, GroupNames.name)
        .order_by(desc("AvgGrade"))
        .all()
    )
    return s3    


def select_4():
    s4 = (
        session.query(
           func.round(func.avg(Grades.grade), 1).label("AvgGrade") 
        )
        .select_from(Grades)
        .all()
    )
    return s4


def select_5():
    s5 = (
        session.query(
            Disceplines.name, Professors.name
        )
        .select_from(Professors)
        .join(Disceplines)
        .filter(Professors.name == 'Tyrone Gonzalez')
        .all()
    )
    return s5


def select_6():
    s6 = (
        session.query(
            GroupNames.name, Students.name
        )
        .select_from(GroupNames)
        .join(Students)
        .filter(GroupNames.name == 'KI24')
        .all()
    )
    return s6


def select_7():
    s7 = (
        session.query(
            GroupNames.name, Students.name, Disceplines.name, Grades.grade
        )
        .select_from(GroupNames)
        .join(Students)
        .join(Disceplines)
        .join(Grades)
        .filter(and_(Disceplines.name == 'History', GroupNames.name == 'KI24'))
        .all()
    )
    return s7


def select_8():
    s8 = (
        session.query(
            Professors.name, Disceplines.name, func.round(func.avg(Grades.grade), 1).label("AvgGrade")
        )
        .select_from(GroupNames)
        .join(Students)
        .join(Grades)
        .join(Disceplines)
        .join(Professors)
        .group_by(Professors.name, Disceplines.name)
        .all()
    )
    return s8


def select_9 ():
    s9 = (
        session.query(
            Students.name, Disceplines.name, GroupNames.name
        )
        .select_from(GroupNames)
        .join(Students)
        .join(Disceplines)
        .filter(Students.name == 'Martha Jacobs')
        .all()
    )
    return s9


def select_10 ():
    s10 = (
        session.query(
            Students.name, Disceplines.name, Professors.name, GroupNames.name
        )
        .select_from(GroupNames)
        .join(Disceplines)
        .join(Students)
        .join(Professors)
        .filter(and_(Students.name == 'Martha Jacobs', Professors.name == 'Megan Ellis'))
        .all()        
    )
    return s10

pprint(select_1())

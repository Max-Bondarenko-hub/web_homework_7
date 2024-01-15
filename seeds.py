import faker
import random
from connection import session
from create_tables import GroupNames, Disceplines, Students, Professors, Grades
from random import randint, choice


NUMBER_STUDENTS = 45
NUMBER_PROFESSORS = 5
GROUPS_NAME = ('KI24', 'PM33', 'AS55')
DISCIPLINES = ('Biology', 'History', 'Math', 'Psychology', 'Since')
MAX_NUMBER_GRADES = 20


def generate_fake_data(number_students, number_professors) -> tuple():
    fake_students = []
    fake_professors = []
    fake_data = faker.Faker()

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_professors):
        fake_professors.append(fake_data.name())

    return fake_students, fake_professors

std_list, prof_list = generate_fake_data(NUMBER_STUDENTS, NUMBER_PROFESSORS)

for group in GROUPS_NAME:
    gr_name = GroupNames(name=group)
    session.add(gr_name)
    session.commit()

for std in std_list:
    fullname = Students(name=std, group_id=randint(1, 3))
    session.add(fullname)
    session.commit()

for disc in DISCIPLINES:
    discipline = Disceplines(name=disc, group_id=randint(1,3))
    session.add(discipline)
    session.commit()    

rand_disc_list = random.sample(range(1, len(DISCIPLINES) + 1), k=len(DISCIPLINES))
i = 0
for prof in prof_list:
    professor = Professors(name=prof, discipline_id=rand_disc_list[i])
    i += 1
    session.add(professor)
    session.commit()   

for stud in std_list:
    for _ in range(1, MAX_NUMBER_GRADES):
        std_id = (std_list.index(stud) + 1)
        grades = Grades(student_name=stud, discepline_name=choice(DISCIPLINES), grade=randint(1, 100), student_id=std_id)
        session.add(grades)
        session.commit()

print('Fake data generating complite')
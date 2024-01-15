from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class GroupNames(Base):
    __tablename__ = "group_names"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]


class Students(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    group_id: Mapped[int] = mapped_column(ForeignKey("group_names.id"))
    groupname: Mapped['GroupNames'] = relationship('GroupNames')


class Disceplines(Base):
    __tablename__ = "disceplines"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    group_id: Mapped[int] = mapped_column(ForeignKey("group_names.id"))
    groupname: Mapped['GroupNames'] = relationship('GroupNames')


class Professors(Base):
    __tablename__ = "professors"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    discipline_id: Mapped[int] = mapped_column(ForeignKey("disceplines.id"))
    disc: Mapped['Disceplines'] = relationship('Disceplines')


class Grades(Base):
    __tablename__ = "grades"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    student_name: Mapped[str]
    discepline_name: Mapped[str]
    grade: Mapped[int]
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    std: Mapped['Students'] = relationship('Students')

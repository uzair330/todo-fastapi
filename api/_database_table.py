from sqlalchemy.orm import declarative_base, Mapped, column_property
from sqlalchemy import Column, Integer, String
from ._database_connection import Session, engine

Base = declarative_base()


class Todo_Table(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)
    status = Column(String, nullable=False)

    def __repr__(self):
        return f"<Todo_Table {self.task}>"


def Data_send(task, status):
    session = Session()
    todo = Todo_Table(task=task, status=status)
    session.add(todo)
    session.commit()
    print("Data sent")
    session.close()


def Creating_table():
    Base.metadata.create_all(bind=engine)
    print("Table created")

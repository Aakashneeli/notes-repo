"""Completed label CRUD mechanics, not a Task repository implementation."""
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session
from orm_example import Base, Label

def run():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        with session.begin():
            session.add_all([Label(name="draft"), Label(name="review"), Label(name="ready")])
        with session.begin():
            total = session.scalar(select(func.count()).select_from(Label))
            names = session.scalars(select(Label.name).order_by(Label.id).offset(1).limit(1)).all()
            print("page", total, names)
        with session.begin():
            row = session.scalars(select(Label).where(Label.name == "draft")).one()
            row.name = "private"  # Dirty tracking turns assignment into UPDATE at flush.
        with session.begin():
            row = session.scalars(select(Label).where(Label.name == "review")).one()
            session.delete(row)  # DELETE is sent when flushed.
        print("remaining", session.scalars(select(Label.name).order_by(Label.id)).all())
    engine.dispose()

if __name__ == "__main__":
    run()

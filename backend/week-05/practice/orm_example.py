"""Completed mechanism example; intentionally not the Task API."""
from sqlalchemy import String, create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

class Base(DeclarativeBase):
    pass

class Label(Base):
    __tablename__ = "example_labels"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), unique=True)

def run():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)  # Only this disposable mechanism example.
    with Session(engine) as session:
        with session.begin():
            item = Label(name="draft")
            session.add(item)
            session.flush()
            print("flushed", item.id)
    with Session(engine) as session:
        print("committed", session.scalars(select(Label.name)).all())
        session.rollback()  # The SELECT began a transaction.
        try:
            with session.begin():
                session.add_all([Label(name="review"), Label(name="draft")])
                session.flush()
        except IntegrityError:
            print("rolled back")
        print("remaining", session.scalars(select(Label.name).order_by(Label.id)).all())
    engine.dispose()

if __name__ == "__main__":
    run()

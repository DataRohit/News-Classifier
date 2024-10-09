from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/news_db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    content = Column(String)
    pub_date = Column(DateTime)
    source_url = Column(String)
    category = Column(String)


Base.metadata.create_all(engine)


def add_article_to_db(article):
    session = Session()
    existing_article = session.query(Article).filter_by(title=article["title"]).first()
    if not existing_article:
        new_article = Article(**article)
        session.add(new_article)
        session.commit()
    session.close()

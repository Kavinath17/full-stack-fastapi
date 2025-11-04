from app.db.session import engine
from app.models import Base

def init_db():
    print("Creating all database tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully!")

if __name__ == "__main__":
    init_db()

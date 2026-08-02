from sqlalchemy import Column, Integer, String

from app.database import Base


class Etudiant(Base):
    __tablename__ = "etudiant"

    id = Column(Integer, primary_key=True, index=True)

    nom = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, nullable=False)
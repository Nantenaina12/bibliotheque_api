from sqlalchemy import Boolean, Column, Integer, String

from app.database import Base


class Livre(Base):
    __tablename__ = "livre"

    id = Column(Integer, primary_key=True, index=True)

    titre = Column(String(150), nullable=False)

    auteur = Column(String(100), nullable=False)

    disponible = Column(Boolean, default=True)
from sqlalchemy import Boolean, Column, Integer, String

from app.database import Base
from sqlalchemy.orm import relationship


class Livre(Base):
    __tablename__ = "livre"

    id = Column(Integer, primary_key=True, index=True)

    titre = Column(String(150), nullable=False)

    auteur = Column(String(100), nullable=False)

    disponible = Column(Boolean, default=True)

emprunts = relationship(
    "Emprunt",
    back_populates="livre"
)
from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database import Base


class Emprunt(Base):
    __tablename__ = "emprunt"

    id = Column(Integer, primary_key=True, index=True)

    date_emprunt = Column(Date, nullable=False)

    date_retour = Column(Date)

    id_etudiant = Column(
        Integer,
        ForeignKey("etudiant.id"),
        nullable=False
    )

    id_livre = Column(
        Integer,
        ForeignKey("livre.id"),
        nullable=False
    )

    etudiant = relationship("Etudiant", back_populates="emprunts")

    livre = relationship("Livre", back_populates="emprunts")
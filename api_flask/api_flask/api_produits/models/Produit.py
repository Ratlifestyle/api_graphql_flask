from api_produits import db
from sqlalchemy import Column, Integer, Text


class Produit(db.Model):
    __tablename__ = 'produit'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(Text, nullable=False, unique=True)
    nom = Column(Text, nullable=False)
    stock = Column(Integer, nullable=False)

    def __init__(self, code, nom, stock):
        self.code = code
        self.nom = nom
        self.stock = stock

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "nom": self.nom,
            "stock": self.stock
        }

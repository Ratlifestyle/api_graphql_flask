import requests

def resolve_produits(obj, info):
    try:
        produits = requests.get('http://localhost:5000/product').content
        print(type(produits))
        payload = {
            "success": True,
            "produits": produits
        }
    except Exception as error:
        print(error)
        payload = {
            "success": False,
            "error": [str(error)]
        }
    finally:
        return payload

def resolve_produit(obj, info, produitCode):
    try:
        produit = Produit.query.filter_by(code=produitCode).first()
        payload = {
            "success": True,
            "produit": produit
        }
    except Exception as error:
        print(error)
        payload = {
            "success": False,
            "error": [str(error)]
        }
    finally:
        return payload


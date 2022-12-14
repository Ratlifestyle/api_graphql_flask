def resolve_create_produit(obj, info, code, nom, stock):
    try:
        produit = Produit(code, nom, stock)
        db.session.add(produit)
        db.session.commit()
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
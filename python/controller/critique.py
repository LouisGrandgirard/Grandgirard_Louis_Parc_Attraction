import request.request as req

def add_critique(data):
    if (not "attraction_id" in data):
        return False
    if (not "note" in data or data["note"] is None):
        return False
    
    # Optional fields
    name = data.get("name", "Anonyme")
    commentaire = data.get("commentaire", "")

    requete = "INSERT INTO critique (attraction_id, name, note, commentaire) VALUES (?, ?, ?, ?);"
    id = req.insert_in_db(requete, (data["attraction_id"], name, data["note"], commentaire))

    return id

def get_critiques_by_attraction(attraction_id):
    if (not attraction_id):
        return []
    
    json = req.select_from_db("SELECT * FROM critique WHERE attraction_id = ?", (attraction_id,))
    return json

def get_all_critiques():
    json = req.select_from_db("SELECT * FROM critique")
    return json

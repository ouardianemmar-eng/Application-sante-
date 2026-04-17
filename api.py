
import sqlite3
from fastapi import FastAPI

from fastapi import FastAPI, Security, HTTPException, status
from fastapi.security import APIKeyHeader

DB_PATH = "./data/processed/sante.db"

API_KEY = "motdepasse" # secret d'authentification
api_key_header = APIKeyHeader(name="X-API-Key") # champs d'authentification
 
def verifier_cle(cle: str = Security(api_key_header)):
    if cle != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Clé API invalide."
        )
        
        
def ouvrir_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

app = FastAPI(
    title="API Santé & Territoires",
    description="Données épidémiologiques de la Haute-Garonne – Source CNAM",
    version="1.0.0"
)

# ──────────────────────────────────────────────────────────────────
# GET /top5-pathologies
# Retourne les 5 pathologies les plus prépondérantes
# dans le département Haute-Garonne (31) — toutes années confondues
# ──────────────────────────────────────────────────────────────────
@app.get("/", dependencies=[Security(verifier_cle)])
def top5_pathologies():
    """
    Retourne les 5 pathologies avec la prévalence moyenne
    la plus élevée dans le département 31 (Haute-Garonne).
    """
    requete = """
        SELECT patho_niv1 as pathologie,ROUND(AVG(prev_calculee), 2) as prevalance_moyenne
        FROM pathologies
        WHERE dept = 31
        GROUP BY patho_niv1
        ORDER BY prevalance_moyenne DESC
        LIMIT 5
    """
    conn = ouvrir_db()
    resultats = conn.execute(requete).fetchall()
    conn.close()

    return [dict(ligne) for ligne in resultats]
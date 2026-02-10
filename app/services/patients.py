from services.db import patients_col

def add_patient(patient_id, consent):
    """Ajoute un patient avec son consentement"""
    patients_col.insert_one({
        "_id": patient_id,
        "consent": consent
    })

from services.db import analyses_col

def add_analysis(patient_id, result):
    analyses_col.insert_one({
        "patient_id": patient_id,
        "result": result
    })

def get_history(patient_id):
    return list(analyses_col.find({"patient_id": patient_id}))

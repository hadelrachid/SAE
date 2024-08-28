from Patient import SPatient

patient = SPatient()

# Configurando as informações clínicas prévias
previous_clinical_info = {
    "procedencia": 2,  # Samu
    "tabagismo": {
        "status": "Yes",
        "duration": "10 years"
    },
    "drogas_ilicitas": {
        "status": "No",
        "duration": None
    },
    "etilismo": {
        "status": "Yes",
        "duration": "5 years"
    },
    "alergia": {
        "status": "Yes",
        "description": "Pollen"
    }
}

personal_history = {
            "antecedentes": 1,  # 1 - DM, 2 - HAS, 3 - Cadiopatia, 4 - Respiratoria, 5 - Neurologica
            "cirurgia": {
                "status": "Yes",
                "description": "cardiology"  # Optional if status is "Yes"
            }     
}

patient.set_previous_clinical_info(previous_clinical_info)
patient.set_personal_history(personal_history)

# Recuperando as informações clínicas prévias
info = patient.get_previous_clinical_info()
info2 = patient.get_personal_history()
print(info)
print(info2)


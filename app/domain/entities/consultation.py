from dataclasses import dataclass
from datetime import datetime


@dataclass
class Consultation:
    id: int
    patient_id: int
    doctor_id: int
    date: datetime
    time: datetime
    payment: float
    diagnostic: str
    treatment: str
    observations: str 

    def _post_init_(self):
        # le diagnostic est obligatoire
        if not self.diagnostic.strip():
            raise ValueError("Le diagnostic est obligatoire.")
        # le traitement est obligatoire
        if not self.treatment.strip():
            raise ValueError("Le traitement est obligatoire.")
        # les observations sont obligatoires
        if not self.observations.strip():
            raise ValueError("Les observations sont obligatoires.")
        # la date doit etre dans le future
        if self.date <= datetime.now():
            raise ValueError("la date de la consulation doi etre planifiee dans le futur.")
        # patient et medcin doivent etre differentes de 0
        if self.patient_id <= 0:
            raise ValueError("patient invalide.0.")
        if self.doctor_id <= 0:
            raise ValueError("medcin invalide.0.")
        # le patient doit avoir au moins 6 ans
        if self.patient_id < 6:
            raise ValueError("le patient doit avoir au moins 6ans.")
        # Le médecin doit avoir un id valide
        if self.doctor_id <= 0:
            raise ValueError("Médecin invalide.")
        # le patient doit avoir un id valide
        if not self.patient_id or self .patient_id <= 0:
            raise ValueError("Patient invalide.")
        # le paiment doit etre valider avant la consultaion
        if self.payment <= 0:
            raise ValueError("Le Paiment doit etre Valider avant la consultation.")
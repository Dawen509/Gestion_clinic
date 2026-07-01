from dataclasses import dataclass
from datetime import datetime

@dataclass
class Consultation:
    id: int
    patient_id: int
    doctor_id: int
    date: datetime
    time: datetime
    diagnostic: str
    treatment: str
    observations: str
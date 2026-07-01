from dataclasses import dataclass
import datetime
import datetime
@dataclass
class Appointment:
    id: int
    patient_id: int
    doctor_id: int
    date_rendevous_: datetime
    time: str
    status: str= "En attente"
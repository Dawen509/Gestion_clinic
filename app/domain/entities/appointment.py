from dataclasses import dataclass
from datetime  import datetime
from enum import Enum

from domain.entities import ValidationError

class StatusRendezvous(str, Enum):
      PLANIFIE = "PLANIFIE"
      EN_COURS = "EN_COURS"
      CONFIRME = "CONFIRME"
      ANNULE = "ANNULE"
      TERMINE = "TERMINE"


@dataclass
class Appointment:
      id: int
      patient_id: int
      doctor_id : int
      diagnostic_: int
      date_rendezvous_: datetime 
      motif: str
      time:  str
      status: StatusRendezvous = StatusRendezvous.PLANIFIE 
    
      def _post_init_(self):
            # le motif est obligatoire
            if not self.motif.strip():
                  raise ValidationError("Le motif est obligatoire.")
            # la date doit etre dans le future 
            if self.date_rendezvous_ <= datetime.now():
                  raise ValidationError("La date du rendez-vous doit être dans le futur.")
            # Patient et médecin doivent être differentes de 0
            if self.patient_id <= 0:
                  raise ValidationError("Patient invalide.0.")    
            if self.doctor_id <= 0:
                  raise ValidationError("Médecin invalide.0.")    
            # Le status initial doit etre PLANIFIE
            if self.status not in StatusRendezvous:
                  raise ValidationError("Status invalide.")
            
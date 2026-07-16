from datetime import datetime
from app.domain.entities.appointment import Appointment, StatusRendezvous

class CreateAppointment:
    def __init__(self, appointment_repository):
        self.appointment_repository = appointment_repository

    def execute(self, patient_id, doctor_id, date_rendezvous_, motif, time):
        appointment = Appointment(
            id=None,
            patient_id=patient_id,
            doctor_id=doctor_id,
            diagnostic_=0,
            date_rendezvous_=date_rendezvous_,
            motif=motif,
            time=time,
            status=StatusRendezvous.PLANIFIE
        )
        return self.appointment_repository.add(appointment) 
class CreateAppointment:
    def _init_(self, appointemnt_repository):
        self.appointment_repository = appointemnt_repository
    def execute(self, sptient_id, doctor_id, date, reason):
        appointment = {
            "appointment_id": sptient_id,
            "doctor_id": doctor_id,
            "date": date,
            "reason": reason
        }
        return self.appointment_repository.create(appointment) 
        
class CancelAppointment:
    def _init_(self, appointment_repository):
        self.appointment_repository = appointment_repository
    def execute(self, appointement_id):
        appointment = self.appointment_repository.get_by_id(appointement_id)

        if appointment is None:
            raise Exception("Appointment not found")
        self.appointment_repository.delete(appointement_id)
        return True 
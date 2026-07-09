class List_Appointment:
    def _init_(self, appointement_repository):
        self.appointment_repository = appointement_repository
        
    def execute(self):
        return self.appoimtment_repository.get_all()
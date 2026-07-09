class Createconsultation:
    def _init_(self, consultation_repository):
        self.consulation_repository = self.consulation_repository
    def execute(self, appointment_id, diagnostic, treatmnt):
        consultation = {
            "appointment_id":appointment_id,
            "diagnostic": diagnostic,
            "treatment": treatmnt 
        }         
        return self.consulation_repository.create(consultation)
from app.domain.entities.consultation import Consultation

class CreateConsultation:
    def __init__(self, consultation_repository):
        self.consultation_repository = consultation_repository

    def execute(self, consultation):
        return self.consultation_repository.create(consultation) 

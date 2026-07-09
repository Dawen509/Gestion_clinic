from app.domain.repositories.patient_repository import patientRepository 

class listPatientUseCase:

    def __init__(self, patient_repository: patientRepository):
        self.patient_repository = patientRepository
    def execute(self):
        return self,patientRepository.repository 
class CreatePatient:
    def __init__(self, patient_repository):
        self.patient_repository = patient_repository 

    def execute(self, patient):
        return self.patient_repository.save(patient) 
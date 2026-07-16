class DeletePatient:
    def __init__(self, patient_repository):
        self.patient_repository = patient_repository

    def execute(self, patient_id):
        return self.patient_repository.delete(patient_id)  
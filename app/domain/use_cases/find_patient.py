class FindPatient:
    def __init__(self, patient_repository):
        self.patient_repository = patient_repository

    def execute(self, patient_id):
        return self.patient_repository.find_by_id(patient_id)    
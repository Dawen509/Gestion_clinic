class ListPatients:
    def __init__(self, patient_repository):
        self.patient_repository = patient_repository

    def execute(self):
         return self.patient_repository.find_all() 
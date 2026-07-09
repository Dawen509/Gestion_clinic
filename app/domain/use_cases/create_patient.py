class CreatePatient:
    def __init__(self, patint_repository):
        self.patient_repository = self.patient_repository

    def execute(self, first_name, last_name, age, sexe, telephone):
        patient = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "sexe": sexe,
            "telephone": telephone
        }

        return self.patient_repository.create(patient) 
class CreateDoctor:
    def _init_(self, doctor_repository):
        self.doctor_repository = doctor_repository

    def execute (self, name,specialty, telephone):
        doctor = {
            "name": name,
            "specialty": specialty,
           "telephone": telephone,
        } 
        return self.doctor_repository.create(doctor) 
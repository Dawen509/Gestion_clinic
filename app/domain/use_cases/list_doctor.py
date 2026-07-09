class ListDoctor:
    def _init_(self, doctor_repository):
        self.doctor_repository = doctor_repository 

    def execute(self):
        return self.doctor_repository.get_all() 
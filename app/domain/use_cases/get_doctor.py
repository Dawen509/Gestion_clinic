class GetDoctor:
    def __init__(self, doctor_repository):
        self.doctor_repository =doctor_repository

    def execute(self, doctor_id):
        return self.doctor_repository.get_by_id(doctor_id) 
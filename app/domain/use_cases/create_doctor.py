from app.domain.entities.doctor import Doctor

class CreateDoctor:
    def __init__(self, doctor_repository):
        self.doctor_repository = doctor_repository

    def execute(self, nom, prenom, age, speciality, telephone, adresse, email):
        doctor = Doctor(
            id=None,
            nom=nom,
            prenom=prenom,
            age=age,
            speciality=speciality,
            telephone=telephone,
            adresse=adresse,
            email=email
        )
        return self.doctor_repository.save(doctor) 
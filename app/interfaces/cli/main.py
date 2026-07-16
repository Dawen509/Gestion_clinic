from app.interfaces.cli.menu import Menu
from app.infrastructure.patient_repository_impl import PatientRepositoryImpl
from app.domain.use_cases.create_patient import CreatePatient
from app.domain.use_cases.find_patient import FindPatient
from app.domain.use_cases.list_patient import ListPatients
from app.domain.use_cases.delete_patient import DeletePatient
from app.domain.entities.patient import Patient 


repository = PatientRepositoryImpl()

create_patient = CreatePatient(repository) 
find_patient = FindPatient(repository) 
list_patients = ListPatients(repository)
delete_patient = DeletePatient(repository) 


while True: 

    Menu.afficher()

    choix = input("Votre choix : ")

    if choix == "1":

        nom = input("Nom : ")
        prenom = input("Prénom : ")
        age = int(input("Age : "))
        sexe = input("Sexe : ")
        telephone = input("Téléphone : ")
        adresse = input("Adresse : ") 

        patient = Patient(
            id=None,
            nom=nom,
            prenom=prenom,
            age=age,
            sexe=sexe,
            telephone=telephone,
            adresse=adresse,
        )

        create_patient.execute(patient)

        print("Patient enregistré.")

    elif choix == "2":

        id = int(input("Id du patient : "))

        patient = find_patient.execute(id)

        if patient:
            print(patient.nom)
            print(patient.prenom)
            print(patient.age)
        else:
            print("Patient introuvable.")

    elif choix == "3":

        patients = list_patients.execute()

        for p in patients:
            print(
                p.id,
                p.nom,
                p.prenom,
                p.age
            )

    elif choix == "5":

        id = int(input("Id : "))

        delete_patient.execute(id)

        print("Patient supprimé.")

    elif choix == "0":
        break

    else:
        print("Choix invalide.") 
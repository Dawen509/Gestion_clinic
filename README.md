# Gestion Clinic

Application de gestion de clinique (patients, médecins, rendez-vous, consultations) construite en Python, en s'inspirant des principes de la **Clean Architecture**.

## 📁 Structure du projet

```
Gestion_clinic/
├── app/
│   ├── domain/
│   │   ├── entities/          # Entités métier (Doctor, Patient, ...)
│   │   └── use_cases/         # Cas d'usage / règles métier
│   │       ├── create_doctor.py
│   │       ├── create_patient.py
│   │       ├── delete_patient.py
│   │       ├── find_patient.py
│   │       ├── get_doctor.py
│   │       ├── list_appointment.py
│   │       ├── list_consultation.py
│   │       ├── list_doctor.py
│   │       └── list_patient.py
│   ├── infrastructure/
│   │   ├── admin_repository_impl.py
│   │   ├── appointment_repository_impl.py
│   │   ├── consultation_repository_impl.py
│   │   ├── database.py
│   │   ├── doctor_repository_impl.py
│   │   └── patient_repository_impl.py
│   └── interfaces/
│       ├── di/
│       │   ├── main.py
│       │   └── menu.py
│       └── templates/
│           ├── index.html
│           ├── add.html
│           ├── add_doctor.html
│           ├── add_appointment.html
│           └── add_consultation.html
├── app.py
├── config.py
├── requirements.txt
└── clinic.db
```

## 🏗️ Architecture

Le projet est organisé selon les 4 cercles de la Clean Architecture (Robert C. Martin) :

1. **Entities** (`domain/entities`) : objets métier purs (ex. `Doctor`, `Patient`). Ne dépendent de rien.
2. **Use Cases** (`domain/use_cases`) : règles métier applicatives (ex. `CreateDoctor`). Dépendent uniquement des entités.
3. **Interface Adapters** : couche de conversion entre les use cases et le monde extérieur.
   - `interfaces/di/main.py`, `menu.py` : *controllers* — orchestrent l'appel aux use cases.
   - `infrastructure/*_repository_impl.py` : *gateways* — implémentations concrètes des repositories consommés par les use cases.
4. **Frameworks & Drivers** : la couche la plus externe.
   - `infrastructure/database.py` : accès SQLite.
   - `interfaces/templates/*.html` : présentation web.

### Principe de dépendance
Les `use_cases` (ex. `CreateDoctor`) reçoivent leurs dépendances (repositories) par injection dans le constructeur, ce qui permet de découpler la logique métier de l'implémentation technique.

```python
class CreateDoctor:
    def __init__(self, doctor_repository):
        self.doctor_repository = doctor_repository

    def execute(self, nom, prenom, age, speciality, telephone, adresse, email):
        doctor = Doctor(...)
        return self.doctor_repository.save(doctor)
```

## ⚠️ Limites actuelles / axes d'amélioration

- Absence d'interfaces abstraites explicites (`ABC`/`Protocol`) pour les repositories dans le domaine : actuellement le typage est implicite (duck typing Python), ce qui fonctionne mais ne formalise pas l'inversion de dépendance (DIP).
- Une couche `domain/repositories/` (contrats) pourrait être ajoutée pour rapprocher le projet d'une Clean Architecture stricte.

## 🚀 Installation

```bash
pip install -r requirements.txt
python app.py
```

## 🛠️ Stack technique

- Python
- SQLite (`clinic.db`)
- HTML (templates pour l'interface)

## 📄 Licence

À définir.  

## Auteur
Dawenshy Amazan 















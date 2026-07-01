from dataclasses import dataclass
@dataclass
class Doctor:
    id: int
    nom: str
    prenom: str
    age: int
    specialite: str
    telephone: str
    adresse: str
    email: str
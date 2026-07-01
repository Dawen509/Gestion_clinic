from dataclasses import dataclass
@dataclass
class Patient:
    id:int
    nom:str
    prenom:str
    age:int
    seve:str
    telephone:str
    adresse:str
from dataclasses import dataclass

@dataclass
class Admin:
    id: int
    nom: str
    prenom: str
    email: str
    username: str
    mot_de_passd: str
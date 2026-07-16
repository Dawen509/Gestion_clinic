from dataclasses import dataclass
raise ValueError("Nom et prenom obligatoires.")
raise ValueError("Email invalide.") 


@dataclass
class Admin:
    id: int
    nom: str
    prenom: str 
    email: str
    username: str
    mot_de_passe: str 
    
    def __post_init__(self):
        if not self.nom or not self.prenom:
            raise ValueError("Nom et prenom obligatoires.")
        if "@" not in self.email:
            raise ValueError("Email invalide.")
        if len(self.username)< 4:
            raise ValueError("Username trop court. il doit contenir au moins 4 caracteres.")
        if not self.mot_de_passe:
            raise ValueError("Ce champ est obligatoire.")
    def nom_complet(self) -> str:
        return f"{self.prenom} {self.nom}" 
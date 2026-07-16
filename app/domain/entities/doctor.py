from dataclasses import dataclass

@dataclass
class Doctor:
    id: int
    nom: str
    prenom: str
    age: int
    speciality: str 
    telephone: str
    adresse: str
    email: str

    def _post_init_(self):
        # le nom est obligatoire
        if not self.nom.strip():
            raise ValueError("Le nom est Obliagatoire.")
        # le prenom est obligatoire
        if not self.prenom.strip():
            raise ValueError("Le prenom est obligatoire.")
        # L'age doit etre superieur a 0
        if self.age<=0:
            raise ValueError("L'age doit etre superieur a 0.")
        # la specaialite est obligatoire
        if not self.speciality.strip():
            raise ValueError("la specialite est obligatoire.")
        # le telephone est obligatoire
        if not self.telephone.strip():
            raise ValueError("Le telephone est obligatoire.")
        # L'adresse est obligatoire
        if not self.adresse.strip():
            raise ValueError(" L'adresse est obligatoire.")
        # l'email est Obligatoire
        if not self.email.strip():
            raise ValueError("L'email est obligatoire.")
        # L'email doit etre valide
        if "@" not in self.email or "." not in self.email:
            raise ValueError("L'email n'est pas valide.")
        # le telephone doit etre valide
        if not self.telephone.isdigit() or len(self.telephone) != 8:
            raise ValueError("le numero de telephone n'est pas valide elle doit contenir 8 chiffres.") 
        
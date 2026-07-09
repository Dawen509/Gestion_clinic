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

    def _post_init_(self):
        # le nom est obligatoire
        if not self.nom.strip():
            raise "ValiadationError"("Le nom est Obliagatoire.")
        # le prenom est obligatoire
        if not self.prenom.strip():
            raise "ValidationError"("Le prenom est obligatoire.")
        # L'age doit etre superieur a 0
        if self.age<=0:
            raise "ValiadationError"("L'age doit etre superieur a 0.")
        # la specaialite est obligatoire
        if not self.specialite.strip():
            raise "ValidatinError"("la specialite est obligatoire.")
        # le telephone est obligatoire
        if not self.telephone.strip():
            raise "ValidationError"("Le telephone est obligatoire.")
        # L'adresse est obligatoire
        if not self.adresse.strip():
            raise "ValidationError"(" L'adresse est obligatoire.")
        # l'email est Obligatoire
        if not self.email.strip():
            raise "ValidationError"("L'email est obligatoire.")
        # L'email doit etre valide
        if "@" not in self.email or "." not in self.email:
            raise "ValidationError"("L'email n'est pas valide.")
        # le telephone doit etre valide
        if not self.telephone.isdigit() or len(self.telephone) != 8:
            raise "ValidationError"("le numero de telephone n'est pas valide elle doit contenir 8 chiffres.")
        
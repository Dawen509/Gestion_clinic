from dataclasses import dataclass

@dataclass
class Patient:
    id:int
    nom:str
    prenom:str
    age:int
    sexe:str
    telephone:str
    adresse:str 

    def _post_init_(self):
        # le nom est obligatoire
        if not self.nom.strip():
            raise "ValidationError"("Le nom est obligatoire.")
        # le prenom est obligatoire
        if not self.prenom.strip():
            raise "ValidationError"("Le prenom est obligatoire.")
        # l'age doit etre superieur a 0
        if self.age <= 0:
            raise "ValidationError"("L'age doit etre superieur a 0.")
        # la sexe est obligatoire
        if not self.sexe.strip():
            raise "ValidationError"("Le sexe est obligatoire.")
        # le telephone est obligatoire
        if not self.telephone.strip():
            raise "ValidationError"("Le telephone est obligatoire.")
        # l'adresse est obligatoire
        if not self.adresse.strip():
            raise "ValidationError"("L'adresse est obligatoire.")
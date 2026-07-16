from app.infrastructure.database import get_connection
from app.domain.entities.patient import Patient

class PatientRepositoryImpl:

    def save(self, patient: Patient):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO patients
        VALUES(?,?,?,?,?,?,?)
        """, (
            patient.id,
            patient.nom,
            patient.prenom,
            patient.age,
            patient.sexe,
            patient.telephone,
            patient.adresse
        ))

        conn.commit()
        conn.close()

    def find_by_id(self, patient_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM patients WHERE id=?",
            (patient_id,)
        )

        row = cursor.fetchone()
        conn.close()

        if row:
            return Patient(
                id=row[0],
                nom=row[1],
                prenom=row[2],
                age=row[3],
                sexe=row[4],
                telephone=row[5],
                adresse=row[6]
            )

        return None

    def find_all(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM patients")
        rows = cursor.fetchall()
        conn.close()

        patients = []



        for row in rows:
            patients.append(
                Patient(
                    id=row[0],
                    nom=row[1],
                    prenom=row[2],
                    age=row[3],
                    sexe=row[4],
                    telephone=row[5],
                    adresse=row[6]
                )
            )

        return patients 
    def delete(self, patient_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
        "DELETE FROM patients WHERE id=?",
        (patient_id,)

        )

        conn.commit()
        conn.close()
    
from app.infrastructure.database import get_connection
from app.domain.entities.doctor import Doctor


class DoctorRepositoryImpl:

    def save(self, doctor: Doctor):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO doctors
        VALUES(?,?,?,?,?,?,?,?)
        """, (
            doctor.id,
            doctor.nom,
            doctor.prenom,
            doctor.age,
            doctor.speciality,
            doctor.telephone,
            doctor.adresse,
            doctor.email
        ))

        conn.commit()
        conn.close()

    def find_by_id(self, doctor_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM doctors WHERE id=?",
            (doctor_id,)
        )

        row = cursor.fetchone()

        conn.close()

        if row:
            return Doctor(*row)

        return None

    def find_all(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM doctors")

        rows = cursor.fetchall()

        conn.close()

        return [Doctor(*row) for row in rows]

    def delete(self, doctor_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM doctors WHERE id=?",
            (doctor_id,)
        )

        conn.commit()
        conn.close()
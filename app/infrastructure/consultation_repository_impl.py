from app.infrastructure.database import get_connection
from app.domain.entities.consultation import Consultation


class ConsultationRepositoryImpl:

    def create(self, consultation: Consultation):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO consultations
        VALUES(?,?,?,?,?,?,?,?,?)
        """, (
            consultation.id,
            consultation.patient_id,
            consultation.doctor_id,
            consultation.date,
            consultation.time,
            consultation.payment,
            consultation.diagnostic,
            consultation.treatment,
            consultation.observations,
        ))

        conn.commit()
        conn.close()

    def find_by_id(self, consultation_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM consultations WHERE id=?",
            (consultation_id,)
        )

        row = cursor.fetchone()
        conn.close()
        return row
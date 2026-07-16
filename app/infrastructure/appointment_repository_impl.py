from app.infrastructure.database import get_connection
from app.domain.entities.appointment import Appointment

class AppointmentRepositoryImpl:

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM appointments")
        rows = cursor.fetchall()

        conn.close()
        return rows

    def add(self, appointment):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO appointments
        VALUES(?,?,?,?,?,?,?,?)
        """, (
            appointment.id,
            appointment.patient_id,
            appointment.doctor_id,
            appointment.diagnostic_,
            appointment.date_rendezvous_.isoformat(),
            appointment.motif,
            appointment.time,
            appointment.status.value
        ))

        conn.commit()
        conn.close() 

    def get_by_id(self, appointment_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM appointments WHERE id=?", (appointment_id,))
        row = cursor.fetchone()
        conn.close()
        return row

def update(self, appointment):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE appointments
        SET patient_id=?, doctor_id=?, diagnostic_=?, date_rendezvous_=?, motif=?, time=?, status=?
        WHERE id=?
    """, (
        appointment.patient_id,
        appointment.doctor_id,
        appointment.diagnostic_,
        appointment.date_rendezvous_.isoformat(),
        appointment.motif,
        appointment.time,
        appointment.status.value,
        appointment.id
    ))
    conn.commit()
    conn.close()

def delete(self, appointment_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM appointments WHERE id=?", (appointment_id,))
    conn.commit()
    conn.close()    
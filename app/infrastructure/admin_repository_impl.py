from app.domain.repositories.admin_repository import AdminRepository
from app.infrastructure.database import get_connection


class AdminRepositoryImpl(AdminRepository):

    def create(self, admin):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO admin (username, password) VALUES (?, ?)",
            (admin["username"], admin["password"])
        )

        conn.commit()
        conn.close()

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM admin")
        admins = cursor.fetchall()

        conn.close()
        return admins

    def get_by_username(self, username):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM admin WHERE username = ?",
            (username,)
        )

        admin = cursor.fetchone()
        conn.close()

        return admin
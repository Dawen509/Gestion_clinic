class CreateAdmin:
    def __init__(self, admin_repository):
        self.admin_repository = admin_repository

    def execute(self, username, password):
        admin = {
            "username": username,
            "password": password
        }

        return self.admin_repository.create(admin)
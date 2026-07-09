class CreateAdin:
    def _init_(slef, admin_repository):
     def execute(self, username, password):
        admin = {
            "username": username,
            "password": password
        }
        return self.admin_repository.create(admin)
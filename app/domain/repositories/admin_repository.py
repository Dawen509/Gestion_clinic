class AdminRepository:
    def create(self, admin):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def get_by_username(self, username):
        raise NotImplementedError
from abc import ABC, abstractmethod

class DoctorRepository:
    pass     

    @abstractmethod
    def save(self, doctor):
        pass
    @abstractmethod
    def find_all(self):
        pass
    @abstractmethod
    def find_by_id(self, doctor_id):
        pass
    @abstractmethod
    def delete(self, doctor_id):
        pass
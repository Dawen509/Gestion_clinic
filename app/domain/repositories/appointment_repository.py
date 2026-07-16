from abc import ABC, abstractmethod

class AppointmentRepository(ABC):

    @abstractmethod
    def add(self, appointment):
        pass 
    @abstractmethod
    def get_by_id(self, appointment_id):
        pass 
    @abstractmethod
    def get_all(self):
        pass 
    @abstractmethod 
    def update(self, appointment):
        pass 
    @abstractmethod
    def delete(self, appointement_id):
        pass

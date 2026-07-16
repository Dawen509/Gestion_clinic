from abc import ABC, abstractmethod

class patientRepository(ABC):
    pass    

    @abstractmethod
    def save(self, patient):
        pass
    @abstractmethod
    def find_all(self):
        pass
    @abstractmethod
    def find_by_id(self, patient_id):
        pass
    @abstractmethod
    def delete(self, patient_id):
        pass 
    
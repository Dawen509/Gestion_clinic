from flask import Flask, render_template, request, redirect, url_for
from app.domain.entities.patient import Patient
from app.infrastructure.patient_repository_impl import PatientRepositoryImpl
from app.domain.use_cases.create_patient import CreatePatient
from app.domain.use_cases.find_patient import FindPatient
from app.domain.use_cases.list_patient import ListPatients
from app.domain.use_cases.delete_patient import DeletePatient
from app.infrastructure.admin_repository_impl import AdminRepositoryImpl 
from app.domain.use_cases.create_admin import CreateAdmin
from app.domain.entities.doctor import Doctor
from app.infrastructure.doctor_repository_impl import DoctorRepositoryImpl
from app.domain.use_cases.create_doctor import CreateDoctor 
from datetime import datetime
from app.domain.entities.appointment import Appointment
from app.infrastructure.appointment_repository_impl import AppointmentRepositoryImpl
from app.domain.use_cases.create_appointment import CreateAppointment
from app.domain.use_cases.create_consultation import CreateConsultation
from app.domain.entities.consultation import Consultation
from app.infrastructure.consultation_repository_impl import ConsultationRepositoryImpl  


app = Flask(__name__)
admin_repository = AdminRepositoryImpl()
create_admin = CreateAdmin(admin_repository)
repository = PatientRepositoryImpl()
create_patient = CreatePatient(repository)
doctor_repository = DoctorRepositoryImpl()
create_doctor = CreateDoctor(doctor_repository)
find_patient = FindPatient(repository)
list_patients = ListPatients(repository)
delete_patient = DeletePatient(repository)
appointment_repository = AppointmentRepositoryImpl()
create_appointment = CreateAppointment(appointment_repository) 
consultation_repository = ConsultationRepositoryImpl()
create_consultation = CreateConsultation(consultation_repository)

@app.route("/")
def index():
    patients = list_patients.execute()
    return render_template("index.html", patients=patients)

@app.route("/admin/add", methods=["POST"])
def add_admin():
    username = request.form["username"]
    password = request.form["password"]

    create_admin.execute(username, password)

    return "Administrateur ajouté avec succès !"

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        patient = Patient(
            id=None,
            nom=request.form["nom"],
            prenom=request.form["prenom"],
            age=int(request.form["age"]),
            sexe=request.form["sexe"],
            telephone=request.form["telephone"],
            adresse=request.form["adresse"],
        )
        create_patient.execute(patient)
        return "patient enregistre avec succèss !" 
        
    return render_template("add.html") 


@app.route("/add_doctor", methods=["GET", "POST"])
def add_doctor():
    if request.method == "POST":
        create_doctor.execute(
            nom=request.form["nom"],
            prenom=request.form["prenom"],
            age=int(request.form["age"]),
            speciality=request.form["specialite"],
            telephone=request.form["telephone"],
            adresse=request.form["adresse"],
            email=request.form["email"]
        )
        return "Docteur enregistré avec succès !"
    return render_template("add_doctor.html") 

@app.route("/add_consultation", methods=["GET", "POST"])
def add_consultation():
    if request.method == "POST":
        date_consultation = datetime.strptime(request.form["date"], "%Y-%m-%d")
        consultation = Consultation(
            id=None,
            patient_id=int(request.form["patient_id"]),
            doctor_id=int(request.form["doctor_id"]),
            date=date_consultation,
            time=request.form["time"],
            payment=float(request.form["payment"]),
            diagnostic=request.form["diagnostic"],
            treatment=request.form["treatment"],
            observations=request.form["observations"],
        )
        create_consultation.execute(consultation)
        return "Consultation enregistrée avec succès !"

    return render_template("add_consultation.html") 

@app.route("/add_appointment", methods=["GET", "POST"])
def add_appointment():
    if request.method == "POST":
        date_rendezvous_ = datetime.strptime(
            request.form["date_rendezvous_"], "%Y-%m-%d"
        )
        create_appointment.execute(
            patient_id=int(request.form["patient_id"]),
            doctor_id=int(request.form["doctor_id"]),
            date_rendezvous_=date_rendezvous_,
            motif=request.form["motif"],
            time=request.form["time"]
        )
        return "Rendez-vous enregistré avec succès !"
    return render_template("add_appointment.html") 



@app.route("/delete/<int:patient_id>")
def delete(patient_id):
    delete_patient.execute(patient_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True) 
    
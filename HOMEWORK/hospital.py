import tkinter as tk
import random

root = tk.Tk()
root.title("Hospital Game")
root.geometry("500x400")

score = 0
patients = []

score_label = tk.Label(root, text="Score: 0", font=("Arial", 16))
score_label.pack(pady=10)

patient_label = tk.Label(root, text="No Patients", font=("Arial", 14))
patient_label.pack(pady=20)

def new_patient():
    names = ["Rahul", "Priya", "Amit", "Neha", "Rohan"]
    diseases = ["Fever", "Cold", "Headache", "Cough", "Infection"]

    patient = f"{random.choice(names)} - {random.choice(diseases)}"
    patients.append(patient)

    patient_label.config(text=f"Patient: {patient}")

def treat_patient():
    global score

    if patients:
        patients.pop(0)
        score += 10
        score_label.config(text=f"Score: {score}")
        patient_label.config(text="Patient Treated!")

        root.after(2000, new_patient)

add_btn = tk.Button(root, text="New Patient", font=("Arial", 12),
                    command=new_patient)
add_btn.pack(pady=10)

treat_btn = tk.Button(root, text="Treat Patient", font=("Arial", 12),
                      command=treat_patient)
treat_btn.pack(pady=10)

root.mainloop()
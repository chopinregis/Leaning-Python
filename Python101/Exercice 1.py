import tkinter as tk
from tkinter import ttk
import pandas as pd

# Initialisation des données
data = pd.DataFrame(columns=["Patient", "Médicament"])

def ajouter_donnees():
    global data
    # Récupérer les valeurs des entrées
    patient = patient_entry.get()
    medicament = medicament_entry.get()
    # Ajouter au DataFrame
    data = data.append({"Patient": patient, "Médicament": medicament}, ignore_index=True)
    # Mise à jour de l'affichage
    update_display()

def update_display():
    for i in tree.get_children():
        tree.delete(i)
    for index, row in data.iterrows():
        tree.insert("", "end", values=(row["Patient"], row["Médicament"]))

# Création de la fenêtre principale
root = tk.Tk()
root.title("Gestion des Patients et Médicaments")

# Création des widgets
patient_label = tk.Label(root, text="Nom du Patient:")
patient_entry = tk.Entry(root, width=50)
medicament_label = tk.Label(root, text="Médicament:")
medicament_entry = tk.Entry(root, width=50)
ajouter_button = tk.Button(root, text="Ajouter", command=ajouter_donnees)
tree = ttk.Treeview(root, columns=("Patient", "Médicament"), show="headings")
tree.heading("Patient", text="Patient")
tree.heading("Médicament", text="Médicament")

# Positionnement des widgets
patient_label.grid(row=0, column=0, padx=10, pady=10)
patient_entry.grid(row=0, column=1, padx=10, pady=10)
medicament_label.grid(row=1, column=0, padx=10, pady=10)
medicament_entry.grid(row=1, column=1, padx=10, pady=10)
ajouter_button.grid(row=2, columnspan=2, pady=10)
tree.grid(row=3, columnspan=2, padx=10, pady=10, sticky="nsew")

# Configuration de l'expansion du tableau
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(1, weight=1)

# Lancement de l'application
root.mainloop()

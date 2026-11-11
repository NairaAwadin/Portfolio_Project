from data import PROJECTS
import csv
import os
from datetime import datetime

def all_tags(projects):
    """
    Renvoie la liste triée des tages uniques des projets
    """
    tags = set()
    for project in projects:
        for tag in project["tags"]:
            tags.add(tag)
    sorted_tags = sorted(tags)
    return sorted_tags

def filter_projects(projects, chosen):
    """
    Renvoie les projets ayant au moins un tag choisi 
    et tous si aucun tag n'est choisi
    """
    list_projets = []

    if not chosen:
        return projects

    for project in projects:
        for tag in project["tags"]:
            if tag in chosen:
                list_projets.append(project)
                break

    return list_projets

def get_year(project):
    """
    Renvoie l'année du projet
    """
    return project["year"]

def check_informations(name, email, message):
    """
        Renvoie True si le nom, l'email et le message sont valides
    """
    valid = True
    if name.strip() == "":
        valid = False

    if "@" not in email or "." not in email:
        valid = False

    if len(message) < 10:
        valid = False

    return valid

def save_emails(name, email, message):
    """
    Ajoute un message à messages.csv ou le creér si il n y a pas de messages.csv

    Quest 13: on ouvre le fihcier en "a", parce qu'on ce qu'on veut c'est ajouter le message à notre csv, donc le append.
    si on utilise "w" c'est write, et enft cv supprimer ce qu'on avait dans le fichier et le récrire de 0.
    """
    file_exist = os.path.exists("messages.csv")
    with open("messages.csv", "a", newline="", encoding="utf-8") as file:
        file_csv = csv.writer(file)

        if not file_exist:
            file_csv.writerow(["Date", "Nom", "Email", "Message"])

        file_csv.writerow([datetime.now().strftime("%d/%m/%Y %H:%M"), name, email, message])

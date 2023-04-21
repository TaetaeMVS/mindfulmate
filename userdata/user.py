# userdata/user.py
from PyQt6.QtWidgets import QInputDialog
import json
import os
class User:
    def __init__(self, name=None, age=None, occupation=None, interests=None):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.interests = interests if interests else []

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_occupation(self, occupation):
        self.occupation = occupation

    def add_interest(self, interest):
        self.interests.append(interest)
        
    def set_interests(self, interests):
        self.interests = interests

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_occupation(self):
        return self.occupation

    def get_interests(self):
        return self.interests

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "occupation": self.occupation,
            "interests": self.interests
        }
        
    def update_user(self, parent):
        # Request user input
        name, ok = QInputDialog.getText(parent, 'Name', 'Please enter your name:')
        if ok:
            parent.user.name = name

        age, ok = QInputDialog.getInt(parent, 'Age', 'Please enter your age:', min=1)
        if ok:
            parent.user.age = age

        occupation, ok = QInputDialog.getText(parent, 'Occupation', 'Please enter your occupation:')
        if ok:
            parent.user.occupation = occupation

        interests, ok = QInputDialog.getText(parent, 'Interests', 'Please enter your interests (comma-separated):')
        if ok:
            parent.user.interests = [interest.strip() for interest in interests.split(',')]
        self.export_user_data()

    # Function to export user data3
    def export_user_data(self):
        with open('userdata/user_data.json', 'w') as outfile:
            json.dump(self.to_dict(), outfile)
            
    def load_user_data(self, parent):
        # check if user_data.json file exists
        if not os.path.exists('userdata/user_data.json'):
            self.update_user(parent)
            return
        with open('userdata/user_data.json', 'r') as f:
            data = json.load(f)
            parent.user.set_age(data['age'])
            parent.user.set_name(data['name'])
            parent.user.set_occupation(data['occupation'])
            parent.user.set_interests(data['interests'])
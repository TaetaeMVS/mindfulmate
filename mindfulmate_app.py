import sys
from dotenv import load_dotenv
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
import openai
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class MindfulMateApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Mindful Mate")
        self.resize(1920, 1080)
        
        # Create widgets
        self.chat_box = QTextEdit(self)
        self.chat_box.setReadOnly(True)
        self.input_box = QLineEdit(self)
        self.send_button = QPushButton("Send", self)
        
        # Connect send button to send_message method
        self.send_button.clicked.connect(self.send_message)
        
        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.chat_box)
        layout.addWidget(self.input_box)
        layout.addWidget(self.send_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # Set font size 
        self.chat_box.setFontPointSize(16)
        
        # Show welcome message
        welcome_msg = self.initial_openai_response()
        self.chat_box.append(f"Mindful Mate: {welcome_msg}")
        
    def send_message(self):
        user_message = self.input_box.text().strip()
        if user_message:
            self.chat_box.append(f"User: {user_message}")
            self.input_box.clear()
            
            response = self.get_openai_response(user_message)
            msg = response['choices'][0]['message']['content']
            self.chat_box.append(f"Mindful Mate: {msg}")
            
    def get_openai_response(self, message):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Mindful Mate, a virtual wellbeing and lifestyle assistant. Please provide helpful answers while being thoughtful, kind and motivating."},
                {"role": "user", "content": message}
            ]
        )
        return response
    
    def initial_openai_response(self):
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Mindful Mate, a virtual wellbeing and lifestyle assistant. Please provide helpful answers while being thoughtful, kind and motivating. Give a short welcome to the user."},
            ]
        )
        return response['choices'][0]['message']['content']
        
    
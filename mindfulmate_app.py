from dotenv import load_dotenv
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget, QInputDialog
from PyQt6.QtCore import Qt
import openai
from userdata.user import User
import semantic_kernel as sk
from semantic_kernel.ai.open_ai import OpenAITextCompletion

kernel = sk.Kernel()
load_dotenv()
api_key = sk.openai_settings_from_dot_env()
kernel.config.add_text_backend("davinci-003", OpenAITextCompletion("text-davinci-003", api_key))
useAzureOpenAI = False
openai.api_key = os.getenv("OPENAI_API_KEY")

class MindfulMateApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.user = User()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Mindful Mate")
        self.resize(1920, 1080)
        
        # Create widgets
        self.chat_box = QTextEdit(self)
        self.chat_box.setReadOnly(True)
        self.input_box = QLineEdit(self)
        self.send_button = QPushButton("Send", self)
        self.settings_button = QPushButton("Update user data", self)
        self.settings_button.clicked.connect(self.update_settings)

        
        # Connect send button to send_message method
        self.send_button.clicked.connect(self.send_message)
        
        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.chat_box)
        layout.addWidget(self.input_box)
        layout.addWidget(self.send_button)
        layout.addWidget(self.settings_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # Load user data
        self.user.load_user_data(self)
        
        # Load skills
        skills_directory = "./skills"
        assistantFunctions = kernel.import_semantic_skill_from_directory(skills_directory, "assistant")
        welcome_function = assistantFunctions["welcome"]
        
        # Set font size 
        self.chat_box.setFontPointSize(16)
        
        # Show welcome message
        # welcome_msg = self.initial_openai_response()
        welcome_msg = welcome_function(self.user.to_dict())
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
            # You are Mindful Mate, a virtual wellbeing and lifestyle assistant. Please provide helpful answers while being thoughtful, kind and motivating.
            messages=[
                {"role": "system", "content": "You are Mindful Mate, a virtual wellbeing and lifestyle assistant. Please provide helpful answers while being thoughtful, kind and motivating."},
                {"role": "user", "content": message}
            ]
        )
        return response
    
    # You are Mindful Mate, a virtual wellbeing and lifestyle assistant. Please provide helpful answers while being thoughtful, kind and motivating. Give a short welcome to the user.
    def initial_openai_response(self):
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Mindful Mate, a virtual wellbeing and lifestyle assistant. Please provide helpful answers while being thoughtful, kind and motivating. Give a short welcome to the user. You do not need to repeat information back to them, pretend you have known them for a while and you are a close friend who they can trust."},
                {"role": "user", "content": f"My name is {self.user.name} and I am {self.user.age} years old. I am a {self.user.occupation} and I am interested in {self.user.interests}."}
            ]
        )
        return response['choices'][0]['message']['content']
        
    def update_settings(self):
        self.user.update_user(self)

        
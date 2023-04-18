import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
import openai


class MindfulMateApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Mindful Mate")
        self.resize(800, 600)
        
    
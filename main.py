import sys
import os
from dotenv import load_dotenv
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from mindfulmate_app import MindfulMateApp
import openai
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    # Create a QApplication instance (required for any PyQt application)
    app = QApplication(sys.argv)

    # Create a QMainWindow instance (the main application window)
    window = MindfulMateApp()

    # Set the title of the main window
    window.setWindowTitle("MindfulMate")

    # Set the size of the main window
    window.resize(1920, 1080)

    # Show the main window
    window.show()

    # Start the PyQt event loop and exit the application when the main window is closed
    sys.exit(app.exec())

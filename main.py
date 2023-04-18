import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

class MindfulMateApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Mindful Mate")
        self.resize(800, 600)


if __name__ == "__main__":
    # Create a QApplication instance (required for any PyQt application)
    app = QApplication(sys.argv)

    # Create a QMainWindow instance (the main application window)
    window = MindfulMateApp()

    # Set the title of the main window
    window.setWindowTitle("Hello, World!")

    # Create a QLabel instance with the text "Hello, World!" and set its parent to the main window
    label = QLabel("Hello, World!", parent=window)

    # Move the label to a specific position within the main window
    label.move(100, 50)

    # Set the size of the main window
    window.resize(300, 200)

    # Show the main window
    window.show()

    # Start the PyQt event loop and exit the application when the main window is closed
    sys.exit(app.exec())

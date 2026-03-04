from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
import os

class UpdateScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Runtimeeee - Updates")
        self.setGeometry(300, 200, 400, 300)
        layout = QVBoxLayout()

        layout.addWidget(QLabel("What's New:"))

        text = "No updates."
        if os.path.exists("config/updates.txt"):
            with open("config/updates.txt") as f:
                text = f.read()

        text_box = QTextEdit()
        text_box.setReadOnly(True)
        text_box.setText(text)
        layout.addWidget(text_box)

        btn = QPushButton("Continue")
        btn.clicked.connect(self.close)
        layout.addWidget(btn)

        self.setLayout(layout)

from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget

class RuntimeeeeMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Runtimeeee")
        self.setGeometry(100, 100, 600, 400)

        container = QWidget()
        layout = QVBoxLayout()

        # Placeholder for ISO/USB boot buttons
        layout.addWidget(QLabel("ISO boot and USB boot buttons go here (simulated)"))

        # Footer notice
        footer = QLabel("For most Windows ISO files, you may need a product key.")
        layout.addWidget(footer)

        container.setLayout(layout)
        self.setCentralWidget(container)

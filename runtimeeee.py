from PySide6.QtWidgets import QApplication
from ui.update_screen import UpdateScreen
from ui.main_window import RuntimeeeeMainWindow
import sys

app = QApplication(sys.argv)

# Show update screen
update = UpdateScreen()
update.show()
app.exec()

# Show main window
main = RuntimeeeeMainWindow()
main.show()
sys.exit(app.exec())

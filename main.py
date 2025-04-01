import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


from PyQt5.QtWidgets import QApplication
import sys
from src.gui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
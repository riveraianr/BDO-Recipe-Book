
import sys
from PyQt5.QtWidgets import QApplication
from ui_main import RecipeBookUI
import app_config

def main():
    app = QApplication(sys.argv)
    window = RecipeBookUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

import sys
import os
from PySide2.QtWidgets import QApplication

from lib.views.login_view import LoginView
from lib.views.main_view import MainView

# * APPLICATION - ENTRY POINT
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # * ----------- UI FILES -------------
    # Compile QT.ui files to Python.py | Update changes on .ui files
    os.system("pyside2-uic ./ui/loginUI.ui -o ./ui/compiled/loginUI.py --from-imports ./ui/compiled")
    os.system("pyside2-uic ./ui/mainUI.ui -o ./ui/compiled/mainUI.py --from-imports ./ui/compiled")
    os.system("pyside2-rcc ./ui/src.qrc -o ./ui/compiled/src_rc.py")

    # * --------- QT APPLICATION ---------
    # Main application
    app = QApplication(sys.argv)
    # Views
    login_view = LoginView()
    main_view = MainView()
    login_view.main_view = main_view
    main_view.login_view = login_view

    # * --------- START ---------
    login_view.show()

    sys.exit(app.exec_())

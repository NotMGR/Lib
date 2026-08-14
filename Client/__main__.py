import sys, logging

from utils import resource_path
from pathlib import Path

from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtGui import QIcon

from GUI.MainWindow import MainWindow
from logic.server import Server_Dialog

from api import test_server_connection
from settings import load_config

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/errors.log",
    level=logging.ERROR,
    format="%(asctime)s — %(levelname)s — %(message)s"
)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    qss_path = resource_path("GUI/style.qss")

    with open(qss_path, "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    app.setWindowIcon(
        QIcon(str(resource_path("images/icons/lib_icon.ico")))
    )

    config = load_config()
    server_url = config.get("server", "").strip().rstrip("/")

    # No saved server, or saved server isn't reachable.
    if not server_url or not test_server_connection(server_url):

        dialog = Server_Dialog()

        if dialog.exec() != QDialog.DialogCode.Accepted:
            sys.exit(0)

    # At this point we have a valid server.
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
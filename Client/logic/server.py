from PySide6.QtWidgets import QMessageBox, QDialog
from GUI.server_dialog import Ui_server_dialog

import requests

from settings import load_config, save_config

class Server_Dialog(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_server_dialog()
        self.ui.setupUi(self)

        config = load_config()

        self.ui.server_url_line_edit.setText(
            config.get("server", "")
        )

        self.ui.ok_cancel_button.accepted.connect(self.save_settings)
        self.ui.test_connection_button.clicked.connect(self.test_connection)
    def save_settings(self):
        server_url = self.ui.server_url_line_edit.text().strip()

        if not server_url:
            QMessageBox.warning(
                self,
                "Invalid Server",
                "Please enter a server URL."
            )
            return

        try:
            response = requests.get(
                f"{server_url}/",
                timeout=5
            )
            response.raise_for_status()

            if response.json().get("status") != "Backend is running":
                QMessageBox.warning(
                    self,
                    "Invalid server",
                    "The server responded, but something went wrong."
                )
                return

        except requests.RequestException as e:
            QMessageBox.critical(
                self,
                "Connection Failed",
                f"Could not connect to the server."
            )
            return
        
        config = load_config()
        config["server"] = server_url

        save_config(config)

        QMessageBox.information(
            self,
            "Settings saved",
            "Server address saved successfully."
        )

        self.accept()

    def test_connection(self):
        server_url = self.ui.server_url_line_edit.text().strip().rstrip("/")

        if not server_url:
            QMessageBox.warning(
                self,
                "Invalid Server",
                "Please enter a server URL."
            )
            return

        try: 
            response = requests.get(
                f"{server_url}/",
                timeout=5
            )
            response.raise_for_status()

            data = response.json()

            if data.get("status") == "Backend is running":
                self.ui.connection_status_label.setText("Success")

            else:
                self.ui.connection_status_label.setText("Failed")
                return

        except requests.RequestException as e:
            self.ui.connection_status_label.setText("Failed")
            
            return
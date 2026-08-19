from PySide6.QtWidgets import QMessageBox, QDialog, QButtonGroup

import requests
import api

from GUI.add_union_dialog import Ui_Union_Dialog

class Union_Dialog(QDialog):
    def __init__(self, mode="create"):
        super().__init__()
        self.ui = Ui_Union_Dialog()
        self.ui.setupUi(self)

        self.mode = mode

        if self.mode == "edit":
            self.setWindowTitle("Edit Unions")

            load_union_cbox(self, self.ui.edit_union_cbox)

            self.ui.edit_union_cbox.currentIndexChanged.connect(self.load_union)
            self.ui.ok_cancel_button_box.accepted.connect(self.update_union)

        else:
            self.setWindowTitle("Add Union")
            self.ui.edit_union_cbox.hide()
            self.ui.union_label.hide()
            self.ui.ok_cancel_button_box.accepted.connect(self.add_union)

    def add_union(self):
        union_name = self.ui.union_name_line_edit.text().strip().lower()
        if not union_name:
            QMessageBox.warning(
                self,
                "Error",
                "Union name cannot be empty."
            )
            return

        new_union_data = {
            "name": union_name
        }
        try:
            api.create_union(new_union_data)

            QMessageBox.information(
                self,
                "Success",
                "Union Created."
            )
            self.accept()

        except requests.HTTPError as e:
            QMessageBox.warning(
                self,
                "Error.",
                api.handle_api_error(e)                
            )

    def update_union(self):
        union_id = self.ui.edit_union_cbox.currentData()
        new_union_name = self.ui.union_name_line_edit.text().strip()

        if union_id is None:
            QMessageBox.warning(
                self, 
                "Error",
                "Please select a union first."
            )
            return

        if not new_union_name:
            QMessageBox.warning(
                self,
                "Error",
                "Union name cannot be empty."
            )
            return

        new_union_data = {
            "name": new_union_name
        }

        try:
            api.update_union(union_id, new_union_data)

            QMessageBox.information(
                self,
                "Success.",
                "Union updated."
            )

            self.accept()

        except requests.HTTPError as e:
            QMessageBox.critical(
                self,
                "Error",
                api.handle_api_error(e)
            )

    def load_union(self):
        self.ui.union_name_line_edit.setText(self.ui.edit_union_cbox.currentText())


def load_union_cbox(self, cbox):
    try:
        union_list = api.fetch_unions()

    except requests.HTTPError as e:
        QMessageBox.warning(
            self,
            "Could not load unions",
            api.handle_api_error(e)
        )
        return

    except requests.RequestException:
        QMessageBox.warning(
            self,
            "Connection Error",
            "Could not connect to the Lib server."
        )
        return

    if not union_list:
        return

    union_list.sort(key=lambda union: union["name"].lower())

    cbox.blockSignals(True)

    try:
        cbox.clear()

        for union in union_list:
            cbox.addItem(
                union["name"].title(),
                union["id"]
            )

        cbox.setCurrentIndex(-1)

    finally:
        cbox.blockSignals(False)

    cbox.view().setMinimumWidth(150)
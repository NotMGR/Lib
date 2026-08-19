from PySide6.QtWidgets import QMessageBox, QDialog, QButtonGroup

import requests
import api

from GUI.add_user_dialog import Ui_Dialog
from GUI.edit_user_dialog import Ui_edit_user_dialog


class User_dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.choice_group = QButtonGroup(self)

        load_union_cbox(self, self.ui.edit_union_cbox)

        self.ui.active_radio_button_yes.setChecked(True)

        self.choice_group.addButton(self.ui.active_radio_button_yes, 1)
        self.choice_group.addButton(self.ui.active_radio_button_no, 0)

        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.buttonBox.accepted.connect(self.add_user)

        self.ui.delete_user_button.hide()

    
    def add_user(self):
        try:
            user_name = self.ui.add_user_line_edit.text().strip()

            if not user_name:
                QMessageBox.warning(
                    self,
                    "Error",
                    "Please enter a valid username.",
                )
                return
            
            is_active = self.choice_group.checkedId()

            user_data = {
                "username": user_name,
                "is_active": is_active,
                "union_id": self.ui.edit_union_cbox.currentData()
            }

            api.create_user(user_data)

            QMessageBox.information(
                self,
                "Success.",
                f"{user_name} was added successfully.",
            )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error.",
                f"Failed to add user", 
            )        

class Edit_User_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_edit_user_dialog()
        self.ui.setupUi(self)
        self.load_user_cbox()
        load_union_cbox(self, self.ui.edit_union_cbox)
        
        self.ui.edit_user_cbox.currentIndexChanged.connect(self.load_user)
        
        self.ui.edit_user_button_box.accepted.disconnect()
        self.ui.edit_user_button_box.accepted.connect(self.update_user)
        self.ui.edit_user_button_box.rejected.connect(self.reject)

        self.choice_group = QButtonGroup(self)

        self.choice_group.addButton(self.ui.edit_user_active_radio_button_yes, 1)
        self.choice_group.addButton(self.ui.edit_user_active_radio_button_no, 0)

        #Hiding the delete button
        self.ui.delete_user_button.hide()

    def load_user_cbox(self):
        user_list = api.fetch_users()
        user_list.sort(key=lambda username: username["username"].lower())

        for item in user_list:
            self.ui.edit_user_cbox.addItem(item["username"].title(), {"id": item["id"], "is_active": item["is_active"]})

        self.ui.edit_user_cbox.setCurrentIndex(-1) 
        self.ui.edit_user_cbox.view().setMinimumWidth(150)

    def load_user(self):
        user_data = self.ui.edit_user_cbox.currentData()
        if not user_data:
            return
        
        self.current_user_id = user_data["id"]

        is_active = user_data["is_active"]
        if is_active:
            self.ui.edit_user_active_radio_button_yes.setChecked(True)
        
        else:
            self.ui.edit_user_active_radio_button_no.setChecked(True)
        
        self.ui.edit_user_line_edit.setText(self.ui.edit_user_cbox.currentText())
    
    def update_user(self):

        user = self.ui.edit_user_cbox.currentData()
        user_id = user["id"]
        username = self.ui.edit_user_line_edit.text().strip()

        if not username:
            QMessageBox.warning(
                self,
                "Error",
                "Please enter a valid username."
            )

        user_data = {
            "username": username,
            "is_active": self.choice_group.checkedId(),
            "union_id": self.ui.edit_union_cbox.currentData()
        } 
        try:
            api.update_user(user_id, user_data)

            QMessageBox.information(
                self,
                "Success",
                "User updated."
            )
            self.accept()

        except requests.HTTPError as e:
            QMessageBox.warning(
                self,
                "Error.",
                api.handle_api_error(e)
            )

def load_union_cbox(self, combo):
    try:
        union_list = api.fetch_unions()

    except requests.HTTPError as e:
        QMessageBox.warning(
        self,
        "Could not load unions",
        api.handle_api_error(e)
    )   
        
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

    for union in union_list:
        combo.addItem(union["name"].title(), union["id"])

    combo.setCurrentIndex(-1)
    combo.view().setMinimumWidth(150)
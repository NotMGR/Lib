from PySide6.QtWidgets import QMessageBox, QDialog
from PySide6.QtCore import Signal

import api, requests

from GUI.edit_raid_dialog import Ui_edit_raid_dialog


class Raid_Dialog(QDialog):
    raid_created = Signal()
    raid_updated = Signal()
    raid_deleted = Signal()

    def __init__(self, mode="create"):
        super().__init__()
        self.ui = Ui_edit_raid_dialog()
        self.ui.setupUi(self)
        self.mode = mode

        if self.mode == "edit":
            self.setWindowTitle("Edit Raid")
            
            from logic.mock_damage import load_raids
            load_raids(self.ui.edit_user_raid_cbox)

            self.ui.edit_user_raid_cbox.currentIndexChanged.connect(self.load_raid_values)
            self.ui.edit_raid_buttonBox.accepted.connect(self.update_raid)
            self.ui.delete_raid_button.clicked.connect(self.delete_raid)
        
        else:
            self.setWindowTitle("Add Raid")
            self.ui.edit_user_raid_cbox.hide()
            self.ui.label.hide() #Select Raid Label
            self.ui.edit_raid_buttonBox.accepted.connect(self.create_raid_and_bosses)


        self.load_elements()
        self.raid_id = None

        self.ui.edit_raid_buttonBox.rejected.connect(self.reject)
    
    def load_elements(self):
        boss_element_cbox = [
                'boss_element_box_1',
                'boss_element_box_2',
                'boss_element_box_3',
                'boss_element_box_4',
                'boss_element_box_5'
            ]
                    
        self.element_list = [
            ('Fire', 'fire'),
            ('Wind', 'wind'),
            ('Water', 'water'),
            ('Iron', 'iron'),
            ('Electric', 'electric')
        ]

        self.element_list.sort(key=lambda x: x[0].lower())
        
        for cbox in boss_element_cbox:
            cbox_object = getattr(self.ui, cbox, None)
            if cbox_object:
                cbox_object.clear()
                for text, data in self.element_list:
                    cbox_object.addItem(text, data)
    
    def load_raid_values(self): #Load the raid values into the fields for editing

        self.raid_id = self.ui.edit_user_raid_cbox.currentData() #This is the select raid cbox
        raid_info = api.fetch_raid_info(self.raid_id)

        if not raid_info:
            return

        for index, boss in enumerate(raid_info["bosses"], start=1):
            name_line = getattr(self.ui, f"boss_name_line_edit_{index}", None)
            weakness_cbox = getattr(self.ui, f"boss_element_box_{index}", None)

            name_line.setText(boss["name"])

            weakness_cbox.setCurrentIndex(
                weakness_cbox.findData(boss["weakness"])
            )

        self.ui.edit_raid_name_line_edit.setText(raid_info["name"])
    
    def update_raid(self):
        raid_id = self.ui.edit_user_raid_cbox.currentData() #This is the raid cbox.
        raid_obj = api.fetch_raid_info(raid_id)
            
        if not raid_obj:
            QMessageBox.information(
                self,
                "Raid Missing",
                "Please select a raid first."
            )
            return
        
        raid_name = self.ui.edit_raid_name_line_edit.text().strip()
        
        if not raid_name:
            QMessageBox.warning(
                self,
                "Error",
                "Raid name cannot be empty."
            )
            return

        raid_info = {
            "name": raid_name,
            "bosses": []
        }

        for index, boss in enumerate(raid_obj["bosses"], start=1):
            name_line = getattr(self.ui, f"boss_name_line_edit_{index}", None)
            weakness_cbox = getattr(self.ui, f"boss_element_box_{index}", None)
            
            if not name_line or not weakness_cbox:
                continue
            
            boss_name = (
                name_line.text().strip()
            )
            
            if not boss_name:
                QMessageBox.warning(
                    self,
                    "Error",
                    f"Boss {index} name is empty."
                )
                return
            
            boss_data = {
                "id": boss["id"],
                "name": boss_name,
                "weakness": weakness_cbox.currentData()
            }

            raid_info["bosses"].append(boss_data)

        try:
            api.update_raid(raid_obj["id"], raid_info)

        except requests.HTTPError as e:
            QMessageBox.warning(
                self,
                "Error.",
                api.handle_api_error(e)
            )

        self.raid_updated.emit()
        QMessageBox.information(
            self,
            "Success",
            "The raid has been updated."
        )

        self.accept()

    def create_raid_and_bosses(self):
        try:
            #RAID DEFINITION
            raid_name = self.ui.edit_raid_name_line_edit.text().strip()
            if not raid_name:
                QMessageBox.warning(self, "Error", "Raid name cannot be empty")
                return

            raid_data = {
                "name": raid_name,
                "bosses": []
            }

            for i in range(1, 6): #ADDING BOSSES
                boss_name_obj = getattr(self.ui, f"boss_name_line_edit_{i}", None)
                boss_weakness_obj = getattr(self.ui, f"boss_element_box_{i}", None)

                if not boss_name_obj or not boss_weakness_obj:
                    return None

                boss_name = boss_name_obj.text().strip()
                boss_weakness = boss_weakness_obj.currentText().strip().lower()

                if not boss_name or not boss_weakness:
                    QMessageBox.warning(
                        self,
                        "Missing boss information.",
                        "Please fill all name and weakness fields before clicking OK.",
                    )
                    return
                
                boss_data = {
                "name": boss_name,
                "weakness": boss_weakness,
            }

                raid_data["bosses"].append(boss_data)

            if raid_data:
                print(raid_data)
                api.create_raid(raid_data)

                QMessageBox.information(
                    self,
                    "Success",
                    "Raid Created Successfully."
                )
                self.raid_created.emit()
        except requests.HTTPError as e:
            QMessageBox.warning(
                self,
                "Error.",
                api.handle_api_error(e)
            )

                
    def delete_raid(self):        
        confirm = QMessageBox.question(
            self,
            "Delete Raid",
            f"Are you sure you want to delete this raid and all it's records?"
        )

        if confirm != QMessageBox.StandardButton.Yes:
            return
        
        api.delete_raid(self.raid_id)

        self.raid_deleted.emit()
        QMessageBox.information(
            self,
            "Success", 
            "Raid has been deleted."
        )

        self.accept()

def get_raid_id(raid_cbox):
    return raid_cbox.currentData()
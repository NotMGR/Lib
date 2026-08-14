from PySide6.QtWidgets import QMessageBox, QDialog, QFileDialog
from PySide6.QtCore import Qt

import requests, os, api
from logic.image_loader import get_pixmap

from GUI.edit_nikke_dialog import Ui_Edit_Nikke_Dialog

class Nikke_Dialog(QDialog):
    def __init__(self, mode="create"):
        super().__init__()
        self.ui = Ui_Edit_Nikke_Dialog()
        self.ui.setupUi(self)
        self.mode = mode
        
        cboxes = [
            self.ui.select_nikke_cbox,
            self.ui.nikke_role_box,
            self.ui.nikke_burst_box,
            self.ui.nikke_manuf_box,
            self.ui.nikke_element_box
        ]

        if self.mode == "edit":
            self.setWindowTitle("Edit Nikke")
            self.load_nikke_cbox()
            
            self.ui.select_nikke_cbox.currentIndexChanged.connect(self.load_nikke)
            self.ui.delete_nikke_button.clicked.connect(self.delete_nikke)
            
        
        else:
            self.setWindowTitle("Add Nikke")
            self.ui.select_nikke_cbox.hide()
            self.ui.select_nikke_label.hide()
            self.ui.delete_nikke_button.hide()


        self.load_bursts()
        self.load_manuf()
        self.load_role()
        self.load_element()

        for item in cboxes:
            item.setCurrentIndex(-1)

        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.buttonBox.accepted.connect(self.on_accept)
        self.ui.nikke_select_image_button.clicked.connect(self.get_nikke_image)

        self.current_image_path = None
        self.selected_local_image = None

    def add_nikke(self):
        try:
            nikke_data = self.validate_nikke_inputs()

            if nikke_data is None:
                return

            if not self.selected_local_image:
                QMessageBox.warning(
                self,
                "No Image selected.",
                "Please select an image."
                )
                return
        
            image_response = api.upload_nikke_image(self.selected_local_image)
            print(image_response)

            nikke_data["image_path"] = image_response["image_path"]
            
            api.create_nikke(nikke_data)

            QMessageBox.information(
                self,
                "Success.",
                f"Nikke was added successfully.",
            )

        except Exception as e:
            try:
                detail = e.response.json()["detail"]

            except Exception:
                detail = str(e)

            QMessageBox.critical(
                self,
                "Error.",
                detail, 
            )        
    
    def load_nikke(self, _):
        nikke = self.ui.select_nikke_cbox.currentData()

        if nikke is None:
                return
            
        nikke = api.fetch_nikke(nikke["id"])
        
        self.current_nikke_id = nikke["id"] #Variable used in update_nikke

        self.ui.nikke_name_line_edit.setText(nikke["name"])

        ele_index = self.ui.nikke_element_box.findData(nikke["element"])
        self.ui.nikke_element_box.setCurrentIndex(ele_index)

        burst_index = self.ui.nikke_burst_box.findData(nikke["burst"])
        self.ui.nikke_burst_box.setCurrentIndex(burst_index)

        manuf_index = self.ui.nikke_manuf_box.findData(nikke["manufacturer"])
        self.ui.nikke_manuf_box.setCurrentIndex(manuf_index)

        role_index = self.ui.nikke_role_box.findData(nikke["role"])
        self.ui.nikke_role_box.setCurrentIndex(role_index)

        self.current_image_path = nikke["image_path"]

        self.set_img_preview(nikke["image_path"])  
    
    def set_img_preview(self, img_path):
        if img_path:
            pixmap = get_pixmap(img_path)
            scaled = pixmap.scaled(
                40, 40,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )

            self.ui.nikke_img_preview.clear()
            self.ui.nikke_img_preview.setPixmap(scaled)
        else:
            self.ui.nikke_img_preview.clear()
            
    def load_nikke_cbox(self):
        nikke_list = api.fetch_nikkes()
        nikke_list.sort(key=lambda nikke: nikke["name"].lower())

        self.ui.select_nikke_cbox.clear()
        for nikke in nikke_list:
            self.ui.select_nikke_cbox.addItem(
                nikke["name"].title(),
                {
                    "id": nikke["id"],
                    "image_path": nikke["image_path"]
                }
            )

        self.ui.select_nikke_cbox.setCurrentIndex(-1)
        self.ui.select_nikke_cbox.view().setMinimumWidth(150)
    
    def load_bursts(self):
        self.bursts_list = [1, 2, 3]
        for value in self.bursts_list:
            self.ui.nikke_burst_box.addItem(
                f"{value}", value
            )
    
    def load_manuf(self):
        self.manuf_list = [
            ("Elysion", "elysion"),
            ("Tetra", "tetra"),
            ("Missilis", "missilis"),
            ("Pilgrim", "pilgrim"),
            ("Abnormal", "abnormal")
        ]

        for text, data in self.manuf_list:
            self.ui.nikke_manuf_box.addItem(f"{text}", data)
    
    def load_role(self):
        self.role_list = [('Attacker', 'attacker'), ('Defender', 'defender'), ('Supporter', 'supporter')]
        for text, data in self.role_list:
            self.ui.nikke_role_box.addItem(text, data)
    
    def load_element(self):
        self.element_list = [('Fire','fire'), ('Wind', 'wind'), ('Water', 'water'), ('Iron','iron'), ('Electric', 'electric')]

        self.element_list.sort(key=lambda x: x[0].lower())
        
        for text, data in self.element_list:
            self.ui.nikke_element_box.addItem(text, data)

    def get_nikke_image(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Image Files (*.png *.jpg *.jpeg *.webp *.bmp)"
        )

        if not file_path:
            return

        filename = os.path.basename(file_path)

        self.selected_local_image = file_path

        self.ui.nikke_select_image_button.setText(filename)

        self.set_img_preview(file_path)
        
    def on_accept(self):
        if self.mode == "edit":
            self.update_nikke()
        
        else:
            self.add_nikke()
    
    def update_nikke(self):
        nikke = self.ui.select_nikke_cbox.currentData()

        if not nikke:
            return
        
        nikke_data = self.validate_nikke_inputs()

        if self.selected_local_image:
            image = api.upload_nikke_image(self.selected_local_image)
            nikke_data["image_path"] = image["image_path"]

        else:
            nikke_data["image_path"] = self.current_image_path

        if nikke_data is None:
            return
            
        try:
            api.update_nikke(nikke["id"], nikke_data)

            QMessageBox.information(
                self,
                "Success",
                "Nikke updated successfully."
            )

        except requests.HTTPError as e:
            try:
                detail = e.response.json()["detail"]

            except Exception:
                detail = str(e)

            QMessageBox.critical(
                self,
                "Error",
                api.handle_api_error(detail)
            )

    def validate_nikke_inputs(self, require_selected=False):

        if require_selected:
            current_nikke = self.ui.select_nikke_cbox.currentData()

            if not current_nikke:
                QMessageBox.warning(
                self,
                "No Nikke selected.",
                "Please select a Nikke."
                )
                return None
        


        name = self.ui.nikke_name_line_edit.text().strip()
        if not name:
            QMessageBox.warning(
                self,
                "Missing Name",
                "Please enter a valid Nikke name."
            )
            return None

        element = self.ui.nikke_element_box.currentData()
        if not element:
            QMessageBox.warning(
            self,
            "Missing Element",
            "Please select a valid element."
            )
            return None

        burst = self.ui.nikke_burst_box.currentData()
        if not burst:
            QMessageBox.warning(
            self,
            "Missing Burst",
            "Please select a valid burst."
            )
            return None
        
        manuf = self.ui.nikke_manuf_box.currentData()
        if not manuf:
            QMessageBox.warning(
            self,
            "Missing manufacturer",
            "Please select a valid manufacturer."
            )
            return None

        role = self.ui.nikke_role_box.currentData()
        if not role:
            QMessageBox.warning(
            self,
            "Missing role",
            "Please select a valid role."
            )
            return None

        return {
            "name": name,
            "element": element,
            "burst": burst,
            "manufacturer": manuf,
            "role": role,
        }
    
    def delete_nikke(self):
        nikke = self.ui.select_nikke_cbox.currentData()
        nikke_name = self.ui.select_nikke_cbox.currentText()
        
        if not nikke:
            QMessageBox.warning(
                self,
                "Error",
                "Nikke not selected."
            )
            return
            
        confirm = QMessageBox.question(
            self,
            "Delete Nikke",
            f"Are you sure you want to delete {nikke_name}?"
        )

        if confirm != QMessageBox.StandardButton.Yes:
            return            

        api.delete_nikke(nikke["id"])

        QMessageBox.information(
            self,
            "Success", 
            "Nikke has been deleted."
        )

        self.accept()
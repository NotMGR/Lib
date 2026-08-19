import os, requests, resources

from PySide6.QtWidgets import QMessageBox, QDialog, QComboBox, QWidget, QCompleter
from PySide6.QtCore import Qt, QRegularExpression, Signal, QObject, QEvent
from PySide6.QtGui import QRegularExpressionValidator

from api import fetch_raids, fetch_users, fetch_raid_boss_info, fetch_nikkes, delete_mock, fetch_mock, update_mock_info, handle_api_error, create_mock, toggle_1_user_mock
from GUI.ui_helpers import make_combo_searchable
from GUI.UI_Files.mock_attempt_frame import Ui_Form

from logic.raid import get_raid_id
from logic.image_loader import get_pixmap

from GUI.add_mock_dmg_dialog import Ui_damage_done_form
from GUI.edit_mock_damage import Ui_edit_mock_form

def setup_searchable_combos(ui):       
    for child in ui.findChildren(QComboBox):
        make_combo_searchable(child)

        line_edit = child.lineEdit()

        line_edit.combo_ref = child

        tab_filter = ComboTabFilter(child)

        child.lineEdit().installEventFilter(tab_filter)

        child._tab_filter = tab_filter

        child.lineEdit().setAlignment(
        Qt.AlignmentFlag.AlignRight
        )

        ### ******* COMPLETER SETUP ********* ###   
        completer = QCompleter(
            child.model(),
            child
        )

        completer.popup().combo_ref = child
        completer.popup().installEventFilter(tab_filter)
        completer.setCaseSensitivity(
            Qt.CaseSensitivity.CaseInsensitive
        )
        completer.activated.connect(
            lambda text, combo=child:
                combo.setCurrentIndex(
                    combo.findText(text)
        )
)
        completer.setFilterMode(
            Qt.MatchFlag.MatchContains
        )
        completer.setCompletionMode(
            QCompleter.CompletionMode.PopupCompletion
        )


        child.lineEdit().setCompleter(completer)
        
class ComboTabFilter(QObject):

    def eventFilter(self, obj, event):

        if (
            event.type() == QEvent.Type.KeyPress
            and event.key() == Qt.Key.Key_Tab
        ):

            combo = obj.combo_ref

            completer = combo.lineEdit().completer()

            if completer and completer.popup().isVisible():

                popup = completer.popup()
                text = None
                current_index = popup.currentIndex()

                if current_index.isValid():
                    text = current_index.data()
                
                if not text:
                    first_index = popup.model().index(0,0)
                    text = first_index.data()
                
                if text:
                    index = combo.findText(text)

                    if index >= 0:
                        combo.setCurrentIndex(index)
                        combo.activated.emit(index)
            

        return False
    
def load_raids(sel_cbox, union_id):
    """Load raids into a searchable combo box."""
    raids = fetch_raids(union_id)

    if raids is None:
        return

    sel_cbox.blockSignals(True)

    try:
        sel_cbox.clear()
        
        for raid in raids:
            sel_cbox.addItem(
                raid["name"],
                raid["id"]
            )

        sel_cbox.setCurrentIndex(-1)

    finally:
        sel_cbox.blockSignals(False)   

class Mock_Dialog(QDialog):
    mock_added = Signal()
    """Creates a dialog to add mock damage"""
    def __init__(self, union_id):
        super().__init__()
        self.ui = Ui_damage_done_form()
        self.ui.setupUi(self)

        self.union_id = union_id

        if self.union_id is None:
            QMessageBox.warning(
                self,
                "Union Missing",
                "Please select a union before creating a mock."
            )
            self.reject()
            return

        self.nikke_list = load_nikkes()
        self.user_list = self.fetch_users()
        if self.user_list is None:
            QMessageBox.warning(
                self,
                "Error",
                "Could not load users for this union."
            )
            self.reject()
            return

        setup_searchable_combos(self)
        load_raids(self.ui.select_raid_cbox, self.union_id)

        self.ui.select_raid_cbox.currentIndexChanged.connect(self.load_bosses)
        self.ui.buttonBox.accepted.connect(self.add_mock_damage)
        self.ui.buttonBox.rejected.connect(self.reject)

        # self.fetch_users()
        self.load_user_cbox(self.user_list)
        load_nikke_cboxes(self.ui, self.nikke_list)
        connect_nikke_combo_signals(self.ui, 25)
        self.load_bosses()

        for i in range (1, 26):
            load_nikke_images(self.ui, i)

        validator = QRegularExpressionValidator(QRegularExpression(r"\d{0,12}"))

        for i in range (1, 6):
            line = getattr(self.ui, f"boss_dmg_{i}")
            line.setValidator(validator)

    def add_mock_damage(self):
        """Adds all the information in the mock damage dialog. Nikke used, boss targeted, """

        try:
            raid_id = self.ui.select_raid_cbox.currentData()
            
            user_id = self.ui.select_user_cbox.currentData()

            if not raid_id:
                QMessageBox.warning(self, "Error", "Please select a raid first.") #Checks if theres a raid selected
                return
            
            if not user_id:
                QMessageBox.warning(self, "Error", "Please select a user first")
                return

            mock_data = []
            for group_num in range(5):  # Groups through nikke cbox in groups of 5
                start = group_num * 5 + 1
                end = start + 5

                dmg_label = getattr(self.ui, f"boss_dmg_{group_num + 1}", None) #Gets each dmg done line edit
                boss_name_label = getattr(self.ui, f"boss_name_{group_num + 1}", None)

                if not (dmg_label and boss_name_label):
                    continue
                
                dmg_done = dmg_label.text().strip()
                boss_id = boss_name_label.boss_id

                #Collect the nikkes

                group_selection = []
                
            
                #Loop to get each nikke team
                for i in range(start, end): 
                    combo = getattr(self.ui, f"nikke_cbox_{i}", None) #Get each nikke's cbox
                    if combo:
                        nikke = combo.currentData()
                        if nikke is not None:

                            group_selection.append(nikke["id"])              
                                
                if not (dmg_done and boss_id):
                    continue
                
                new_mock = {
                    "damage_number": dmg_done,
                    "player_id": user_id,
                    "boss_id": boss_id,
                    "team_members": group_selection if group_selection else None,
                }
                mock_data.append(new_mock)    

            create_mock(mock_data)
            self.mock_added.emit()

            QMessageBox.information(
                self,
                "Success.",
                f"Mocks added successfully.",
            )

        except requests.HTTPError as e:
            QMessageBox.warning(
                self,
                "Something went wrong.",
                handle_api_error(e)
    )              

    def load_user_cbox(self, users):
        for user in users:
            if user["is_active"]:
                self.ui.select_user_cbox.addItem(user["username"], user["id"])

        self.ui.select_user_cbox.setCurrentIndex(-1)

    def fetch_users(self):
        return fetch_users(self.union_id)
    
    def load_bosses(self):
        """Loads the boss names into their labels."""
        raid_id = self.ui.select_raid_cbox.currentData()

        for i in range(1, 6):  # assuming 5 bosses max
            name_label = getattr(self.ui, f"boss_name_{i}", None)
            weakness_label = getattr(self.ui, f"boss_weak_label_img_{i}", None)

            if name_label:
                name_label.clear()
            if weakness_label:
                weakness_label.clear()
        
        if raid_id is None:
            return
        
        boss_list = fetch_raid_boss_info(raid_id)
        
        if not boss_list:
            return                    
        
        for i, boss in enumerate(boss_list, start=1): 

            label_widget = getattr(self.ui, f"boss_name_{i}", None)
            weakness_widget = getattr(self.ui, f"boss_weak_label_img_{i}", None)

            if label_widget:
                label_widget.setText(boss["name"])
                label_widget.boss_id = boss["id"]
        

            if weakness_widget:
                image_path = resources.ELEMENT_IMAGES.get(boss["weakness"].lower())
                
                pixmap = get_pixmap(image_path)
                scaled = pixmap.scaled(
                    30, 30,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
                weakness_widget.setPixmap(scaled)
                weakness_widget.setScaledContents(False)
            else:
                weakness_widget.clear()                        
                
def connect_nikke_combo_signals(ui, combo_number):

    for i in range(1, combo_number + 1):  # adjust to your number of combos
        combo = getattr(ui, f"nikke_cbox_{i}", None)

        if combo:

            combo.currentIndexChanged.connect(
                lambda _, idx=i:
                handle_nikke_combo_change(
                    ui, idx
                )
            )

def handle_nikke_combo_change(ui, idx):
    combo = getattr(
        ui, 
        f"nikke_cbox_{idx}",
        None
    )
    if not combo:
        return
    
    combo.lineEdit().setCursorPosition(0)
    load_nikke_images(
        ui,
        idx
    )

def load_nikke_images(ui, idx): #Loads each nikke img respective to the cbox selection from 1 to idx   
        
    nikke_img_label = getattr(
        ui,
        f"nikke_img_label_{idx}",
        None
    )

    nikke_cbox = getattr(
        ui,
        f"nikke_cbox_{idx}",
        None
    )

    if not nikke_cbox or not nikke_img_label:
        return
    
    selected_nikke = (
        nikke_cbox.currentData()
    )

    if not selected_nikke:
        nikke_img_label.clear()
        return
    
    nikke_img_path = (
            selected_nikke["image_path"]
        )


    if nikke_img_path:
        pixmap = get_pixmap(nikke_img_path)

        scaled = pixmap.scaled(
            90,
            90,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        nikke_img_label.setPixmap(scaled)

        nikke_img_label.setScaledContents(False)
    
    else:
        nikke_img_label.clear()

def load_nikkes():
    """Loads and store the list of all nikkes"""
    nikke_query = fetch_nikkes()
    return nikke_query
      
def load_nikke_cboxes(ui, items, count=25): #Count is the number of cboxes
    """Puts the nikke list into their combo boxes"""
    items.sort(key=lambda nikke: nikke["name"].lower())

    for i in range(1, count+1):
        cbox = getattr(ui, f"nikke_cbox_{i}", None)
        if cbox:
            cbox.clear()
            for nikke in items:
                cbox.addItem(nikke["name"].title(), {
                    "id": nikke["id"],
                    "image_path": nikke["image_path"]
                })          

            cbox.setCurrentIndex(-1) #Empty at start
            cbox.view().setMinimumWidth(150) #Makes dropdown bigger

def load_bosses_and_weaknesses(raid_object, ui): #Loads both attempts and ranking pages boss names and weaknesses -- Main Buttons 1 - 5 too
        raid_id = get_raid_id(raid_object)
    
        for i in range(1, 6):  # assuming 5 bosses max
            name_label = getattr(ui, f"boss_name_label_att_{i}", None)
            weakness_label = getattr(ui, f"boss_weak_label_attempt_{i}", None)
            boss_rank_name = getattr(ui, f"boss_name_rank_label_{i}", None)
            boss_rank_label = getattr(ui, f"boss_weak_rank_label_{i}", None)
            main_button_name = getattr(ui, f"boss_push_button_{i}", None)

            if name_label:
                name_label.clear()

            if weakness_label:
                weakness_label.clear()
            
            if boss_rank_name:
                boss_rank_name.clear()
            
            if boss_rank_label:
                boss_rank_label.clear()
            
        if not raid_id:
            return
        
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__)) 
            image_folder = os.path.join(base_dir, "..", "images", "codes")  
            image_folder = os.path.normpath(image_folder)  

            bosses = fetch_raid_boss_info(raid_id)

            for i, boss in enumerate(bosses, start=1):
                boss_name = boss["name"]
                boss_weakness = boss["weakness"]


                label_name = f"boss_name_label_att_{i}"
                weakness_label = f"boss_weak_label_attempt_{i}"
                boss_rank_name = f"boss_name_rank_label_{i}"
                boss_rank_label = f"boss_weak_rank_label_{i}"
                main_button_name = f"boss_push_button_{i}"

                label_widget = getattr(ui, label_name, None)
                weakness_widget = getattr(ui, weakness_label, None)
                rank_name_widget = getattr(ui, boss_rank_name, None)
                rank_weak_widget = getattr(ui, boss_rank_label, None)
                main_button_widget = getattr(ui, main_button_name, None)


                if label_widget:
                    label_widget.setText(boss_name.title())
                    label_widget.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)

                if rank_name_widget:
                    rank_name_widget.setText(boss_name.title())
                    rank_name_widget.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)

                if main_button_widget:
                    main_button_widget.setText(boss_name.title())

                if weakness_widget:
                    image_path = resources.ELEMENT_IMAGES.get(
                        boss_weakness.lower()
                    )
                    pixmap = get_pixmap(image_path)
                    scaled = pixmap.scaled(
                        32, 32,
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )
                    weakness_widget.setPixmap(scaled)
                    weakness_widget.setScaledContents(True)

                    rank_weak_widget.setPixmap(scaled)
                    rank_weak_widget.setScaledContents(True)

                else:
                    weakness_widget.clear()
                    weakness_widget.setText("error")

                    rank_weak_widget.clear()
                    rank_weak_widget.setText("error")

class MockFrameModel(QWidget):
    mock_toggled = Signal(int, bool, int)
    edit_toggled = Signal(int)

    def __init__(self, username: str, damage: int, image_paths: list[str], mock_id: int, is_active: bool, boss_id, parent=None):
        super().__init__(parent)

        #Loads the UI file for the mock damage frame widget
        self.ui = Ui_Form() 
        self.ui.setupUi(self)

        #button state
        self.ui.remove_mock_button_1.setCheckable(True)
        self.ui.remove_mock_button_1.toggled.connect(self.on_toggle)
        self.ui.edit_tool_button.clicked.connect(self.on_edit_click)
        
        #self variables
        self.username = username
        self.damage = damage
        self.image_paths = image_paths
        self.id = mock_id
        self.is_active = is_active
        self.boss_id = boss_id
               

        self.update_overlay_geometry()

        #Final setup
        self.setup_ui()
        self.apply_initial_state()
    
    def setup_ui(self):

        #username and damage
        self.ui.username_label_1.setText(str(self.username))
        self.ui.user_damage_label_1.setText(
            f"{self.damage:,}".replace(",", ".")
        )  
        DEFAULT_IMAGE = "nikke/noimg.png"


        #Alignment
        self.ui.user_damage_label_1.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.ui.username_label_1.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)

        for index in range(1, 6):
            label = getattr(self.ui, f"nikke_mock_img_label_{index}", None)

            if not label:
                continue

            if index <= len(self.image_paths):
                img_path = self.image_paths[index -1]
            
            else:
                img_path = DEFAULT_IMAGE
            
            pixmap = get_pixmap(img_path)

            if not pixmap.isNull():
                scaled = pixmap.scaled(
                    90,
                    90,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
                label.setPixmap(scaled)
                label.setScaledContents(False)
        
    def alter_mock(self, enabled: bool): 
        """Builds a visual layer with reduced opacity above each frame, as if it's disabling it."""
        if enabled:
            if not hasattr(self, "_overlay"):

                self._overlay = QWidget(self.ui.mock_frame_1)
                self._overlay.setStyleSheet("background-color: rgba(0, 0, 0, 180);")
                self._overlay.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
                self._overlay.show()
            
            self._overlay.setGeometry(self.ui.mock_frame_1.rect())
            self._overlay.show()

            
        else:
            if hasattr(self, "_overlay"):
                self._overlay.hide()
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_overlay_geometry()

    def update_overlay_geometry(self):
        if hasattr(self, "_overlay"):
            self._overlay.setGeometry(self.ui.mock_frame_1.rect())
    
    def db_mock_update(self, enabled: bool):
        
        new_state = not enabled

        toggle_1_user_mock(self.id, new_state)
    
    def on_toggle(self, enabled: bool):
        self.alter_mock(enabled)
        self.db_mock_update(enabled)
        self.mock_toggled.emit(self.id, enabled, self.boss_id)

    def apply_initial_state(self):
        is_disabled = not self.is_active

        self.ui.remove_mock_button_1.setChecked(is_disabled)

        self.alter_mock(is_disabled)

    def on_edit_click(self):
        self.edit_toggled.emit(self.id)

class Edit_Mock(QDialog):
    mock_updated = Signal()
    mock_deleted = Signal()

    def __init__(self, mock_id):
        super().__init__()
        self.ui = Ui_edit_mock_form()
        self.ui.setupUi(self)
        self.mock_id = mock_id
        self.nikke_list = load_nikkes()        

        load_nikke_cboxes(self.ui, self.nikke_list, count=5)
        connect_nikke_combo_signals(self.ui, 5)   

        self.load_mock_info()

        self.ui.buttonBox.accepted.connect(self.update_mock)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.delete_mock_button.clicked.connect(self.delete_mock)
    
    def load_mock_info(self):
        mock = fetch_mock(self.mock_id)

        self.load_team_cbox(mock["team"])
        self.load_boss_weak_img(mock["boss"]["weakness"])

        self.ui.boss_name_2.setText(mock["boss"]["name"])
        self.ui.boss_dmg_1.setText(str(mock["damage_number"]))
        self.ui.edit_name_label.setText(mock["player"]["username"])

    def load_team_cbox(self, team):
        """Loads the teams into the cboxes"""
        if not team:
            return
        formation_order = team["team_order"]

        nikke_ids = [
            int(x)
            for x in formation_order.split(",")
        ] 

        for i, nikke_id in enumerate(nikke_ids, start=1):
            combo = getattr(self.ui, f"nikke_cbox_{i}", None)

            if combo:
                set_combo_by_nikke_id(combo, nikke_id)

    def load_boss_weak_img(self, weakness):
            image_path = resources.ELEMENT_IMAGES.get(weakness.lower())

            if image_path: #Loads the weakness icons
                pixmap = get_pixmap(image_path)
                scaled = pixmap.scaled(
                    32, 32,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
                self.ui.boss_weak_label_img_1.setPixmap(scaled)
                self.ui.boss_weak_label_img_1.setScaledContents(True)
    
    def update_mock(self): 
        """Update the mock data in the db"""
        try:
            group_selection = []
                    
            for i in range(1, 6): 
                combo = getattr(self.ui, f"nikke_cbox_{i}", None) #Get each nikke's cbox
                if combo:
                    selected = combo.currentData()

                    if selected is not None:
                        group_selection.append(selected["id"])

            damage = int(self.ui.boss_dmg_1.text().strip())
            
            mock_data = {
                "damage_number": damage,
                "team_members": group_selection if group_selection else None,
            }

            print(mock_data)
            update_mock_info(self.mock_id, mock_data)

            QMessageBox.information(
                self,
                "Success.",
                f"Mock Changed",
            )
            
            self.accept()
            self.mock_updated.emit()
        

        except requests.HTTPError as e:
            print(e.response.json())
            QMessageBox.warning(
                self,
                "Something went wrong.",
                handle_api_error(e)
        )

        except Exception:
            QMessageBox.warning(
                self,
                "Error",
                "Not able to update mock. Check all fields and try again."
            )

    def delete_mock(self):
        mock= self.mock_id
        
        if not mock:
            QMessageBox.warning(
                self,
                "Error",
                "Not able to select mock."
            )
            return
            
        confirm = QMessageBox.question(
            self,
            "Delete Mock",
            "Are you sure you want to delete this mock?"
        )

        if confirm != QMessageBox.StandardButton.Yes:
            return
        
        if mock:
            delete_mock(mock)

        QMessageBox.information(
            self,
            "Success", 
            "Mock has been deleted."
        )

        self.accept()
        self.mock_deleted.emit()

def set_combo_by_nikke_id(combo, nikke_id):
    for index in range(combo.count()):
        data = combo.itemData(index)

        if data and data["id"] == nikke_id:
            combo.setCurrentIndex(index)
            return True

    return False
from PySide6.QtWidgets import QMainWindow, QMessageBox,QVBoxLayout, QButtonGroup

import api, requests
from GUI.main_window_redesign import Ui_MainWindow
from logic import nikkes, raid, users, mock_damage, attempts, rankings, server

import GUI.ui_helpers

from logic.raid import get_raid_id


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        self.hide_future_functions()
        self._updating = False

        GUI.ui_helpers.setup_all_tables(self)

        mock_damage.load_raids(self.ui.select_raid_cbox_main)

        self.ui.select_raid_cbox_main.currentIndexChanged.connect(
            self.on_raid_changed
        )

        self.setWindowTitle("Lib")

        #Boss buttons configuration
        self.boss_button_group = QButtonGroup(self)
        self.boss_button_group.setExclusive(True)
        boss_buttons = [
            self.ui.boss_push_button_1,
            self.ui.boss_push_button_2,
            self.ui.boss_push_button_3,
            self.ui.boss_push_button_4,
            self.ui.boss_push_button_5,
        ]

        for button in boss_buttons:
            button.setCheckable(True)
            self.boss_button_group.addButton(button)
        
        self.ui.boss_push_button_1.setChecked(True)

        # Navigation buttons configuration
        self.navigation_button_group = QButtonGroup(self)
        self.navigation_button_group.setExclusive(True)
        navigation_buttons = [
            self.ui.mock_home_button,
            self.ui.Attempt_tracker_button,
            self.ui.ranking_button,
        ]
        
        for button in navigation_buttons:
            button.setCheckable(True)
            self.navigation_button_group.addButton(button)

        self.ui.mock_home_button.setChecked(True)

        ## Other UI elements
        self.mock_avg_labels = [
            self.ui.average_mock_number_1,
            self.ui.average_mock_number_2,
            self.ui.average_mock_number_3,
            self.ui.average_mock_number_4,
            self.ui.average_mock_number_5,
        ]

        ## Menu linkage to dialogs
        self.ui.actionAdd_Nikke.triggered.connect(self.open_nikke_dialog)
        self.ui.actionEdit_Nikke.triggered.connect(lambda: self.open_nikke_dialog(mode="edit"))
        self.ui.actionAdd_Raid_2.triggered.connect(self.open_raid_dialog)
        self.ui.actionEdit_Raid.triggered.connect(lambda: self.open_raid_dialog(mode="edit"))
        self.ui.actionAdd_Member.triggered.connect(self.open_user_dialog)
        self.ui.actionServer.triggered.connect(self.open_server_dialog)
        
        self.ui.actionAdd_Mock_Damage.triggered.connect(self.open_mock_dialog)
        self.ui.actionEdit_Member.triggered.connect(self.open_edit_user_dialog)

        #Reloads data
        self.ui.show_inactive_table_checkbox.toggled.connect(self.load_ranking_page)
        self.ui.show_inactive_mock_checkbox.toggled.connect(self.load_main_mocks)
        
        #Changes main page
        self.ui.mock_home_button.clicked.connect(lambda: self.ui.main_stacked_widget.setCurrentIndex(0))
        self.ui.Attempt_tracker_button.clicked.connect(lambda: self.ui.main_stacked_widget.setCurrentIndex(1))
        self.ui.ranking_button.clicked.connect(lambda: self.ui.main_stacked_widget.setCurrentIndex(2))

        #Changes boss shown on mocks
        self.ui.boss_push_button_1.clicked.connect(lambda: self.ui.mock_stacked_widget_1.setCurrentIndex(0))
        self.ui.boss_push_button_2.clicked.connect(lambda: self.ui.mock_stacked_widget_1.setCurrentIndex(1))
        self.ui.boss_push_button_3.clicked.connect(lambda: self.ui.mock_stacked_widget_1.setCurrentIndex(2))
        self.ui.boss_push_button_4.clicked.connect(lambda: self.ui.mock_stacked_widget_1.setCurrentIndex(3))
        self.ui.boss_push_button_5.clicked.connect(lambda: self.ui.mock_stacked_widget_1.setCurrentIndex(4))

    # ========== Dialog linkage =============
    def open_nikke_dialog(self, mode):
        dialog = nikkes.Nikke_Dialog(mode=mode)
        dialog.exec()
          
    def open_raid_dialog(self, mode):
        dialog = raid.Raid_Dialog(mode=mode)

        dialog.raid_created.connect(
           lambda: mock_damage.load_raids(self.ui.select_raid_cbox_main)
        )
        if self.ui.select_raid_cbox_main.currentIndex() != -1:
            dialog.raid_updated.connect(
                self.on_raid_changed
            )
        
        dialog.raid_deleted.connect(
            self.on_raid_deleted
        )

        dialog.raid_updated.connect(
            lambda: mock_damage.load_raids(self.ui.select_raid_cbox_main)
        )
        dialog.exec()    
    
    def open_user_dialog(self):
        dialog = users.User_dialog()
        dialog.exec()

    def open_mock_dialog(self):
        dialog = mock_damage.Mock_Dialog()

        dialog.mock_added.connect(
            self.on_raid_changed
        )

        dialog.exec()
    
    def open_edit_user_dialog(self):
        dialog = users.Edit_User_Dialog()
        dialog.exec()
    
    def open_edit_mock_dialog(self, mock_id):
        dialog = mock_damage.Edit_Mock(mock_id)
        dialog.mock_updated.connect(self.load_main_mocks)
        dialog.mock_deleted.connect(self.on_raid_changed)
        dialog.exec()

    def open_server_dialog(self):
        dialog = server.Server_Dialog()
        dialog.exec()

    #=========== Main Logic =============
    def load_main_mocks(self): #Creates each instance of the frame models
            
            raid_id = self.ui.select_raid_cbox_main.currentData()

            mock_info = api.fetch_mock_info(raid_id)
            boss_list = api.fetch_raid_boss_info(raid_id)

            sorted_mock_info = {}
            for mock in mock_info:
                if mock["boss_id"] in sorted_mock_info:
                    sorted_mock_info[mock["boss_id"]].append(mock)
                
                else:
                    sorted_mock_info.setdefault(mock["boss_id"], []).append(mock)          

            for index, boss in enumerate(boss_list, start=1):

                boss_mock_info = sorted_mock_info.get(boss["id"], [])

                boss_scroll_area = getattr(self.ui, f"mock_scroll_area_content_{index}")

                content_layout = boss_scroll_area.layout()

                if content_layout is None:
                    content_layout = QVBoxLayout(boss_scroll_area)

                self.clear_layout(content_layout)

                show_inactive = self.ui.show_inactive_mock_checkbox.isChecked()

                for item in boss_mock_info:

                    if not show_inactive and not item["is_active"]:
                        continue

                    images = [
                        img if img else "noimg.png"
                        for img in item["images"]
                    ]
                    mock_frame = mock_damage.MockFrameModel(
                        item["username"],
                        item["damage_number"],
                        images,
                        item["mock_id"],
                        item["is_active"],
                        boss_id=boss["id"]
                    )
                    
                    content_layout.addWidget(mock_frame)

                    #Signals
                    mock_frame.mock_toggled.connect(self.handle_mock_toggle) 
                    mock_frame.edit_toggled.connect(self.open_edit_mock_dialog)

    def handle_mock_toggle(self, mock_id, enabled, boss_id): #Receives ID and the enabled variable. The ranking table update function should be called here. boss id used for ranking table update
        self.load_ranking_page()                        

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

    def load_attempt_frames(self):
        try:
            raid_id = self.ui.select_raid_cbox_main.currentData()

            if not raid_id:               
                return            
            
            attempts_rows = api.fetch_attempts(raid_id)

            content_area = self.ui.scrollAreaWidgetContents_2.layout() #scroll_area is the content widget for the attempt scroll area widget
            self.clear_layout(content_area)

            for attempt in attempts_rows:
                frame = attempts.AttemptFrameWidget(
                    id = attempt["id"],
                    user_id=attempt["user_id"],
                    raid_id=attempt["raid_id"],
                    username=attempt["username"],
                    attempts=attempt["attempts"],
                    att_left=attempt["attempts_remaining"]
                )
                frame.attempt_changed.connect(
                    self.on_attempt_changed
                )

                frame.toggle_mocks.connect(
                    self.toggle_user_mocks
                )

                content_area.addWidget(frame)

        except requests.HTTPError as e:
            try:
                detail = e.response.json()["detail"]

            except Exception:
                detail = str(e)

            QMessageBox.critical(
                self,
                "Error.",
                f"Something went wrong loading the attempt frames.", 
            )
            print(detail)        
    
    def on_attempt_changed(self, attempt_id, active_buttons):
        try:
            api.update_attempt(attempt_id, active_buttons)

        except requests.HTTPError as e:
            print(e)

    def toggle_user_mocks(self, raid_id, uid):
        try:
            api.toggle_user_mocks(uid, raid_id)
            self.load_main_mocks()
            self.load_ranking_page()

        except requests.HTTPError as e:
            QMessageBox.warning(
                self,
                "Error",
                "No Mocks Found."
            )
            return

    def load_ranking_page(self):
        self.models = {}

        raid_id = get_raid_id(self.ui.select_raid_cbox_main)
        show_inactive = self.ui.show_inactive_table_checkbox.isChecked()

        mock_ranking = api.fetch_ranking(raid_id, show_inactive)
        boss_list = api.fetch_raid_boss_info(raid_id)

        for table, label, boss in zip(self.get_boss_tables(), self.mock_avg_labels, boss_list):
            boss_id = boss["id"]

            boss_data = mock_ranking.get(str(boss_id), {
                "average": None, 
                "rankings": []
            })    

            model = rankings.MockDamageModel(boss_data["rankings"], boss_id)
            table.setModel(model)

            #avg
            average = boss_data["average"]
            self.set_mock_avg(label, average)

            #Color gradient based on rankings
            config = GUI.ui_helpers.TableConfigurator(table)
            config.apply_default()
            config.apply_rank_gradient(max_rank=max(len(boss_data["rankings"]), 1))
            
            table.setSortingEnabled(True)

            self.models[boss_id] = model

    def set_mock_avg(self, avg_label, average):        
        avg_label.clear()            
        if average is not None:
            formatted_dmg = f"{int(average):,}".replace(",", ".")
            avg_label.setText(formatted_dmg)
        
        else:
            avg_label.setText("N/A")
        
        return

    def get_boss_tables(self):
        return [
            self.ui.boss_rank_table_1,
            self.ui.boss_rank_table_2,
            self.ui.boss_rank_table_3,
            self.ui.boss_rank_table_4,
            self.ui.boss_rank_table_5,
        ]

    def update_data(self):
        raid_id = self.ui.select_raid_cbox_main.currentData()

        if raid_id is None:
            return
        
        self.safe_call(self.load_main_mocks)
        self.safe_call(self.load_attempt_frames)
        self.safe_call(self.load_ranking_page)
        self.ui.mock_stacked_widget_1.setCurrentIndex(0)
    
    def update_ui(self):
        self.safe_call(self.load_ranking_page)
        mock_damage.load_bosses_and_weaknesses(
            self.ui.select_raid_cbox_main,
            self.ui
        )

    def safe_call(self, func):
        try:
            func()
        except Exception as e:
            print(f"Error in {func.__name__}:", e)

    def on_raid_changed(self):
        if self._updating:
            return
        
        self._updating = True

        try:
            self.update_data()
            self.update_ui()
        
        finally:
            self._updating = False
    
    def on_raid_deleted(self):
        mock_damage.load_raids(self.ui.select_raid_cbox_main)
        self.ui.select_raid_cbox_main.setCurrentIndex(-1)

    def hide_future_functions(self):
        
        #=========== SORTING BUTTONS ==============#
        self.ui.sort_by_label.hide()
        self.ui.sort_by_label_attempt.hide()
        self.ui.damage_sort_mock_button.hide()
        self.ui.attempt_sort_button_2.hide()
        self.ui.member_sort_attempt_button_2.hide()
        self.ui.member_sort_mock_button.hide()

        #============ MENUS ===========#
        self.ui.actionEdit_Mocks.setVisible(False)
        self.ui.actionAdd_Damage.setVisible(False)

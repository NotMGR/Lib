
from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtCore import Signal, Qt

from GUI.UI_Files.attempt_frame import Ui_Form

class AttemptFrameWidget(QWidget):
    attempt_changed = Signal(int, list)
    toggle_mocks = Signal(int, int)

    def __init__(self, id, user_id, raid_id, username, attempts, att_left, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )
        self.id = id
        self.user_id = user_id
        self.raid_id = raid_id

        self.ui.user_attempt_label_1.setText(username)

        self.ui.mock_toggle_button.clicked.connect(self.on_toggle_mock_press) 

        self.buttons = [
            self.ui.boss_attempt_pbutton_1,
            self.ui.boss_attempt_pbutton_2,
            self.ui.boss_attempt_pbutton_3,
            self.ui.boss_attempt_pbutton_4,
            self.ui.boss_attempt_pbutton_5,
        ]
        self.ui.attempt_left_label_1.setText(str(att_left))
        self.ui.attempt_left_label_1.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)

        for i, btn in enumerate(self.buttons, start=1):
            btn.clicked.connect(
                lambda _, idx=i: self.on_button_clicked(idx)
            )
        
        for button, state in zip(self.buttons, attempts):
            button.setChecked(state)
    
    def on_button_clicked(self, idx):
        active = self.get_active_buttons()

        if len(active) > 3:
            self.buttons[idx - 1].blockSignals(True)
            self.buttons[idx - 1].setChecked(False)
            self.buttons[idx - 1].blockSignals(False)
            return
        
        
        self.update_attempts_left_label()

        self.attempt_changed.emit(
            self.id,
            self.get_active_buttons()
        )
    
    def get_active_buttons(self):
        return[
            i + 1 for i, btn in enumerate(self.buttons)
            if btn.isChecked()
        ]
    
    def update_attempts_left_label(self):
        remaining = 3 - len(self.get_active_buttons())
        self.ui.attempt_left_label_1.setText(str(remaining))
        self.ui.attempt_left_label_1.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
    
    def on_toggle_mock_press(self):
        self.toggle_mocks.emit(self.user_id, self.raid_id)

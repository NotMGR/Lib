from PySide6.QtCore import Qt, QAbstractTableModel
from PySide6.QtGui import QColor, QBrush


class MockDamageModel(QAbstractTableModel):
    def __init__(self, data, boss_id, parent=None):
        super().__init__(parent)
        self.__data = data
        self.boss_id = boss_id
    
    def rowCount(self, parent=None):
        return len(self.__data)
    
    def columnCount(self, parent=None):
        return 3
    
    def data(self, index, role):
        if not index.isValid():
            return None
        
        row = index.row()
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0:
                return self.__data[row]["rank"]
            if col == 1:
                return self.__data[row]["username"]
            if col == 2:
                damage = self.__data[row]["damage"]
                return f"{damage:,}".replace(",", ".") ## THIS MAKES DAMAGE RETURN A STRING INSTEAD OF INT. Should be no problem as it is already sorted.
        
        if role == Qt.ItemDataRole.TextAlignmentRole:
            if col == 1:
                return Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
            if col == 2:
                return Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        
        if self.__data[row]["is_active"] == False:

            #Background
            if role == Qt.ItemDataRole.BackgroundRole:
                return QBrush(QColor(60, 60, 60))
            
            #Text Color
            if role == Qt.ItemDataRole.ForegroundRole:
                return QBrush(QColor(170, 170, 170))
            
        return None

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
              return ["Rank", "User", "Damage"][section]
    
    def update_row_by_id(self, id, enabled):
        for row_index, item in enumerate(self.__data):

            if item["id"] == id:

                item["is_active"] = bool (not enabled)

                #Notify qt that the row changed
                top_left = self.index(row_index, 0)
                bottom_right = self.index(row_index, self.columnCount() - 1)

                self.dataChanged.emit(top_left, bottom_right)
                
                return


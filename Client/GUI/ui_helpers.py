from PySide6.QtWidgets import QComboBox, QCompleter, QHeaderView, QTableView, QStyledItemDelegate
from PySide6.QtCore import Qt, QSortFilterProxyModel
from PySide6.QtGui import QLinearGradient, QColor

def make_combo_searchable(combo_box: QComboBox):
    """
    Turns a QComboBox into a searchable, filterable combo box with auto-complete.
    Compatible with PySide6.
    """
    combo_box.setFocusPolicy(Qt.StrongFocus)
    combo_box.setEditable(True)

    # create filter model
    filter_model = QSortFilterProxyModel(combo_box)
    filter_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
    filter_model.setSourceModel(combo_box.model())

    # create completer using filter model
    completer = QCompleter(filter_model, combo_box)
    completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
    combo_box.setCompleter(completer)

    # update filter on text edit
    combo_box.lineEdit().textEdited.connect(filter_model.setFilterFixedString)

    # select item when a completer option is activated
    def on_completer_activated(text):
        if text:
            index = combo_box.findText(text)
            combo_box.setCurrentIndex(index)
            combo_box.activated.emit(index)
    


    completer.activated.connect(on_completer_activated)

    # override setModel to keep filter & completer updated
    original_set_model = combo_box.setModel

    def new_set_model(model):
        original_set_model(model)
        filter_model.setSourceModel(model)
        completer.setModel(filter_model)

    combo_box.setModel = new_set_model

    # override setModelColumn to keep filter column synced
    original_set_model_column = combo_box.setModelColumn

    def new_set_model_column(column):
        filter_model.setFilterKeyColumn(column)
        completer.setCompletionColumn(column)
        original_set_model_column(column)

    combo_box.setModelColumn = new_set_model_column

def setup_all_tables(parent):
    for table in parent.findChildren(QTableView):
        TableConfigurator(table).apply_default()

class TableConfigurator:
    def __init__(self, table):
        self.table = table
        self.header = table.horizontalHeader()

    #Controller function
    def apply_default(self):
        self.stretch()
        self.hide_vertical_header()
        self.hide_column(0)
        self.hide_header()


    #Property functions

    def stretch(self):
        self.header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    
    def hide_vertical_header(self):
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(34)
    
    def hide_header(self):
        self.table.horizontalHeader().setVisible(False)
    
    def hide_column(self, col):
        self.table.setColumnHidden(col, True)
    
    def apply_rank_gradient(self, max_rank):
        delegate = RankGradientDelegate(max_rank, self.table)
        self.table.setItemDelegate(delegate)


class RankGradientDelegate(QStyledItemDelegate):
    def __init__(self, max_rank, parent=None):
        super().__init__(parent)
        self.max_rank = max_rank

    def paint(self, painter, option, index):
        rank = index.sibling(index.row(), 0).data()

        ratio = (rank - 4) / max(self.max_rank - 4, 1)

        start = QColor(36, 35, 51)
        end   = QColor(94, 49, 74)

        r = start.red() + (end.red() - start.red()) * ratio
        g = start.green() + (end.green() - start.green()) * ratio
        b = start.blue() + (end.blue() - start.blue()) * ratio

        color = QColor(int(r), int(g), int(b))

        painter.save()
        painter.fillRect(option.rect, color)
        painter.restore()

        option.palette.setColor(
        option.palette.ColorRole.Text,
        Qt.GlobalColor.white      # or Qt.GlobalColor.white
    )
        option.displayAlignment = Qt.AlignmentFlag.AlignCenter

        super().paint(painter, option, index)



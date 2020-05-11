from PySide2.QtGui import QPainter, QBrush, QPen
from PySide2.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QComboBox, QLabel, QHBoxLayout, \
    QVBoxLayout, QGridLayout
from PySide2.QtCore import Qt, QSize, Signal
import sys

from puissance4.color import Color

from puissance4.grid import Grid


class SettingsWindow(QMainWindow):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.setWindowTitle("Puissance 4 - Settings")

        self.nb_row = 6
        self.nb_column = 7
        self.align = 4
        self.player = Qt.red

        # columns
        column_label = QLabel("Number of columns: ")
        column_combo_box = QComboBox()
        row_values = ["4", "5", "6", "7", "8", "9"]
        column_combo_box.insertItems(0, row_values)
        column_combo_box.setCurrentIndex(row_values.index("7"))
        column_combo_box.currentTextChanged.connect(lambda: self.set_column(column_combo_box.currentText()))
        column_box = QHBoxLayout()
        column_box.addWidget(column_label)
        column_box.addStretch()
        column_box.addWidget(column_combo_box)

        # rows
        row_label = QLabel("Number of rows: ")
        row_combo_box = QComboBox()
        row_values = ["4", "5", "6", "7", "8", "9"]
        row_combo_box.insertItems(0, row_values)
        row_combo_box.setCurrentIndex(row_values.index("6"))
        row_combo_box.currentTextChanged.connect(lambda: self.set_row(row_combo_box.currentText()))
        row_box = QHBoxLayout()
        row_box.addWidget(row_label)
        row_box.addStretch()
        row_box.addWidget(row_combo_box)

        # rows
        align_label = QLabel("Number of pieces to align: ")
        align_combo_box = QComboBox()
        align_values = ["2", "3", "4", "5"]
        align_combo_box.insertItems(0, align_values)
        align_combo_box.setCurrentIndex(align_values.index("4"))
        align_combo_box.currentTextChanged.connect(lambda: self.set_align(align_combo_box.currentText()))
        align_box = QHBoxLayout()
        align_box.addWidget(align_label)
        align_box.addStretch()
        align_box.addWidget(align_combo_box)

        # player
        player_label = QLabel("Who starts?")
        player_combobox = QComboBox()
        player_values = ["Red", "Yellow"]
        player_combobox.insertItems(0, player_values)
        player_combobox.setCurrentIndex(0)
        player_combobox.currentTextChanged.connect(lambda: self.set_player(player_combobox.currentText()))
        player_box = QHBoxLayout()
        player_box.addWidget(player_label)
        player_box.addStretch()
        player_box.addWidget(player_combobox)

        start_button = QPushButton("Start game")
        start_button.clicked.connect(self.start)

        quit_button = QPushButton("Quit game")
        quit_button.clicked.connect(self.quit)

        buttons_box = QHBoxLayout()
        buttons_box.addWidget(start_button)
        buttons_box.addStretch()
        buttons_box.addWidget(quit_button)

        vert_box = QVBoxLayout()
        vert_box.addLayout(row_box)
        vert_box.addStretch()
        vert_box.addLayout(column_box)
        vert_box.addStretch()
        vert_box.addLayout(align_box)
        vert_box.addStretch()
        vert_box.addLayout(player_box)
        vert_box.addStretch()
        vert_box.addLayout(buttons_box)

        widget = QWidget()
        widget.setLayout(vert_box)
        self.setCentralWidget(widget)

    def set_row(self, row):
        self.nb_row = int(row)

    def set_column(self, column):
        self.nb_column = int(column)

    def set_align(self, align):
        self.align = align

    def set_player(self, player):
        if player == "Red":
            self.player = Qt.red
        else:
            self.player = Qt.yellow

    def start(self):
        self.game = GameWindow(self.nb_row, self.nb_column, self.align, self.player)
        self.game.show()
        self.hide()

    def quit(self):
        self.close()


class GameWindow(QMainWindow):
    def __init__(self, nb_row=6, nb_col=7, align=4, player=Qt.red):
        super(GameWindow, self).__init__()
        self.nb_row = nb_row
        self.nb_col = nb_col
        self.align = align
        self.player = player
        self.setWindowTitle("Puissance 4 - Play game")

        self.grid = Grid()
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(3)
        self.init_grid()

        if self.player == Qt.red:
            self.title = QLabel(f"RED's turn")
        else:
            self.title =QLabel(f"YELLOW's turn")

        widget = QWidget()
        vb = QVBoxLayout()
        vb.addWidget(self.title)
        vb.addLayout(self.grid_layout)
        widget.setLayout(vb)
        self.setCentralWidget(widget)

    def init_grid(self):
        for i in range(self.nb_row):
            for j in range(self.nb_col):
                c = Cell(i, j)
                self.grid_layout.addWidget(c, i, j)
                c.clicked.connect(self.click)
                c.set()

    def click(self, col):
        if not self.grid.is_column_full(col) and not self.grid.winner_present():
            if self.player == Qt.red:
                color = Color.RED
            else:
                color = Color.YELLOW
            x, y = self.grid.add_piece(color, col)
            cell = self.grid_layout.itemAtPosition(self.nb_row - x - 1, y).widget()
            cell.color = self.player
            cell.set()
            if self.grid.winner_present():
                self.title.setText(f"{color.name} wins!")
            else:
                self.change_player()

    def change_player(self):
        if self.player == Qt.red:
            self.player = Qt.yellow
            self.title.setText("Yellow's turn")
        else:
            self.player = Qt.red
            self.title.setText("Red's turn")


class Cell(QWidget):
    clicked = Signal(int)

    def __init__(self, x, y, *args, **kwargs):
        super(Cell, self).__init__(*args, **kwargs)
        self.x = x
        self.y = y
        self.setFixedSize(QSize(50, 50))
        self.color = Qt.white

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        r = event.rect()
        p.fillRect(r, QBrush(self.color))
        pen = QPen(Qt.lightGray)
        pen.setWidth(1)
        p.setPen(pen)
        p.drawRect(r)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.click()

    def click(self):
        self.clicked.emit(self.y)

    def set(self):
        self.update()


def main():
    app = QApplication(sys.argv)
    t = SettingsWindow()
    t.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

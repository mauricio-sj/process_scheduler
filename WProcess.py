import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QGridLayout, QHBoxLayout,
                             QInputDialog, QColorDialog, QApplication, QFontDialog, QMessageBox,
                             QSizePolicy, QDialog, QLabel, QTextEdit, QAction, QFileDialog, QMainWindow, QVBoxLayout, QSpinBox)
from PyQt5.QtGui import QColor, QIcon

from process import Process

class Window_Process(QDialog):
    def __init__(self, id, process, parent):
        super().__init__(parent)

        self.id = id
        self.startTime = 0
        self.executionTime = 1
        self.deadlineTime = 1
        self.priorityTime = 0
        self.pagesNumber = 1
        self.process = process

        self.setWindowIcon(QIcon('feature.png'))

        layout = QGridLayout()

        label_style = "QLabel { background-color: #3498db; color: white; padding: 5px; border-radius: 5px; }"
        spinbox_style = "QSpinBox { background-color: #ecf0f1; color: #2c3e50; padding: 5px; border-radius: 5px; }"
        button_style = "QPushButton { background-color: #2ecc71; color: white; padding: 5px; border-radius: 5px; }"

        self.start = QLabel("Chegada")
        self.start.setAlignment(Qt.AlignCenter)
        self.start.setStyleSheet(label_style)
        self.start_sp = QSpinBox()
        self.start_sp.setStyleSheet(spinbox_style)

        self.execution = QLabel("Tempo de execução")
        self.execution.setAlignment(Qt.AlignCenter)
        self.execution.setStyleSheet(label_style)
        self.execution_sp = QSpinBox()
        self.execution_sp.setStyleSheet(spinbox_style)
        self.execution_sp.setMinimum(1)

        self.deadline = QLabel("Deadline")
        self.deadline.setAlignment(Qt.AlignCenter)
        self.deadline.setStyleSheet(label_style)
        self.deadline_sp = QSpinBox()
        self.deadline_sp.setStyleSheet(spinbox_style)
        self.deadline_sp.setMinimum(self.executionTime)

        self.priority = QLabel("Prioridade")
        self.priority.setAlignment(Qt.AlignCenter)
        self.priority.setStyleSheet(label_style)
        self.priority_sp = QSpinBox()
        self.priority_sp.setStyleSheet(spinbox_style)

        self.pages = QLabel("Páginas")
        self.pages.setAlignment(Qt.AlignCenter)
        self.pages.setStyleSheet(label_style)
        self.pages_sp = QSpinBox()
        self.pages_sp.setStyleSheet(spinbox_style)
        self.pages_sp.setMaximum(10)
        self.pages_sp.setMinimum(1)

        self.btnOK = QPushButton('Criar', self)
        self.btnOK.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btnOK.setStyleSheet(button_style)

        self.btnCancel = QPushButton('Cancelar', self)
        self.btnCancel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btnCancel.setStyleSheet(button_style)

        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnOK)
        layoutBtn.addWidget(self.btnCancel)

        layout.addWidget(self.start, 0, 0)
        layout.addWidget(self.start_sp, 0, 1)
        layout.addWidget(self.execution, 1, 0)
        layout.addWidget(self.execution_sp, 1, 1)
        layout.addWidget(self.deadline, 2, 0)
        layout.addWidget(self.deadline_sp, 2, 1)
        layout.addWidget(self.priority, 3, 0)
        layout.addWidget(self.priority_sp, 3, 1)
        layout.addWidget(self.pages, 4, 0)
        layout.addWidget(self.pages_sp, 4, 1)
        layout.addLayout(layoutBtn, 5, 0, 1, 2)

        self.start_sp.valueChanged.connect(self.startvalue)
        self.execution_sp.valueChanged.connect(self.executionvalue)
        self.deadline_sp.valueChanged.connect(self.deadlinevalue)
        self.priority_sp.valueChanged.connect(self.priorityvalue)
        self.pages_sp.valueChanged.connect(self.pagesvalue)
        self.btnOK.clicked.connect(self.createProcess)
        self.btnCancel.clicked.connect(self.cancelProcess)

        self.setLayout(layout)
        self.setWindowTitle("Processo "+ str(id))

    def startvalue(self):
        self.start.setText("Valor chegada : " + str(self.start_sp.value()))
        self.startTime = self.start_sp.value()

    def executionvalue(self):
        self.execution.setText("Valor de execução : " + str(self.execution_sp.value()))
        self.executionTime = self.execution_sp.value()
        if self.deadlineTime < self.executionTime:
            self.deadline_sp.setValue(self.executionTime)
        self.deadline_sp.setMinimum(self.executionTime)

    def deadlinevalue(self):
        self.deadline.setText("Valor de deadline : " + str(self.deadline_sp.value()))
        self.deadlineTime = self.deadline_sp.value()

    def priorityvalue(self):
        self.priority.setText("Valor de prioridade : " + str(self.priority_sp.value()))
        self.priorityTime = self.priority_sp.value()

    def pagesvalue(self):
        self.pages.setText("Páginas : " + str(self.pages_sp.value()))
        self.pagesNumber = self.pages_sp.value()

    def createProcess(self):
        reply = QMessageBox.question(self, 'Criar',
                                     "Quer mesmo criar? ", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            self.process = Process(self.id, self.startTime, self.executionTime, self.pagesNumber, self.deadlineTime, priority=self.priorityTime)

            self.close()

    def cancelProcess(self):
        reply = QMessageBox.question(self, 'Cancelar',
                                     "Quer mesmo cancelar? ", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.process = None
            self.close()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Window_Process(1)
#     sys.exit(app.exec_())

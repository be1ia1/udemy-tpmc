from PyQt6.QtWidgets import QApplication, QWidget, \
                            QLabel, QGridLayout, \
                            QComboBox, QLineEdit, \
                            QPushButton
import sys

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Average Speed Calculator')
        grid = QGridLayout()

        distance_label = QLabel('Distance:')
        self.distance_label_line_edit = QLineEdit('')
        self.metric_system_box = QComboBox(self)
        self.metric_system_box.addItems(['Metric(km)', 'Imperial(miles)'])
        time_label = QLabel('Time(hours):')
        self.time_label_line_edit = QLineEdit('')
        calculate_button = QPushButton('Calculate')
        calculate_button.clicked.connect(self.calculate)
        self.answer_label = QLabel('')

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_label_line_edit, 0, 1)
        grid.addWidget(self.metric_system_box, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_label_line_edit, 1, 1)
        grid.addWidget(calculate_button, 3, 1)
        grid.addWidget(self.answer_label, 4, 0)

        self.setLayout(grid)
    
    def calculate(self):
        speed = float(self.distance_label_line_edit.text()) / float(self.time_label_line_edit.text())
        metric_system = self.metric_system_box.currentText()
        if metric_system == 'Metric(km)':
            self.answer_label.setText(f'Average Speed: {speed:.2f} km/h')
        else:
            self.answer_label.setText(f'Average Speed: {speed * 0.621371:.2f} mph')

app = QApplication(sys.argv)
speed_calc = SpeedCalculator()
speed_calc.show()
sys.exit(app.exec())

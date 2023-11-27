# Import PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QSlider, QSpinBox, QCheckBox, QRadioButton, QComboBox, QProgressBar, QCalendarWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

# Create a subclass of QWidget to hold the interface
class Example(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.setWindowTitle("PyQt5 Widgets Example")
        self.resize(800, 600)

        # Create a vertical layout to arrange the widgets
        self.layout = QVBoxLayout()

        # Create a label and a button
        self.label = QLabel("Hello, PyQt5!")
        self.button = QPushButton("Click Me")

        # Connect the button's clicked signal to a custom slot
        self.button.clicked.connect(self.on_button_clicked)

        # Add the label and the button to the layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        # Create a text edit and a slider
        self.text_edit = QLineEdit()
        self.slider = QSlider(Qt.Horizontal)

        # Connect the slider's value changed signal to a custom slot
        self.slider.valueChanged.connect(self.on_slider_changed)

        # Add the text edit and the slider to the layout
        self.layout.addWidget(self.text_edit)
        self.layout.addWidget(self.slider)

        # Create a spin box and a check box
        self.spin_box = QSpinBox()
        self.check_box = QCheckBox("Check Me")

        # Connect the check box's state changed signal to a custom slot
        self.check_box.stateChanged.connect(self.on_check_box_changed)

        # Add the spin box and the check box to the layout
        self.layout.addWidget(self.spin_box)
        self.layout.addWidget(self.check_box)

        # Create a horizontal layout to hold the radio buttons
        self.radio_layout = QHBoxLayout()

        # Create three radio buttons and add them to the radio layout
        self.radio_button_1 = QRadioButton("Option 1")
        self.radio_button_2 = QRadioButton("Option 2")
        self.radio_button_3 = QRadioButton("Option 3")
        self.radio_layout.addWidget(self.radio_button_1)
        self.radio_layout.addWidget(self.radio_button_2)
        self.radio_layout.addWidget(self.radio_button_3)

        # Add the radio layout to the main layout
        self.layout.addLayout(self.radio_layout)

        # Create a combo box and a progress bar
        self.combo_box = QComboBox()
        self.progress_bar = QProgressBar()

        # Add some items to the combo box
        self.combo_box.addItem("Item 1")
        self.combo_box.addItem("Item 2")
        self.combo_box.addItem("Item 3")

        # Connect the combo box's current index changed signal to a custom slot
        self.combo_box.currentIndexChanged.connect(self.on_combo_box_changed)

        # Add the combo box and the progress bar to the layout
        self.layout.addWidget(self.combo_box)
        self.layout.addWidget(self.progress_bar)

        # Create a calendar widget
        self.calendar = QCalendarWidget()

        # Connect the calendar's selection changed signal to a custom slot
        self.calendar.selectionChanged.connect(self.on_calendar_changed)

        # Add the calendar to the layout
        self.layout.addWidget(self.calendar)

        # Set the layout of the widget
        self.setLayout(self.layout)

    # Define the custom slots
    def on_button_clicked(self):
        # Change the label's text when the button is clicked
        self.label.setText("You clicked the button!")

    def on_slider_changed(self, value):
        # Set the text edit's text to the slider's value
        self.text_edit.setText(str(value))

    def on_check_box_changed(self, state):
        # Set the spin box's value to 0 or 100 depending on the check box's state
        if state == Qt.Checked:
            self.spin_box.setValue(100)
        else:
            self.spin_box.setValue(0)

    def on_combo_box_changed(self, index):
        # Set the progress bar's value to the combo box's current index
        self.progress_bar.setValue(index + 1)

    def on_calendar_changed(self):
        # Get the selected date from the calendar
        date = self.calendar.selectedDate()

        # Set the label's text to the date in ISO format
        self.label.setText(date.toString(Qt.ISODate))

# Create an instance of QApplication
app = QApplication([])

# Create an instance of Example
example = Example()

# Show the widget
example.show()

# Start the application's event loop
app.exec()

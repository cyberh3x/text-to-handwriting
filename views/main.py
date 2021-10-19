from PyQt5.QtWidgets import QTextEdit, QPushButton, QMessageBox
from modules.text_to_handwriting import converter


class MainView:
    def __init__(self, layout):
        self.layout = layout
        self.text_box = QTextEdit()
        self.text_box.setPlaceholderText("Type your text...")
        self.submit_button = QPushButton("Convert to Handwrite")
        self.converter = converter.Converter

    def onSubmit(self):
        self.disableSubmitButton()
        text = self.text_box.toPlainText()
        save = self.converter(text).convert()
        message = "Handwriting created successfully!\nPath: {path}"
        message_box = QMessageBox()
        message_box.setIcon(message_box.Information)
        message_box.setWindowTitle("Success")
        message_box.setText(message.format(path=save))
        message_box.exec_()
        self.clearTextBox()
        self.enableSubmitButton()

    def disableSubmitButton(self):
        self.submit_button.setDisabled(True)

    def enableSubmitButton(self):
        self.submit_button.setDisabled(False)

    def clearTextBox(self):
        self.text_box.setText("")

    def render(self):
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.submit_button)
        self.submit_button.clicked.connect(lambda: self.onSubmit())
        return self.text_box, self.submit_button

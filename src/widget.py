from PySide6.QtCore import Qt, QDateTime
from ui_widget import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem
from PySide6.QtGui import QColor
from photoshopFunctions import *
from generateDetail import *
import os
import uuid

DOWNLOAD_PATH = r"C:\Users\kmyn7\Dropbox\generative projects\bankSimulator\downloads"
HEIGHT_VALUE = 529
WIDTH_VALUE = 774

class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("bankSimulator")

        self.setGeometry(200, 100, WIDTH_VALUE, HEIGHT_VALUE)
        self.setMaximumHeight(HEIGHT_VALUE)
        self.setMaximumWidth(WIDTH_VALUE)

# TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO 
        self.shopnames = ["customizedblankets4u", "ashleysblanketgifts"]  # List to hold shop names 
        self.descriptions = ["cool shit but died", "hell nah"]  # List of descriptions  
# TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO 

        # Initialize a list to store uploaded file paths and shops
        self.uploaded_files = []
        self.selected_shops = []

        self.upload_button.setAcceptDrops(True)
        # Connect the dragEnterEvent and dropEvent to the upload button
        self.upload_button.dragEnterEvent = self.dragEnterEvent
        self.upload_button.dropEvent = self.dropEvent

        # Connect the clicked signal of the upload button to the uploadButton method
        self.upload_button.clicked.connect(self.uploadButton)
        self.submit_button.clicked.connect(self.submitButton)
        self.toggle_button.clicked.connect(self.toggleButton)
        self.clear_button.clicked.connect(self.clearButton)

        self.shopname_list.clicked.connect(self.updateDescription)
        self.repopulateList()

    def clearButton(self):
        self.uploaded_files = []
        self.updateSelectedLabel()

    def uploadButton(self):
        # Open a file dialog to select JPEG files
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("JPEG Files (*.jpeg *.jpg)")

        if file_dialog.exec():
            # Get the selected file paths
            selected_files = file_dialog.selectedFiles()
            self.uploaded_files.extend(selected_files)
            # Do something with the selected files, e.g., display images
        self.uploaded_files = [x for i, x in enumerate(self.uploaded_files) if self.uploaded_files.index(x) == i]
        self.updateSelectedLabel()

    # Create a drag enter event handler
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    # Create a drop event handler
    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.endswith(('.jpeg', '.jpg')):
                self.uploaded_files.append(file_path)
                # Do something with the selected files, e.g., display images
        self.uploaded_files = [x for i, x in enumerate(self.uploaded_files) if self.uploaded_files.index(x) == i]
        self.updateSelectedLabel()

    def updateSelectedLabel(self):
        current_text = f"{len(self.uploaded_files)} selected."
        if len(self.uploaded_files) == 0:
            current_text = "0 Selected."
        self.selected_label.setText(current_text)

    def submitButton(self):
        user_input = self.user_input.text()
        self.selected_shops = []
        for row in range(self.shopname_list.count()):
            item = self.shopname_list.item(row)
            if item.checkState() == Qt.Checked:
                self.selected_shops.append(item.text())
        if user_input == "" or len(self.selected_shops) == 0 or len(self.uploaded_files) == 0:
            self.action_label.setText("Fill out all fields.")
            return 1
        self.updateHistory(user_input, self.selected_shops, self.uploaded_files)
        for shop in self.selected_shops:
            for image in self.uploaded_files:
                generated_info = generate_details(shop, user_input)
                title = generated_info["title"]
                tag = generated_info["tag"]
                description = generated_info["description"]
                random_uuid = uuid.uuid4()
                new_folder_path = f"{DOWNLOAD_PATH}/{random_uuid}"
                if not os.path.exists(new_folder_path):
                    # Create the new folder
                    os.makedirs(new_folder_path)
                else:
                    print("Folder already exists.")

                text_file_path = os.path.join(new_folder_path, "generated_info.txt")
                with open(text_file_path, "w") as file:
                    # Write into the file
                    file.write(f"Title:\n{title}\n\n")
                    file.write(f"Tags:\n{tag}\n\n")
                    file.write(f"Description:\n{description}\n\n")
            
                uploadImage([image], f"{random_uuid}", "design", f"{shop}", "replacement")
                downloadImage([new_folder_path], f"{random_uuid}", "design", f"{shop}", "replacement")
# TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO 
                for i in range(2):
                    replaceSmartObject(f"mockup{str(i+1)}", f"{random_uuid}", "design", "Design #1", "output", "input", "replacement", f"{shop}")
                    downloadImage([new_folder_path], f"{random_uuid}", f"mockup{str(i+1)}", f"{shop}", "output")
                    replaceSmartObject(f"supporting{str(i+1)}", f"{random_uuid}", "design", "Design #1", "output", "supporting", "replacement", f"{shop}")
                    downloadImage([new_folder_path], f"{random_uuid}", f"supporting{str(i+1)}", f"{shop}", "output")
# TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO 
                print("Success!")

                
    def toggleButton(self):
        for row in range(self.shopname_list.count()):
            item = self.shopname_list.item(row)
            if item.checkState() == Qt.Checked:
                item.setCheckState(Qt.Unchecked)
            else:
                item.setCheckState(Qt.Checked)

    def repopulateList(self):
        for shopname in self.shopnames:
            item = QListWidgetItem(shopname)
            item.setCheckState(Qt.Unchecked)
            self.shopname_list.addItem(item)

    def updateHistory(self, user_input, selected_shops, file_paths):
        files = []
        for file in file_paths:
            filename = os.path.basename(file)
            files.append(filename)
        entry = "-----------------------------------------------------------\n"
        entry += f"User Input: {user_input}\n"
        entry += "Selected Shops: " + ", ".join(selected_shops) + "\n"
        entry += "Uploaded Files: " + ", ".join(files) + "\n"
        entry += "Date and Time: " + QDateTime.currentDateTime().toString(Qt.DateFormat.ISODate)

        item = QListWidgetItem(entry)  # Create a QListWidgetItem with the entry text
        self.terminal.addItem(item)     # Add the item to the terminal QListWidget

        if self.terminal.count() > 4:
            self.terminal.takeItem(0)  # Remove the oldest item

    def updateDescription(self, index):
        if index.isValid() and index.row() < len(self.descriptions):
            desc = self.descriptions[index.row()]
            self.description.setPlainText(desc)
        else:
            self.description.clear()

if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    app.exec()

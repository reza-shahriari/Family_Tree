# Import PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QGridLayout, QListWidget, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtCore import Qt,QTimer

# Import custom classes 
from Person import Person
from Tree import FamilyTree
from Name import name_generator
name_gen = name_generator()
#other imports
import random
import numpy as np
import cv2
from PIL import Image, ImageQt
# Define the main menu widget class
class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        # Set the window title and size
        self.setWindowTitle("Main Menu")
        self.resize(300, 200)
        # Create a grid layout to arrange the buttons
        layout = QGridLayout()
        # Create the buttons and connect them to the functions
        self.button1 = QPushButton("See the tree")
        self.button1.clicked.connect(self.SeeTheTree)
        self.button2 = QPushButton("Work with functions")
        self.button2.clicked.connect(self.OpneSubMenu)
        self.button3 = QPushButton("Exit")
        self.button3.clicked.connect(self.ConfirmExit)
        # Add the buttons to the layout
        layout.addWidget(self.button1, 0, 0)
        layout.addWidget(self.button2, 0, 1)
        layout.addWidget(self.button3, 1, 0, 1, 2)
        # Set the layout for the widget
        self.setLayout(layout)
    def SeeTheTree(self):
        h,w,cordinates = tree.VisualizeTree()
        im = np.ones((h,w,3), dtype=np.uint8)*255
        print(im.shape)
        all_persons = Person.all_persons
        for i in all_persons:
            cv2.circle(im,cordinates[i],10,(153,153,0),-1)
            im = cv2.putText(im,i.name,(cordinates[i][0]+10,cordinates[i][1]-10),cv2.FONT_HERSHEY_SIMPLEX 
                             ,.5,(102,204,0),2,cv2.LINE_AA)
        for i in all_persons:
            for child in i.children:
                cv2.line(im,cordinates[i],cordinates[child],(94,194,0),2)
        # Create an instance of the sub menu widget
        self.res_screen = ResScreen('Family Tree',self,im)
        # Show the sub menu and hide the main menu
        self.res_screen.show()
        self.hide()
    # Define the method to open the sub menu
    def OpneSubMenu(self):
        # Create an instance of the sub menu widget
        self.sub_menu = SubMenu()
        # Show the sub menu and hide the main menu
        self.sub_menu.show()
        self.hide()

    # Define the method to confirm exit
    def ConfirmExit(self):
        # Create a message box to ask the user if they are sure
        reply = QMessageBox.question(self, "Exit", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # If the user clicks yes, exit the app
        if reply == QMessageBox.Yes:
            QApplication.instance().quit()
        # Otherwise, do nothing

# Define the sub menu widget class
class SubMenu(QWidget):
    def __init__(self):
        super().__init__()
        # Set the window title and size
        self.setWindowTitle("Sub Menu")
        self.resize(400, 300)
        # Create a grid layout to arrange the buttons
        layout = QGridLayout()
        # Create the buttons and connect them to the functions
        self.button1 = QPushButton("Add new person")
        self.button1.clicked.connect(self.function1)
        self.button2 = QPushButton("Remove a person")
        self.button2.clicked.connect(self.function2)
        self.button3 = QPushButton("Check if parent")
        self.button3.clicked.connect(self.function3)
        self.button4 = QPushButton("Find lowest common ancestor")
        self.button4.clicked.connect(self.function4)
        self.button5 = QPushButton("Find Farest born")
        self.button5.clicked.connect(self.function5)
        self.button6 = QPushButton("Find Farest realationship")
        self.button6.clicked.connect(self.function6)
        self.button7 = QPushButton("Find path between 2 persons")
        self.button7.clicked.connect(self.function7)
        self.button8 = QPushButton("see size")
        self.button8.clicked.connect(self.function8)
        self.button9 = QPushButton("Back to main menu")
        self.button9.clicked.connect(self.back_to_main_menu)
        # Add the buttons to the layout
        layout.addWidget(self.button1, 0, 0)
        layout.addWidget(self.button2, 0, 1)
        layout.addWidget(self.button3, 0, 2)
        layout.addWidget(self.button4, 0, 3)
        layout.addWidget(self.button5, 1, 0)
        layout.addWidget(self.button6, 1, 1)
        layout.addWidget(self.button7, 1, 2)
        layout.addWidget(self.button8, 1, 3)
        layout.addWidget(self.button9, 2, 0, 1, 4)
        # Set the layout for the widget
        self.setLayout(layout)

    # Define the methods for the functions
    def function1(self):
        # Create an instance of the new screen widget
        self.new_screen = AddPersonScreen(self)
        # Show the new screen and hide the sub menu
        self.new_screen.show()
        self.hide()

    def function2(self):
        # Create an instance of the new screen widget
        self.new_screen = RemovePersonScreen(self)
        # Show the new screen and hide the sub menu
        self.new_screen.show()
        self.hide()

    def function3(self):
        # Create an instance of the new screen widget
        self.new_screen = CheckIfParentScreen(self)
        # Show the new screen and hide the sub menu
        self.new_screen.show()
        self.hide()

    def function4(self):
        # Create an instance of the new screen widget
        self.new_screen = FindLCAScreen(self)
        # Show the new screen and hide the sub menu
        self.new_screen.show()
        self.hide()

    def function5(self):
        # Create an instance of the new screen widget
        self.new_screen = FindFarestBornScreen(self)
        # Show the new screen and hide the sub menu
        self.new_screen.show()
        self.hide()

    def function6(self):
        # Create an instance of the new screen widget
        self.new_screen = FindFarestRealationScreen(self)
        # Show the new screen and hide the sub menu
        self.new_screen.show()
        self.hide()

    def function7(self):
        # Create an instance of the new screen widget
        self.new_screen = FindRelationbtw2(self)
        # Show the new screen and hide the sub menu
        self.new_screen.show()
        self.hide()
    
    def function8(self):
        # Create an instance of the new screen widget
        self.new_screen = GetSizeScreen(self)
        # Show the new screen and hide the sub menu
        self.new_screen.show()
        self.hide()

    # Define the method to go back to the main menu
    def back_to_main_menu(self):
        # Show the main menu and close the sub menu
        main_menu.show()
        self.close()

# Define the AddPersonScreen widget class
class AddPersonScreen(QWidget):
    def __init__(self,submenu):
        super().__init__()
        # Set the window title and size
        self.setWindowTitle("Add person Screen")
        self.resize(300, 200)
        # Create a grid layout to arrange the widgets
        layout = QGridLayout()
        # Create a list widget and add some items to it
        self.list_widget = QListWidget()
        options = tree.GetAllPersons()
        self.list_widget.addItems(options)
        # Create two input widgets and a button widget
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.button = QPushButton("Add Child")
        # Connect the button's clicked signal to a function
        self.button.clicked.connect(self.get_inputs_and_option)
        # Add the widgets to the layout
        self.list_label = QLabel("Choose The parent(name_birthday)")
        self.input1_label = QLabel("Enter child's name")
        self.input2_label = QLabel("Enter child's birthday")
        
        layout.addWidget(self.list_widget, 1, 0, 1, 2)
        layout.addWidget(self.input1, 3, 0)
        layout.addWidget(self.input2, 3, 1)
        layout.addWidget(self.button, 4, 0, 1, 2)
        # Add the labels to the layout
        layout.addWidget(self.list_label, 0, 0, 1, 2, alignment=Qt.AlignTop | Qt.AlignLeft)
        layout.addWidget(self.input1_label, 2, 0, alignment=Qt.AlignTop | Qt.AlignLeft)
        layout.addWidget(self.input2_label, 2, 1, alignment=Qt.AlignTop | Qt.AlignLeft)
        
        # Set the layout for the widget
        self.setLayout(layout)
        self.submenu = submenu
    # Define the function to get the inputs and the option
    def get_inputs_and_option(self):
        # Get the text from the input widgets
        input1 = self.input1.text()
        input2 = self.input2.text()
        # Get the current item from the list widget
        option = self.list_widget.currentItem().text() if self.list_widget.currentItem() is not None else ""
        # Call another function with the inputs and the option
        if input2 != '' and input2 != '' and option != '':
            text = tree.AddPerson(option.split('_')[0].strip(), int(option.split('_')[1].strip()),input1, input2)
        # Create an instance of the screen that shows the text
        else:
            text = 'Wrong inputs...'
        self.text_screen = ResScreen(text,self.submenu)
        # Show the text screen and hide the new screen
        self.text_screen.show()
        self.hide()

# Define the RemovePersonScreen widget class
class RemovePersonScreen(QWidget):
    def __init__(self,submenu):
        super().__init__()
        # Set the window title and size
        self.setWindowTitle("Remove Person Screen")
        self.resize(300, 200)
        # Create a grid layout to arrange the widgets
        layout = QGridLayout()
        # Create a list widget and add some items to it
        self.list_widget = QListWidget()
        options = tree.GetAllPersons()
        self.list_widget.addItems(options)
        self.button = QPushButton("Remove Person")
        # Connect the button's clicked signal to a function
        self.button.clicked.connect(self.get_inputs_and_option)
        # Add the widgets to the layout
        self.list_label = QLabel("Choose a Person(name_birthday)")
        layout.addWidget(self.list_widget, 1, 0, 1, 2)
        layout.addWidget(self.button, 2, 0, 1, 2)
        # Add the labels to the layout
        layout.addWidget(self.list_label, 0, 0, 1, 2, alignment=Qt.AlignTop | Qt.AlignLeft)
        
        # Set the layout for the widget
        self.setLayout(layout)
        self.submenu = submenu
    # Define the function to get the inputs and the option
    def get_inputs_and_option(self):
        # Get the text from the input widgets
        # Get the current item from the list widget
        option = self.list_widget.currentItem().text() if self.list_widget.currentItem() is not None else ""
        # Call another function with the inputs and the option
        if  option != '':
            text = tree.RemovePerson(option.split('_')[0].strip(), int(option.split('_')[1].strip()))
        # Create an instance of the screen that shows the text
        else:
            text = 'Wrong inputs...'
        self.text_screen = ResScreen(text,self.submenu)
        # Show the text screen and hide the new screen
        self.text_screen.show()
        self.hide()

# Define the CheckIfParent widget class
class CheckIfParentScreen(QWidget):
    def __init__(self,submenu):
        super().__init__()
        # Set the window title and size
        self.setWindowTitle("Check If Parent Screen")
        self.resize(300, 200)
        # Create a grid layout to arrange the widgets
        layout = QGridLayout()
        # Create a list widget and add some items to it
        self.list_widget1 = QListWidget()
        self.list_widget2 = QListWidget()
        options = tree.GetAllPersons()
        self.list_widget1.addItems(options)
        self.list_widget2.addItems(options)
        self.button = QPushButton("Check")
        # Connect the button's clicked signal to a function
        self.button.clicked.connect(self.get_inputs_and_option)
        # Add the widgets to the layout
        self.list_label1 = QLabel("Choose The Parent")
        self.list_label2 = QLabel("Choose The Child")
        layout.addWidget(self.list_widget1, 1, 0, 1, 2)
        layout.addWidget(self.list_widget2, 3, 0, 1, 2)
        layout.addWidget(self.button, 4, 0, 1, 2)
        # Add the labels to the layout
        layout.addWidget(self.list_label1, 0, 0, 1, 2, alignment=Qt.AlignTop | Qt.AlignLeft)
        layout.addWidget(self.list_label2, 2, 0, 1, 2, alignment=Qt.AlignTop | Qt.AlignLeft)
        
        # Set the layout for the widget
        self.setLayout(layout)
        self.submenu = submenu
    # Define the function to get the inputs and the option
    def get_inputs_and_option(self):
        # Get the text from the input widgets
        # Get the current item from the list widget
        parent = self.list_widget1.currentItem().text() if self.list_widget1.currentItem() is not None else ""
        child = self.list_widget2.currentItem().text() if self.list_widget2.currentItem() is not None else ""
        # Call another function with the inputs and the option
        if  parent != '' and child != '':
            text = tree.CheckIsParent(parent.split('_')[0].strip(), int(parent.split('_')[1].strip()),child.split('_')[0].strip(), int(child.split('_')[1].strip()))
        # Create an instance of the screen that shows the text
        else:
            text = 'Wrong inputs...'
        self.text_screen = ResScreen(text,self.submenu)
        # Show the text screen and hide the new screen
        self.text_screen.show()
        self.hide()

# Define the FindLCA widget class
class FindLCAScreen(QWidget):
    def __init__(self,submenu):
        super().__init__()
        # Set the window title and size
        self.setWindowTitle("Find LCA screen")
        self.resize(300, 200)
        # Create a grid layout to arrange the widgets
        layout = QGridLayout()
        # Create a list widget and add some items to it
        self.list_widget1 = QListWidget()
        self.list_widget2 = QListWidget()
        options = tree.GetAllPersons()
        self.list_widget1.addItems(options)
        self.list_widget2.addItems(options)
        self.button = QPushButton("Find")
        # Connect the button's clicked signal to a function
        self.button.clicked.connect(self.get_inputs_and_option)
        # Add the widgets to the layout
        self.list_label1 = QLabel("Choose person1")
        self.list_label2 = QLabel("Choose person2")
        layout.addWidget(self.list_widget1, 1, 0, 1, 2)
        layout.addWidget(self.list_widget2, 3, 0, 1, 2)
        layout.addWidget(self.button, 4, 0, 1, 2)
        # Add the labels to the layout
        layout.addWidget(self.list_label1, 0, 0, 1, 2, alignment=Qt.AlignTop | Qt.AlignLeft)
        layout.addWidget(self.list_label2, 2, 0, 1, 2, alignment=Qt.AlignTop | Qt.AlignLeft)
        
        # Set the layout for the widget
        self.setLayout(layout)
        self.submenu = submenu
    # Define the function to get the inputs and the option
    def get_inputs_and_option(self):
        # Get the text from the input widgets
        # Get the current item from the list widget
        person1 = self.list_widget1.currentItem().text() if self.list_widget1.currentItem() is not None else ""
        person2 = self.list_widget2.currentItem().text() if self.list_widget2.currentItem() is not None else ""
        # Call another function with the inputs and the option
        if  person1 != '' and person2 != '':
            text = tree.FindLCA(person1.split('_')[0].strip(), int(person1.split('_')[1].strip()),person2.split('_')[0].strip(), int(person2.split('_')[1].strip()))
        # Create an instance of the screen that shows the text
        else:
            text = 'Wrong inputs...'
        self.text_screen = ResScreen(text,self.submenu)
        # Show the text screen and hide the new screen
        self.text_screen.show()
        self.hide()

# Define the FindFarestBorn widget class
class FindFarestBornScreen(QWidget):
    def __init__(self,submenu):
        super().__init__()
        # Set the window title and size
        self.setWindowTitle("Find farest born  Screen")
        self.resize(300, 200)
        # Create a grid layout to arrange the widgets
        layout = QGridLayout()
        # Create a list widget and add some items to it
        self.list_widget = QListWidget()
        options = tree.GetAllPersons()
        self.list_widget.addItems(options)
        self.button = QPushButton("Find")
        # Connect the button's clicked signal to a function
        self.button.clicked.connect(self.get_inputs_and_option)
        # Add the widgets to the layout
        self.list_label = QLabel("Choose a Person(name_birthday)")
        layout.addWidget(self.list_widget, 1, 0, 1, 2)
        layout.addWidget(self.button, 2, 0, 1, 2)
        # Add the labels to the layout
        layout.addWidget(self.list_label, 0, 0, 1, 2, alignment=Qt.AlignTop | Qt.AlignLeft)
        
        # Set the layout for the widget
        self.setLayout(layout)
        self.submenu = submenu
    # Define the function to get the inputs and the option
    def get_inputs_and_option(self):
        # Get the text from the input widgets
        # Get the current item from the list widget
        option = self.list_widget.currentItem().text() if self.list_widget.currentItem() is not None else ""
        # Call another function with the inputs and the option
        if  option != '':
            text = tree.FindFarestBorn(option.split('_')[0].strip(), int(option.split('_')[1].strip()))
        # Create an instance of the screen that shows the text
        else:
            text = 'Wrong inputs...'
        self.text_screen = ResScreen(text,self.submenu)
        # Show the text screen and hide the new screen
        self.text_screen.show()
        self.hide()

# Define the FindFarestRealationScreen widget class
class FindFarestRealationScreen(QWidget):
    def __init__(self,submenu):
        super().__init__()
        # Set the window title and size
        self.setWindowTitle("farest realation Screen")
        self.resize(300, 200)
        # Create a grid layout to arrange the widgets
        layout = QGridLayout()
        # Create a list widget and add some items to it
        self.list_widget = QListWidget()
        options = tree.GetAllPersons()
        self.list_widget.addItems(options)
        self.button = QPushButton("Find")
        # Connect the button's clicked signal to a function
        self.button.clicked.connect(self.get_inputs_and_option)
        # Add the widgets to the layout
        self.list_label = QLabel("click Find to find farest realation in the family tree")
        layout.addWidget(self.button, 1, 0, 1, 2)
        # Add the labels to the layout
        layout.addWidget(self.list_label, 0, 0, 1, 2, alignment=Qt.AlignCenter )
        # Set the layout for the widget
        self.setLayout(layout)
        self.submenu = submenu
    # Define the function to get the inputs and the option
    def get_inputs_and_option(self):
        text = tree.FindFarestRelations()
        # Create an instance of the screen that shows the text
        self.text_screen = ResScreen(text,self.submenu)
        # Show the text screen and hide the new screen
        self.text_screen.show()
        self.hide()

# Define the FindRelationbtw2 widget class
class FindRelationbtw2(QWidget):
    def __init__(self,submenu):
        super().__init__()
        # Set the window title and size
        self.setWindowTitle("Find relation between 2 persons Screen")
        self.resize(300, 200)
        # Create a grid layout to arrange the widgets
        layout = QGridLayout()
        # Create a list widget and add some items to it
        self.list_widget1 = QListWidget()
        self.list_widget2 = QListWidget()
        options = tree.GetAllPersons()
        self.list_widget1.addItems(options)
        self.list_widget2.addItems(options)
        self.button = QPushButton("Check")
        # Connect the button's clicked signal to a function
        self.button.clicked.connect(self.get_inputs_and_option)
        # Add the widgets to the layout
        self.list_label1 = QLabel("Choose The Person1")
        self.list_label2 = QLabel("Choose The Person2")
        layout.addWidget(self.list_widget1, 1, 0, 1, 2)
        layout.addWidget(self.list_widget2, 3, 0, 1, 2)
        layout.addWidget(self.button, 4, 0, 1, 2)
        # Add the labels to the layout
        layout.addWidget(self.list_label1, 0, 0, 1, 2, alignment=Qt.AlignTop | Qt.AlignLeft)
        layout.addWidget(self.list_label2, 2, 0, 1, 2, alignment=Qt.AlignTop | Qt.AlignLeft)
        
        # Set the layout for the widget
        self.setLayout(layout)
        self.submenu = submenu
    # Define the function to get the inputs and the option
    def get_inputs_and_option(self):
        # Get the text from the input widgets
        # Get the current item from the list widget
        person1 = self.list_widget1.currentItem().text() if self.list_widget1.currentItem() is not None else ""
        person2 = self.list_widget2.currentItem().text() if self.list_widget2.currentItem() is not None else ""
        # Call another function with the inputs and the option
        if  person1 != '' and person2 != '':
            text = tree.FindRelation(person1.split('_')[0].strip(), int(person1.split('_')[1].strip()),person2.split('_')[0].strip(), int(person2.split('_')[1].strip()))
            # Create an instance of the screen that shows the text
        else:
            text = 'Wrong inputs...'
        self.text_screen = ResScreen(text,self.submenu)
        # Show the text screen and hide the new screen
        self.text_screen.show()
        self.hide()

# Define the GetSize widget class
class GetSizeScreen(QWidget):
    def __init__(self,submenu):
        super().__init__()
        # Set the window title and size
        self.setWindowTitle("Size Screen")
        self.resize(300, 200)
        # Create a grid layout to arrange the widgets
        layout = QGridLayout()
        # Create a list widget and add some items to it
        self.list_widget = QListWidget()
        options = tree.GetAllPersons()
        self.list_widget.addItems(options)
        self.button = QPushButton("Show")
        # Connect the button's clicked signal to a function
        self.button.clicked.connect(self.get_inputs_and_option)
        # Add the widgets to the layout
        self.list_label = QLabel("click show to see size of family tree")
        layout.addWidget(self.button, 1, 0, 1, 2)
        # Add the labels to the layout
        layout.addWidget(self.list_label, 0, 0, 1, 2, alignment=Qt.AlignCenter )
        # Set the layout for the widget
        self.setLayout(layout)
        self.submenu = submenu
    # Define the function to get the inputs and the option
    def get_inputs_and_option(self):
        text = tree.GetSize()
        # Create an instance of the screen that shows the text
        self.text_screen = ResScreen(text,self.submenu)
        # Show the text screen and hide the new screen
        self.text_screen.show()
        self.hide()

class ResScreen(QWidget):

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        rgb_image = cv2.resize(rgb_image,(self.disply_width, self.display_height))
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        # p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(convert_to_Qt_format)

    def __init__(self, text, back_menu, image=None):
        super().__init__()
        # Set the window title and size
        self.setWindowTitle("Text Screen")
        self.disply_width = 1028 if image is not None else 300
        self.display_height = 640 if image is not None else 200
        self.image_label = QLabel(self)
        self.resize(self.disply_width, self.display_height)
        # Create a grid layout to arrange the widget
        layout = QGridLayout()
        # Create a label widget and set the text to the message
        self.label = QLabel()
        self.label.setText(text)
        # Add the label to the layout
        layout.addWidget(self.label, 1, 0, alignment=Qt.AlignCenter)
        if image is not None:
            img = self.convert_cv_qt(image)
            self.image_label.setPixmap(img)
            # Add the image to the layout
            layout.addWidget(self.image_label, 0, 0, alignment=Qt.AlignCenter)
        # Set the alignment and stretch of the layout
        layout.setAlignment(Qt.AlignCenter)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(2, 1)
        # Set the layout for the widget
        self.setLayout(layout)
        # Create a timer that will trigger a function after 3 seconds
        if image is None:
            QTimer.singleShot(2000, self.back_to_sub_menu)
        if image is not None:
            QTimer.singleShot(5000, self.back_to_sub_menu)
        self.back_menu = back_menu

    # Define the function that will be triggered by the timer
    def back_to_sub_menu(self):
        # Show the sub menu and close the text screen
        self.back_menu.show()
        self.close()

def custom_tree(tree: FamilyTree):
    global name, birthday
    for i in range(10):
        all_p = Person.all_persons
        p = random.choice(all_p)
        c_name = name_gen.generate()
        c_birth_day = random.randint(p.birth_day+20,p.birth_day +80)
        tree.AddPerson(p.name,p.birth_day,c_name,c_birth_day)

tree = FamilyTree('Reza',1700,1740)
tree.AddPerson('Reza',1700,'moh',1738)
custom_tree(tree)

app = QApplication([])
main_menu = MainMenu()
main_menu.show()
app.exec_()

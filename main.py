# Import PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QGridLayout, QListWidget, QLineEdit, QLabel
from PyQt5.QtCore import Qt,QTimer

# Import custom classes 
from Person import Person
from Tree import FamilyTree
from Name import name_generator
name_gen = name_generator()
#other imports
import random

# Define the functions that will be called when the buttons are clicked
def see_the_tree():
    print("See the tree function")

def work_with_functions():
    print("Work with functions function")

def exit_app():
    print("Exit app function")

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
        self.button1.clicked.connect(see_the_tree)
        self.button2 = QPushButton("Work with functions")
        self.button2.clicked.connect(self.open_sub_menu)
        self.button3 = QPushButton("Exit")
        self.button3.clicked.connect(self.confirm_exit)
        # Add the buttons to the layout
        layout.addWidget(self.button1, 0, 0)
        layout.addWidget(self.button2, 0, 1)
        layout.addWidget(self.button3, 1, 0, 1, 2)
        # Set the layout for the widget
        self.setLayout(layout)

    # Define the method to open the sub menu
    def open_sub_menu(self):
        # Create an instance of the sub menu widget
        self.sub_menu = SubMenu()
        # Show the sub menu and hide the main menu
        self.sub_menu.show()
        self.hide()

    # Define the method to confirm exit
    def confirm_exit(self):
        # Create a message box to ask the user if they are sure
        reply = QMessageBox.question(self, "Exit", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # If the user clicks yes, exit the app
        if reply == QMessageBox.Yes:
            exit_app()
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
        self.button2 = QPushButton("Function 2")
        self.button2.clicked.connect(self.function2)
        self.button3 = QPushButton("Function 3")
        self.button3.clicked.connect(self.function3)
        self.button4 = QPushButton("Function 4")
        self.button4.clicked.connect(self.function4)
        self.button5 = QPushButton("Function 5")
        self.button5.clicked.connect(self.function5)
        self.button6 = QPushButton("Function 6")
        self.button6.clicked.connect(self.function6)
        self.button7 = QPushButton("Function 7")
        self.button7.clicked.connect(self.function7)
        self.button8 = QPushButton("Function 8")
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
        print("Function 2")

    def function3(self):
        print("Function 3")

    def function4(self):
        print("Function 4")

    def function5(self):
        print("Function 5")

    def function6(self):
        print("Function 6")

    def function7(self):
        print("Function 7")

    def function8(self):
        print("Function 8")

    # Define the method to go back to the main menu
    def back_to_main_menu(self):
        # Show the main menu and close the sub menu
        main_menu.show()
        self.close()

# Define the new screen widget class
class AddPersonScreen(QWidget):
    def __init__(self,submenu):
        super().__init__()
        # Set the window title and size
        self.setWindowTitle("New Screen")
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
        self.list_label = QLabel("Choose a Person(name_birthday)")
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
        option = self.list_widget.currentItem().text()
        # Call another function with the inputs and the option
        if input2 != '' and input2 != '' and option != '':
            text = tree.AddPerson(option.split('_')[0].strip(), int(option.split('_')[1].strip()),input1, input2)
        # Create an instance of the screen that shows the text
        else:
            text = 'Wrong inputs...'
        self.text_screen = TextScreen(text,self.submenu)
        # Show the text screen and hide the new screen
        self.text_screen.show()
        self.hide()


class TextScreen(QWidget):
    def __init__(self,text,back_menu):
        super().__init__()
        # Set the window title and size
        self.setWindowTitle("Text Screen")
        self.resize(200, 100)
        # Create a grid layout to arrange the widget
        layout = QGridLayout()
        # Create a label widget and set the text to the message
        self.label = QLabel()
        self.label.setText(text)
        # Add the label to the layout
        layout.addWidget(self.label, 0, 0, alignment=Qt.AlignCenter)
        # Set the layout for the widget
        self.setLayout(layout)
        # Create a timer that will trigger a function after 3 seconds
        QTimer.singleShot(2000, self.back_to_sub_menu)
        self.back_menu = back_menu
    # Define the function that will be triggered by the timer
    def back_to_sub_menu(self):
        # Show the sub menu and close the text screen
        self.back_menu.show()
        self.close()

           
        
name = ''
birthday = ''
def custom_tree(tree: FamilyTree):
    global name, birthday
    for i in range(10):
        all_p = Person.all_persons
        p = random.choice(all_p)
        print("parent is:",p.name)
        c_name = name_gen.generate()
        name = c_name
        c_birth_day = random.randint(p.birth_day+20,p.birth_day +80)
        birthday = c_birth_day
        tree.AddPerson(p.name,p.birth_day,c_name,c_birth_day)

tree = FamilyTree('Reza',1700,1740)
print(tree.root.name)
# custom_tree(tree)
# print(tree.All)
# tree.RemovePerson(name,birthday)
# print(tree.GetSize())
app = QApplication([])
main_menu = MainMenu()
main_menu.show()
app.exec_()

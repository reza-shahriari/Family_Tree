# Import PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QGridLayout
from PyQt5.QtCore import Qt

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
        self.sub_menu = SubMenu(self)
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
    def __init__(self,main_menu):
        super().__init__()
        # Set the window title and size
        self.setWindowTitle("Sub Menu")
        self.resize(400, 300)
        # Create a grid layout to arrange the buttons
        layout = QGridLayout()
        # Create the buttons and connect them to the functions
        self.button1 = QPushButton("Function 1")
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
        self.main_menu = main_menu
    # Define the methods for the functions
    def function1(self):
        print("Function 1")

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
        self.main_menu.show()
        self.close()

def custom_tree(tree: FamilyTree):
    for i in range(10):
        all_p = Person.all_persons
        p = random.choice(all_p)
        c_name = name_gen.generate()
        c_birth_day = random.randint(p.birth_day+20,p.birth_day +80)
        tree.AddPerson(p.name,p.birth_day,c_name,c_birth_day)

tree = FamilyTree('Reza',1700,1740)
custom_tree(tree)
print(tree.All)
app = QApplication([])
main_menu = MainMenu()
main_menu.show()
app.exec_()

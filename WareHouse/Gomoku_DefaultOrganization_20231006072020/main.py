'''
Main file for the virtual software company ChatDev.
'''
from tkinter import Tk, Button, Label, Frame
class ChatDevApp:
    def __init__(self, master):
        self.master = master
        master.title("ChatDev")
        self.frame = Frame(master)
        self.frame.pack()
        self.label = Label(self.frame, text="Welcome to ChatDev!")
        self.label.pack()
        self.design_button = Button(self.frame, text="Design", command=self.design)
        self.design_button.pack()
        self.code_button = Button(self.frame, text="Code", command=self.code)
        self.code_button.pack()
        self.test_button = Button(self.frame, text="Test", command=self.test)
        self.test_button.pack()
        self.document_button = Button(self.frame, text="Document", command=self.document)
        self.document_button.pack()
    def design(self):
        '''
        Designing...
        '''
        print("Designing...")
    def code(self):
        '''
        Coding...
        '''
        print("Coding...")
    def test(self):
        '''
        Testing...
        '''
        print("Testing...")
    def document(self):
        '''
        Documenting...
        '''
        print("Documenting...")
if __name__ == "__main__":
    root = Tk()
    app = ChatDevApp(root)
    root.mainloop()
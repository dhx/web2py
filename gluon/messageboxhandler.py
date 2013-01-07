import logging

try:
    import tkMessageBox
except:
    tkMessageBox = None

<<<<<<< HEAD
=======

>>>>>>> upstream/master
class MessageBoxHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):
        if tkMessageBox:
            msg = self.format(record)
            tkMessageBox.showinfo('info1', msg)
<<<<<<< HEAD


=======
>>>>>>> upstream/master

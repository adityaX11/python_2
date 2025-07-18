from db import init_db
from gui import ExpenseTrackerApp
import tkinter as tk

if __name__ == '__main__':
    init_db()
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop() 
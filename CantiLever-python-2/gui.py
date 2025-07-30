import tkinter as tk
from tkinter import ttk, messagebox
from db import init_db, add_category, get_categories, add_expense, get_expenses
from reports import plot_expenses_by_category, plot_expenses_over_time
from datetime import datetime

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Expense Tracker')
        self.create_widgets()
        self.refresh_categories()
        self.refresh_expenses()

    def create_widgets(self):
        # Add Expense Frame
        frame = ttk.LabelFrame(self.root, text='Add Expense')
        frame.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        ttk.Label(frame, text='Amount:').grid(row=0, column=0)
        self.amount_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.amount_var).grid(row=0, column=1)

        ttk.Label(frame, text='Category:').grid(row=0, column=2)
        self.category_var = tk.StringVar()
        self.category_cb = ttk.Combobox(frame, textvariable=self.category_var, state='readonly')
        self.category_cb.grid(row=0, column=3)

        ttk.Label(frame, text='Date (YYYY-MM-DD):').grid(row=0, column=4)
        self.date_var = tk.StringVar(value=datetime.now().strftime('%Y-%m-%d'))
        ttk.Entry(frame, textvariable=self.date_var, width=12).grid(row=0, column=5)

        ttk.Label(frame, text='Description:').grid(row=0, column=6)
        self.desc_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.desc_var, width=20).grid(row=0, column=7)

        ttk.Button(frame, text='Add', command=self.add_expense).grid(row=0, column=8, padx=5)

        # Add Category Frame
        cat_frame = ttk.LabelFrame(self.root, text='Add Category')
        cat_frame.grid(row=1, column=0, padx=10, pady=5, sticky='ew')
        self.new_cat_var = tk.StringVar()
        ttk.Entry(cat_frame, textvariable=self.new_cat_var, width=20).grid(row=0, column=0)
        ttk.Button(cat_frame, text='Add Category', command=self.add_category).grid(row=0, column=1, padx=5)

        # Expenses Table
        table_frame = ttk.LabelFrame(self.root, text='Expenses')
        table_frame.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
        self.tree = ttk.Treeview(table_frame, columns=('Amount', 'Category', 'Date', 'Description'), show='headings')
        for col in ('Amount', 'Category', 'Date', 'Description'):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(fill='both', expand=True)

        # Reports Buttons
        report_frame = ttk.Frame(self.root)
        report_frame.grid(row=3, column=0, pady=10)
        ttk.Button(report_frame, text='Pie Chart by Category', command=plot_expenses_by_category).pack(side='left', padx=5)
        ttk.Button(report_frame, text='Line Chart Over Time', command=plot_expenses_over_time).pack(side='left', padx=5)

        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def refresh_categories(self):
        categories = get_categories()
        self.category_cb['values'] = [name for _, name in categories]
        if categories:
            self.category_cb.current(0)

    def refresh_expenses(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for _, amount, category, date, desc in get_expenses():
            self.tree.insert('', 'end', values=(amount, category, date, desc))

    def add_expense(self):
        try:
            amount = float(self.amount_var.get())
            date_str = self.date_var.get()
            datetime.strptime(date_str, '%Y-%m-%d')  # Validate date
            desc = self.desc_var.get()
            category_name = self.category_var.get()
            categories = get_categories()
            category_id = None
            for cid, name in categories:
                if name == category_name:
                    category_id = cid
                    break
            if category_id is None:
                messagebox.showerror('Error', 'Please select a valid category.')
                return
            add_expense(amount, category_id, date_str, desc)
            self.refresh_expenses()
        except ValueError:
            messagebox.showerror('Error', 'Invalid input. Please check amount and date.')

    def add_category(self):
        name = self.new_cat_var.get().strip()
        if name:
            add_category(name)
            self.refresh_categories()
            self.new_cat_var.set('')
        else:
            messagebox.showerror('Error', 'Category name cannot be empty.')

if __name__ == '__main__':
    init_db()
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop() 
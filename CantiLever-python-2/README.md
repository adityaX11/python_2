# Expense Tracker

A simple expense tracker application with a GUI to input, categorize, and analyze your expenses.

## Features

- Add expenses with amount, category, date, and description
- Add custom categories
- View all expenses in a table
- Visualize spending by category (pie chart)
- Visualize spending over time (line chart)
- Data stored locally in SQLite database

## Technologies Used

- Python (Tkinter for GUI)
- SQLite (via `sqlite3`)
- Matplotlib (for charts)
- Standard library: datetime

## Installation

1. Clone this repository or download the files.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:

```bash
python main.py
```

## Notes

- The database file (`expenses.db`) will be created automatically in the project      directory.
- You can add new categories as needed.
- Use the report buttons to visualize your spending.

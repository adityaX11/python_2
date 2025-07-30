import matplotlib.pyplot as plt
from db import get_expenses
from collections import defaultdict
from datetime import datetime

def plot_expenses_by_category():
    expenses = get_expenses()
    category_totals = defaultdict(float)
    for _, amount, category, _, _ in expenses:
        if category:
            category_totals[category] += amount
        else:
            category_totals['Uncategorized'] += amount
    labels = list(category_totals.keys())
    sizes = list(category_totals.values())
    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Expenses by Category')
    plt.show()

def plot_expenses_over_time():
    expenses = get_expenses()
    date_totals = defaultdict(float)
    for _, amount, _, date_str, _ in expenses:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        date_totals[date.date()] += amount
    dates = sorted(date_totals.keys())
    totals = [date_totals[d] for d in dates]
    plt.figure(figsize=(8,4))
    plt.plot(dates, totals, marker='o')
    plt.title('Expenses Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.tight_layout()
    plt.show() 
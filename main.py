from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Текущая дата и время: {current_date}")

    calculate_salary()
    get_employees()

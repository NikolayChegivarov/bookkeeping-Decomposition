# импортирую модули основная функция сработать не должна
from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

print( )
# импортирую функции, должна сработать основная функция
calculate_salary()
get_employees()
current_date = datetime.datetime.now().date()
formatted_date = current_date.strftime("%d-%m-%Y")
print(f'Дата вызова функций: {formatted_date}')
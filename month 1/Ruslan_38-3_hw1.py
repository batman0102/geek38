mon = int(input("Расход за понедельник"))
tue = int(input("Расход за вторник"))
wed = int(input("Расход за среду"))
thur = int(input("Расход за четверг"))
fri = int(input("Расход за пятницу"))
sat = int(input("Расход за субботу"))
sun = int(input("Расход за воскресенье"))

summ = mon + tue + wed + thur + fri + sat + sun
print (f"Общая сумма расходов за неделю {summ} ")

days= 7
average_expense =  summ/days
average_expense = round(average_expense, 1)
print (f"Средний расход в день {average_expense} ")


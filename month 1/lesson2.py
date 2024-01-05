time = input( 'Введите время суток').lower()

if time == "morning" or time == "утро":
    print ("good morning")
elif time == "day" or time == 'день':
    print ("good afternoon")
elif time == "evening" or time == "вечер":
    print ("good evening")
else:
    print ('i don\'t know time')

mon = int(input("Расход за понедельник"))
tue = int(input("Расход за вторник"))
wed = int(input("Расход за среду"))
thur = int(input("Расход за четверг"))
fri = int(input("Расход за пятницу"))
sat = int(input("Расход за субботу"))
sun = int(input("Расход за воскресенье"))

summ = mon + tue + wed + thur + fri + sat + sun
print (f"Общая сумма расходов за неделю {summ}")

days= 7
average_expense =  summ/days
average_expense = round(average_expense, 1)
print (f"Средний расход в день {average_expense}")

if average_expense >= 5000:
    print ("Потратили много")
elif average_expense<=500 and average_expense >0:
    print ("Потратили мало")
elif average_expense>=501 or average_expense<=4999 and average_expense >0:
    print ("Потратили средне")
else:
    print ("Не потрачено ничего")































#print(1>2)
#print(2<3)
#print(2==2)
#print(2==2)
#print(1<=2)
#print(1>=2)
#print(1 > 2 and 2>1)
#print(2!=3)


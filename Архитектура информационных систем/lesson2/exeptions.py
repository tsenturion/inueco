"""
try - попытка выполнить ошибкойный код
except - если в try возникла ошибка, то выполняется код в except
в except можно указать тип ошибки
else - если в try не возникла ошибки, то выполняется код в else
finally - выполняется всегда
exit(1) - выход из программы с кодом 1
"""
try:
    print()

except ZeroDivisionError:
    print("You can't divide by zero")

except Exception as e:
    print(e)

else:
    print('ошибок нет')

finally:
    print("выполняется всегда")

exit(1)
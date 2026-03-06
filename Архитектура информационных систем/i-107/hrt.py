# 1
motto = "What Is Dead May Never Die!"
print(motto)
# 2
some_var = 'message'
# Записываем message в обратном порядке
some_var = some_var[::-1]  # теперь some_var = 'egassem'
# 3
brothers_count = 2
print(brothers_count)
# 4
euros_count = 100  # Исходное количество евро

# Перевод евро в доллары (курс: 1 евро = 1.25 доллара)
dollars_count = euros_count * 1.25
print(dollars_count)

# Перевод долларов в юани (курс: 1 доллар = 6.91 юаня)
yuans_count = dollars_count * 6.91
print(yuans_count)
# 5
first_name = 'Joffrey'
greeting = 'Hello'
info = 'Here is important information about your account security.'
intro = 'We couldn\'t verify your mother\'s maiden name.'

# Вывод заголовка
print(f"{greeting}, {first_name}!")

# Вывод тела письма
print(f"{info}\n{intro}")
# 6
frist_num = 20
second_num = -100
print(frist_num*second_num)
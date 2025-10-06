try:
    int(input())
    # 6 / 0
except ValueError as e:
    print(f"Ошибка: {e} ValueError")
except Exception as e:
    print(f"Ошибка: {e}")
else:
    print('ошибок нет')
finally:
    print('освобождение ресурсов')
from user_interface import show_all, add_new_animal, add_command


i = 0
while i < 10:
    add_new_animal()
    i += 1

add_command(5, "Игого", "Что-то Игого")
add_command(0, "Мяу", "Гав")
add_command(6, "Трололо", "Уляля")
print(show_all())

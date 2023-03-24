from user_commands import show_all, add_new_animal_random, add_command, all_animals, add_new_animal


def start_registry():
    print('*** Добро пожаловать в програму реестр домашних животных! *** \n')
    while True:
        program = input(str(f'{"*" * 40} \n             Вы в меню\n {"*" * 40} \n'
                            f'{"-" * 15}Введите{"-" * 15}\n'
                            f'1 - Внести в реестр рандомный список животных\n'
                            f'2 - Внести в реестр совое животное\n'
                            f'3 - Обучить животное команде\n'
                            f'4 - Показать всех животных\n'
                            f'5 - Выйти\n'                            
                            f'Вводите сюда --->: '))
        menu = {
            '1': 'start',
            '2': 'add',
            '5': 'quit',
            '4': 'show_all',
            '3': 'learn_animal'
        }

        try:
            program = menu[program]
            if program == 'quit':
                exit(0)
            elif program == 'start':
                add_new_animal_random()
                print(f'{"-" * 15}\nЖивотные добавлены в реестр!\n{"-" * 15}')
                show_all()
            elif program == 'add':
                add_new_animal()
                print(f'{"-" * 15}\nЖивотное добавлено в реестр!\n{"-" * 15}')
            elif program == 'show_all':
                show_all()
            elif program == 'learn_animal':
                if show_all is None:
                    print('Еще не записано ни одно животное!')
                else:
                    print(show_all())
                    id_param = int(input('Введите id животного которому вы хотите добавить команду: '))
                    key_type = input('Введите название команды: ')
                    val_type = input('Введите результат команды: ')
                    add_command(id_param, key_type, val_type)
                    print(f'Команда "{key_type}" добавлена для животного - {all_animals[id_param - 1]}')
        except KeyError:
            print('Введено неверное значение, возврат в меню!')

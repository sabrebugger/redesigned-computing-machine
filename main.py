import random

def guess_number():
    # Генерируем случайное число от 1 до 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    
    while True:
        try:
            # Пользователь вводит свою догадку
            guess = int(input("Введите вашу догадку (от 1 до 100): "))
            
            # Увеличиваем количество попыток
            attempts += 1
            
            if guess < secret_number:
                print("Загаданное число больше вашей догадки.")
            elif guess > secret_number:
                print("Загаданное число меньше вашей догадки.")
            else:
                print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
                break
        except ValueError:
            print("Ошибка: Введите число от 1 до 100.")

if __name__ == "__main__":
    print("Добро пожаловать в игру 'Угадай число'!")
    guess_number()

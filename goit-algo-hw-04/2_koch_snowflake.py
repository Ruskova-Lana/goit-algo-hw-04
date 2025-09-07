import turtle

def koch_curve(t, length, level):
    """Рекурсивне малювання кривої Коха"""
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def koch_snowflake(t, length, level):
    """Малювання сніжинки Коха (3 криві)"""
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

if __name__ == "__main__":
    # 1. Користувач вводить рівень рекурсії
    level = int(input("Введіть рівень рекурсії (0-6): "))

    # 2. Налаштування вікна
    screen = turtle.Screen()
    screen.title("Сніжинка Коха")

    # 3. Налаштування «черепашки»
    t = turtle.Turtle()
    t.speed(0)  # максимальна швидкість

    # 4. Малювання фракталу
    koch_snowflake(t, 300, level)

    # 5. Очікування закриття
    screen.mainloop()

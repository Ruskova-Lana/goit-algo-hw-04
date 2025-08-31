import queue
import time
import random

# Створюємо чергу заявок
requests_queue = queue.Queue()

# Лічильник для унікальних заявок
request_id = 0

def generate_request():
    """
    Генерація нової заявки з унікальним ID та додавання її до черги
    """
    global request_id
    request_id += 1
    request = f"Request-{request_id}"
    requests_queue.put(request)
    print(f"[+] Нова заявка створена і додана до черги: {request}")

def process_request():
    """
    Обробка заявки з черги (якщо черга не пуста)
    """
    if not requests_queue.empty():
        request = requests_queue.get()
        print(f"[~] Обробляється заявка: {request}")
        time.sleep(random.uniform(0.5, 1.5))  # імітація часу обробки
        print(f"[✓] Заявка {request} успішно оброблена")
    else:
        print("[!] Черга пуста, немає заявок для обробки")

def main():
    """
    Основний цикл програми: генеруємо і обробляємо заявки
    """
    print("Система обробки заявок запущена.")
    print("Для зупинки програми натисніть Ctrl+C (у терміналі / консолі).\n")  # <--- Коментар для користувача
    
    try:
        while True:
            # Генеруємо випадкову кількість нових заявок (0–2 за раз)
            for _ in range(random.randint(0, 2)):
                generate_request()

            # Обробляємо одну заявку (якщо є)
            process_request()

            # Невелика пауза для наочності
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Програму зупинено користувачем.")

if __name__ == "__main__":
    main()


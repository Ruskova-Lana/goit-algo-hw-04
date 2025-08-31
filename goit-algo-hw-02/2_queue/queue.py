from collections import deque

def is_palindrome(s: str) -> bool:
    # Видаляємо пробіли та приводимо до нижнього регістру
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    # Додаємо символи до двосторонньої черги
    dq = deque(cleaned)
    
    # Порівнюємо символи з обох кінців
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

# Приклади використання
examples = [
    "А роза упала на лапу Азора",
    "level",
    "hello",
    "Madam In Eden, I'm Adam"
]

for text in examples:
    print(f"'{text}' -> {is_palindrome(text)}")
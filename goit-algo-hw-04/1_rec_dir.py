import os
import shutil
import argparse


def move_files_recursively(src_dir, dest_dir):
    """
    Рекурсивно переміщує файли з src_dir у dest_dir,
    розкладаючи їх по піддиректоріях за розширенням.
    """
    try:
        for entry in os.scandir(src_dir):
            if entry.is_dir():
                # Якщо директорія — рекурсивно обходимо її
                move_files_recursively(entry.path, dest_dir)
            elif entry.is_file():
                # Беремо розширення
                _, ext = os.path.splitext(entry.name)
                # Якщо немає розширення, кладемо у "no_ext"
                ext = ext[1:].lower() if ext else "no_ext"

                # Шлях до підпапки для цього розширення
                ext_dir = os.path.join(dest_dir, ext)

                # Створюємо піддиректорію, якщо її ще нема
                os.makedirs(ext_dir, exist_ok=True)

                # Формуємо шлях для нового файлу
                dest_file = os.path.join(ext_dir, entry.name)

                try:
                    shutil.move(entry.path, dest_file)
                    print(f"Moved: {entry.path} -> {dest_file}")
                except Exception as e:
                    print(f"Помилка переміщення {entry.path}: {e}")
    except Exception as e:
        print(f"Помилка доступу до директорії {src_dir}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Рекурсивне переміщення файлів з сортуванням за розширенням."
    )
    parser.add_argument("src", help="Шлях до вихідної директорії")
    parser.add_argument(
        "dest",
        nargs="?",
        default="dist",
        help="Шлях до директорії призначення (за замовчуванням: dist)",
    )

    args = parser.parse_args()

    src_dir = args.src
    dest_dir = args.dest

    if not os.path.exists(src_dir):
        print(f"Помилка: директорія '{src_dir}' не існує.")
        return

    os.makedirs(dest_dir, exist_ok=True)

    move_files_recursively(src_dir, dest_dir)


if __name__ == "__main__":
    main()

import psycopg2
import csv
from tabulate import tabulate

# Прямая функция подключения
def connect():
    return psycopg2.connect(
        host="localhost",
        dbname="lab10",
        user="postgres",
        password="Sql1234",
        port=5432
    )

# 1. Поиск по шаблону (имя, фамилия, телефон)
def search_pattern(pattern: str):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
            return cur.fetchall()

# 2. Добавить или обновить пользователя
def upsert_user(name: str, surname: str, phone: str):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_user(%s, %s, %s)", (name, surname, phone))
    print(f"User {name} {surname} -> {phone} upserted.")

# 3. Массовая вставка
def bulk_insert(names, surnames, phones):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL bulk_insert_users(%s, %s, %s)", (names, surnames, phones))
    print("Bulk insert completed. Check server for invalid entries.")

# 4. Постраничный просмотр
def paginated_view(limit: int, offset: int):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM paginate_phonebook(%s, %s)", (limit, offset))
            return cur.fetchall()

# 5. Удаление по шаблону
def delete_by_name_or_phone(pattern: str):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_by_name_or_phone(%s)", (pattern,))
    print(f"Records matching '{pattern}' deleted.")

# Вставка одного пользователя
def insert_from_console():
    name = input("Name: ")
    surname = input("Surname: ")
    phone = input("Phone: ")
    upsert_user(name, surname, phone)

# Загрузка из CSV
def insert_from_csv(path: str):
    names, surnames, phones = [], [], []
    with open(path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 3:
                names.append(row[0])
                surnames.append(row[1])
                phones.append(row[2])
    bulk_insert(names, surnames, phones)

# Показать всю таблицу
def query_all():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook ORDER BY user_id")
            return cur.fetchall()

# Меню
def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Insert single user (console)")
        print("2. Bulk insert from CSV")
        print("3. Upsert user manually")
        print("4. Search by pattern")
        print("5. View paginated")
        print("6. Delete by name or phone")
        print("7. Show all")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv(input("CSV file path: "))
        elif choice == '3':
            upsert_user(input("Name: "), input("Surname: "), input("Phone: "))
        elif choice == '4':
            result = search_pattern(input("Pattern: "))
            print(tabulate(result, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
        elif choice == '5':
            try:
                limit = int(input("Limit: "))
                offset = int(input("Offset: "))
                result = paginated_view(limit, offset)
                print(tabulate(result, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
            except ValueError:
                print("Limit and offset must be integers.")
        elif choice == '6':
            delete_by_name_or_phone(input("Enter name, surname, or phone to delete: "))
        elif choice == '7':
            result = query_all()
            print(tabulate(result, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Запуск программы
if __name__ == "__main__":
    menu()
def total_salary(path: str):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            salary_list = []
            total = 0

            for line in lines:
                parts = line.split(',')
                if len(parts) > 1:
                    number = parts[1].strip()
                    if number.isdigit():
                        salary_list.append(int(number))
                        total += int(number)

            if len(salary_list) == 0:
                return 0, 0 

            average = int(total / len(salary_list))
            return total, average

    except FileNotFoundError:
        return "Не вдалося знайти файл", None  
    
total, average = total_salary("./task_1_data.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

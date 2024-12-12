def get_cats_info(path: str):
  try:
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        cats_list = []

        for line in lines:
            parts = line.split(',')
            if len(parts) > 1:
                cat_data = {
                    "id": parts[0] if parts[0] else "",
                    "name": parts[1] if parts[1] else "",
                    "age": parts[2].strip() if parts[2] else ""
                }
                cats_list.append(cat_data)
        return cats_list

  except FileNotFoundError:
        return "Не вдалося знайти файл", None  

cats_info = get_cats_info("./task_2_data.txt")
print(cats_info)


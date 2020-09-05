# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
def reading_data(file_name = "data.json"):
    import json
    with open(file_name, "r", encoding="utf-8") as file:
        new_file = json.load(file)
    return new_file

##############################################################################################

# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Рене Декарта фамилия это Декарт, у Пьера де Ферма - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
def _sort_key_name(value):
    if value["name"][-1] == " ":
        result = value["name"].split(" ")[-2]
    else:
        result = value["name"].split(" ")[-1]
    return result
def name_sorted_function(file_name = "data.json"):
    my_list = reading_data(file_name)
    new_list = sorted(my_list, key=_sort_key_name)
    return new_list

##############################################################################################

# 3. Написать функцию сортировки по дате смерти из поля "лет".
# Обратите внимание на сокращение BC. - это означает до н.э.
def compute(age, my_bool):
    import re
    new_age = re.findall(r'[0-9] {,4}', age)
    str_age = ""
    for symbol in new_age:
        str_age += symbol
    int_age = int(str_age)
    if my_bool:
        int_age = int_age * -1
    return int_age
def _sort_key_age(value):
    my_bool = False
    if "years" in value.keys():
        age1, age2 = value["years"].split("-")
        if value["years"].find("BC") != -1:
            my_bool = True
    age1 = compute(age1, my_bool)
    if age2.find("BC") == -1:
        my_bool = False
    age2 = compute(age2, my_bool)
    result = max(age1, age2)
    return result
def age_sorted_function():
    my_list = reading_data()
    new_list = sorted(my_list, key=_sort_key_age)
    return new_list

##############################################################################################

# 4. Написать функцию сортировки по количеству слов в поле "text"
def _sort_key_len_word(value):
    if "text" in value.keys():
        my_list = value["text"].split(" ")
    my_symbol = my_list.count("")
    if my_symbol :
        for index in range(my_symbol):
            my_list.remove("")
    result = len(my_list)
    return result
def len_word_sorted_function():
    my_list = reading_data()
    new_list = sorted(my_list, key=_sort_key_len_word)
    return new_list

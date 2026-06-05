History = "Здравия желаю, я как понял ты новый работник нашей организации O.O.P.S.\nи ближайщие 10 дней ты будешь выполнять задачи что тебе будут приходить.Давай я тебе озвучу твои их .\nБудь осторожен ведь кто знает что ты встретишь."
laptop_documentation = ["[1]Save objects", "[2]Странные обьекты", "[3]Обьекты класса удержания", "[4]O.O.P.S objects", "[5]<--EXIT"]
rules = ["[1]Будь внимателен","[2]Смотри на детали", "[3]Принимай максимально взвешанное решение", "[X]EXIT"]

messages_safe = {1: "Пропавшие обьекты", 2: "Резкое похолодание", 3: "Странные звуки",
                 4: "Красная луна", 5: "Перевёрнутые деревья", 6: "Странное поведение животных",
                 7: "Раздраженные люди", 8: "Помехи линий связи", 9: "Не рабочий фонарь", 10: "Неопозннаный запах"}
messages_str = {1: "11", 2: "12", 3: "13", 4: "14", 5: "15", 6: "16", 7: "17", 8: "18", 9: "19", 10: "20"}
messages_ocs = {1: "1", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: ""}
messages_OOPS = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: ""}
messages_names = ("messages_safe", "messages_str", "messages_ocs", "messages_OOPS")

city_places = ["sector_1a", "sector_2a", "sector_3a", "sector_4a", "sector_5a",
               "sector_1b", "sector_2b", "sector_3b", "sector_4b", "sector_5b",
               "sector_1c", "sector_2c", "sector_3c", "sector_4c", "sector_5c",
               "sector_1d", "sector_2d", "sector_3d", "sector_4d", "sector_5d",
               "city_center", "Hospital", "Police", "Your_base", "[X]EXIT"]

Oopy_help_list = ["/helpy", "/printo", "/inputo", "/function base", "/debug_menu", "/exit"]
Oopy_function_description = ["Список всех функций что вы можете написать", "Вывод текста на экран: /printo(Text here)",
                             "Позволяет вводить в консоль данные: /inputo(Pr) after Pr = /printo(Enter what is text be in Pr",
                             "Вывод всей информации про функции", "Среда для программирования", "Выход"]
Oopy_input_message = ["Здравия желаю! Моё имя [O.O.P.Y]. Готов помочь в любую минуту... [/helpy]<-- Для просмотра всех функций"]

workbench_main = ["[1]Laptop", " [2]Messages", "  [3]Game Boy"]
workbench_main_with_message = ["[1]Laptop", " [2]Messages-!1!", "  [3]Game Boy"]
laptop_main = ["[1]Documentation", "[2]Rules", "[3]Cities_map", "[4]O.O.P.Y", "[5]News", "[X]EXIT"]

Game_boy_main = ["[1]Snake", "[2]Car road simulator[CRS]", "[3]Cyberpank2077"]

city_place_message_save = {"sector_1a": [], "sector_2a": [], "sector_3a": [], "sector_4a": [], "sector_5a": [],
               "sector_1b": [], "sector_2b": [], "sector_3b": [], "sector_4b": [], "sector_5b": [],
               "sector_1c": [], "sector_2c": [], "sector_3c": [], "sector_4c": [], "sector_5c": [],
               "sector_1d": [], "sector_2d": [], "sector_3d": [], "sector_4d": [], "sector_5d": [],
               "city_center": [], "Hospital": [], "Police": [], "Your_base": []}

city_place_distance = {"Your_base": {"Police": 30},
                       "Police": {"Hospital": 10, "sector_3d": 20},
                       "Hospital": {"city_center": 20, "sector_2d": 20},
                       "sector_5d": {"sector_4d": 15, "sector_5c": 25},
                       "sector_4d": {"sector_3d": 15, "sector_4c": 25},
                       "sector_3d": {"sector_2d": 15, "sector_3c": 25},
                       "sector_2d": {"sector_1d": 15, "sector_2c": 25},
                       "sector_1d": {"sector_1c": 25},
                       "sector_5c": {"sector_4c": 10, "sector_5b": 20},
                       "sector_4c": {"sector_3c": 10, "sector_4b": 20},
                       "sector_3c": {"sector_2c": 10, "sector_3b": 20},
                       "sector_2c": {"sector_1c": 10, "sector_2b": 20},
                       "sector_1c": {"sector_1b": 20},
                       "sector_5b": {"sector_4b": 15, "sector_5a": 25},
                       "sector_4b": {"sector_3b": 15, "sector_4a": 25},
                       "sector_3b": {"sector_2b": 15, "sector_3a": 25},
                       "sector_2b": {"sector_1b": 15, "sector_2a": 25},
                       "sector_1b": {"sector_1a": 25},
                       "sector_5a": {"sector_4a": 15},
                       "sector_4a": {"sector_3a": 15},
                       "sector_3a": {"sector_2a": 15},
                       "sector_2a": {"sector_1a": 15},
                       "sector_1a": {"Another_city": 12500}
                       }

creatures_names = {"police": [100, 10, 15, 0], "Trained_police": [120, 10, 25, 0], "Soldier": [150, 12, 35, 5],
                   "Special_soldier": [200, 8, 50, 20], "O.O.P.E.R.S": [1000, 5, 100, 100]}
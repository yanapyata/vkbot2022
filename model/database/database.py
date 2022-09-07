import sqlalchemy


class DataBase:
    """Класс для работы с запросами к БД"""
    def __init__(self, db):
        self.db = db
        self.engine = sqlalchemy.create_engine(self.db)
        self.connection = self.engine.connect()

    def insert_users(self, users_ids):
        """Добавление юзеров в БД"""
        self.connection.execute(f"INSERT INTO Users (id, users_id) VALUES (DEFAULT, {users_ids});")

    def select_users(self, event):
        """Извлечение юзеров из БД"""
        result_dict = dict()
        result_db = self.connection.execute("select * from Users").fetchall()
        for item in result_db:
            result_dict[item[1]] = item[0]

        if result_dict.get(event.user_id):
            result = result_dict.get(event.user_id)
            return result
        else:
            self.insert_users(event.user_id)

    def select_users_lists(self, table_name):
        """Извлечение списков избранное и черный и получение id"""
        result_db = self.connection.execute(f"select * from {table_name}").fetchall()
        result = list()
        for item in result_db:
            result.append(item[1])
        return result

    def select_advanced_search(self, user_id):
        """Получение рассширенного поиска или поиска по пареметрам и взятие от туда id"""
        if user_id is not None:
            result_db = self.connection.execute(f"select * from advancedsearch where id_users={user_id};").fetchall()
            if len(result_db) != 0:
                result = list()
                for item in result_db:
                    if item[-1] == user_id:
                        result.append(item)
                return result[-1]

    def select_list(self, db_name, table_name, user_id):
        """Получение 10 последних забисей из Избранных и Черных списков"""
        result_db = self.connection.execute(
            f"select {table_name} from {db_name} where id_users={user_id} order by id desc limit 10;").fetchall()
        if len(result_db) != 0:
            result = list()
            for item in result_db:
                result.append(item[0])
            return result

    def delete_advanced_search(self, user_id):
        """Удаление по id пользователя данных по поиску по параметрам"""
        result = self.connection.execute(f"delete from advancedsearch where id_users={user_id}")
        return result

    def insert_users_like_list(self, users_like, id_users):
        """Добавление данных в таблицу Избранный список"""
        self.connection.execute(
            f"INSERT INTO Userslikelist (id, users_like, id_users) VALUES (DEFAULT, {users_like}, {id_users})")

    def insert_users_black_list(self, users_black, id_users):
        """Добавление данных в таблицу Черный список"""
        self.connection.execute(
            f"INSERT INTO Usersblacklist (id, users_black, id_users) VALUES (DEFAULT, {users_black}, {id_users})")

    def insert_advanced_search(self, city, age_from, age_to, user_sex, user_status, id_users):
        """Добавление данных в динамическую таблицу с поиском по параметрам"""
        self.connection.execute(
            f"INSERT INTO advancedsearch (id,city,age_from,age_to,user_sex,user_status,id_users) VALUES "
            f"(DEFAULT, '{city}', {age_from}, {age_to}, {user_sex}, {user_status}, {id_users});")

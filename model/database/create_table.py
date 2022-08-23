    def __init__(self, db):
        self.connections = self.engine.connect()

    def create_table(self):
        """создание таблиц в БД"""
        self.connections.execute(
            "create table if not exists Users (id serial primary key, users_id integer unique not null);")
        self.connections.execute("create table if not exists UsersLikeList (id serial primary key, "

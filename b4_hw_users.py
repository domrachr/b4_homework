import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# базовый класс моделей таблиц
Base = declarative_base()

class User(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    __tablename__ = 'user'
    id = sa.Column(sa.INTEGER, primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.DATE)
    height = sa.Column(sa.REAL)

def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    # выводим приветствие
    print("Добавляем в базу нового пользователя")
    # запрашиваем у пользователя данные
    first_name = input("Введи имя: ")
    last_name = input("Введи фамилию: ")
    gender = input("Введи пол (Male/Female): ")
    email = input("Введи адрес электронной почты: ")
    birthdate = input("Введи дату рождения: ")
    height = float(input("Введи рост (в сантиметрах): "))/100
    # создаем нового пользователя
    user = User(
        first_name = first_name,
        last_name = last_name,
        gender = gender,
        email = email,
        birthdate = birthdate,
        height = height
    )
    # возвращаем созданного пользователя
    return user

def connect_db(db_path):
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(db_path)
    # создаем описанные таблицы
    Base.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()

def main():
    session = connect_db("sqlite:///sochi_athletes.sqlite3")
    while True:
        mode = input("Выбери режим.\n1 - ввести данные нового пользователя\n2 - выйти\n")    
        if mode=="1":
            user = request_data()
            session.add(user)
            session.commit()
            print("Спасибо, данные сохранены!")
        elif mode=="2":
            break
if __name__ == "__main__":
    main()
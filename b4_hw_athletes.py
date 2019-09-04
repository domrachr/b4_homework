from datetime import datetime as dt
from b4_hw_users import *

class Athelete(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    __tablename__ = 'athelete'
    id = sa.Column(sa.INTEGER, primary_key=True)
    age = sa.Column(sa.INTEGER)
    birthdate = sa.Column(sa.DATE)
    gender = sa.Column(sa.Text)
    height = sa.Column(sa.REAL)
    name = sa.Column(sa.Text)
    weight = sa.Column(sa.INTEGER)
    gold_medals = sa.Column(sa.INTEGER)
    silver_medals = sa.Column(sa.INTEGER)
    bronze_medals = sa.Column(sa.INTEGER)
    total_medals = sa.Column(sa.INTEGER)
    sport = sa.Column(sa.Text)
    country = sa.Column(sa.Text)
    
    

def find_athelet1(user, session):
    atheletes = session.query(Athelete).all()
    MinHeightDelta = None
    MinHeightDeltaAthelete = None
    for athelete in atheletes:
        if athelete.height is None:
            continue
        HeightDelta = abs(user.height - athelete.height)
        if MinHeightDelta is None:
            MinHeightDelta = HeightDelta
            MinHeightDeltaAthelete = athelete
        elif HeightDelta < MinHeightDelta:
            MinHeightDelta = HeightDelta
            MinHeightDeltaAthelete = athelete
    return "id:{} Name:{} Height:{}".format(MinHeightDeltaAthelete.id, MinHeightDeltaAthelete.name, MinHeightDeltaAthelete.height)

def find_athelet2(user, session):
    atheletes = session.query(Athelete).all()
    MinBDDelta = None
    MinBDDeltaAthelete = None
    for athelete in atheletes:
        if athelete.birthdate is None:
            continue
        BDDelta = abs(user.birthdate - athelete.birthdate)
        if MinBDDelta is None:
            MinBDDelta = BDDelta
            MinBDDeltaAthelete = athelete
        elif BDDelta < MinBDDelta:
            MinBDDelta = BDDelta
            MinBDDeltaAthelete = athelete
    return "id:{} Name:{} Birthdate:{}".format(MinBDDeltaAthelete.id, MinBDDeltaAthelete.name, MinBDDeltaAthelete.birthdate)

def main():
    session = connect_db("sqlite:///sochi_athletes.sqlite3")
    while True:
        mode = input("Выбери режим.\n1 - Подобрать атлета\n2 - выйти\n")    
        if mode=="1":
            id = int(input("Введи id пользователя: "))
            query = session.query(User).filter(User.id == id)
            if query.count():
                print("Один из подходящих по росту атлетов:")
                print(find_athelet1(query[0],session))
                print("Один из подходящих по дате рождения атлетов:")
                print(find_athelet2(query[0],session))
            else:
                print("Пользователь с таким id не найден")
                continue    
        elif mode=="2":
            break

if __name__ == "__main__":
    main()
import data_base_init as db


def insert_row(personal_info):
    try:
        db.curs.executemany("INSERT INTO personal VALUES(null, ?, ?, ?, ?, ?)", personal_info)
        db.d_base.commit()
        return True
    except:
        return False


def select_row_by_id(name_id):
    try:
        db.curs.execute(f'SELECT * FROM personal WHERE id={name_id};')
        res = db.curs.fetchone()
        print(*res)
        return True
    except:
        return False


def select_row_by_somename_str(name, value):
    try:
        db.curs.execute(f'SELECT * FROM personal WHERE {name} LIKE "{value}";')
        res = db.curs.fetchall()
        print(res)
        return True
    except:
        return False


def delete_row_by_id(name_id):
    try:
        db.curs.execute(f'DELETE FROM personal WHERE ID={name_id};')
        db.d_base.commit()
        return True
    except:
        return False


def delete_row_by_somename_str(name, value):
    try:
        db.curs.execute(f'DELETE FROM personal WHERE {name} LIKE "{value}";')
        db.d_base.commit()
        return True
    except:
        return False


def clear_table():
    db.curs.execute('DELETE FROM personal;')
    db.d_base.commit()
    print(f'Таблица очищена. Удалено {db.curs.rowcount} строк. ')
    
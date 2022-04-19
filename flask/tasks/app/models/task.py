from datetime import datetime

# Class to model Task objects
class Task:
    def __init__(self, description):
        self._description = description
        self._creation_datetime = datetime.now()
        self._completed = 0
    

    @property
    def description(self):
        return self._description
    

    @description.setter
    def description(self, new_description):
        self._description = new_description
    

    @property
    def completed(self):
        return bool(self._completed)
    

    @completed.setter
    def completed(self, complete):
        if not 0 <= complete <= 1:
            raise ValueError(f"A complete task value must be 1 or 0. Received {complete}")
        self._completed = bool(complete)
    

    @property
    def creation_datetime(self):
        return self._creation_datetime


# Class to support reading/writing Task objects with the database
class TaskDB:
    def __init__(self, db_conn, db_cursor):
        self._db_conn = db_conn
        self._cursor = db_cursor
    

    def select_all_tasks(self):
        select_all_query = """
            SELECT * from tasks;
        """
        self._cursor.execute(select_all_query)

        return self._cursor.fetchall()


    def select_all_tasks_by_description(self, description):
        select_tasks_by_description = """
            SELECT * from tasks WHERE description LIKE %s;
        """
        self._cursor.execute(select_tasks_by_description, (f"%{description}%",))
        return self._cursor.fetchall()
    

    def select_task_by_id(self, task_id):
        select_task_by_id = """
                SELECT * from tasks WHERE id = %s;
        """
        self._cursor.execute(select_task_by_id, (task_id,))
        return self._cursor.fetchall()


    def insert_task(self, task):
        insert_query = """
            INSERT INTO tasks (description, creation_datetime, completed)
            VALUES (%s, %s, %s);
        """

        self._cursor.execute(insert_query, (task.description, task.creation_datetime, task.completed))
        self._cursor.execute("SELECT LAST_INSERT_ID() task_id")
        task_id = self._cursor.fetchone()
        self._db_conn.commit()
        return task_id


    def update_task(self, task_id, new_task):
        update_query = """
            UPDATE tasks
            SET description=%s
            WHERE id=%s;
        """
        self._cursor.execute(update_query, (new_task.description, task_id))
        self._db_conn.commit()

    def delete_task_by_id(self, task_id):
        delete_query = """
            DELETE from tasks
            WHERE id=%s;
        """
        self._cursor.execute(delete_query, (task_id,))
        self._db_conn.commit()

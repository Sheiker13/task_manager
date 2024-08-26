from typing import List

class Task:
    """
    Класс, представляющий задачу.

    Атрибуты:
        title (str): Название задачи.
        description (str): Описание задачи.
    """
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description

class TaskManager:
    """
    Класс, управляющий списком задач.

    Атрибуты:
        __tasks (List[Task]): Закрытый список задач пользователя.
    """
    def __init__(self):
        # Инициализация закрытого атрибута для хранения задач.
        self.__tasks = []

    def add_task(self, title: str, description: str) -> None:
        """
        Добавляет новую задачу в список задач.

        Параметры:
            title (str): Название задачи.
            description (str): Описание задачи.
        """
        task = Task(title, description)
        self.__tasks.append(task)

    @property
    def tasks(self) -> List[Task]:
        """
        Возвращает копию списка задач.

        Возвращаемое значение:
            List[Task]: Копия списка задач пользователя.
        """
        return self.__tasks.copy()

if __name__ == "__main__":
    task_manager = TaskManager()


    while True:
        title = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")


        task_manager.add_task(title, description)


        another = input("Хотите добавить еще одну задачу? (да/нет): ").strip().lower()
        if another != 'да':
            break


    tasks = task_manager.tasks
    for idx, task in enumerate(tasks, start=1):
        print(f"Задача {idx}: {task.title} - {task.description}")

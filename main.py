from typing import List


class Task:
    def __init__(self, title: str, description: str) -> None:
        # Инкапсулируем атрибуты задачи, делая их закрытыми
        self.__title = title
        self.__description = description

    # Предоставляем только доступ для чтения через свойства
    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description


class TaskManager:
    def __init__(self):
        # Инициализация закрытого атрибута для хранения задач
        self.__tasks: List[Task] = []

    # Метод для добавления задачи, доступ извне
    def add_task(self, title: str, description: str) -> None:
        task = Task(title, description)
        self.__tasks.append(task)

    # Свойство, предоставляющее доступ к копии списка задач
    @property
    def tasks(self) -> List[Task]:
        return self.__tasks.copy()

    # Метод для удаления задачи по индексу (если нужно)
    def remove_task(self, index: int) -> None:
        if 0 <= index < len(self.__tasks):
            del self.__tasks[index]
        else:
            raise IndexError("Задача с таким индексом не существует.")


if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        title = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")

        task_manager.add_task(title, description)

        another = input("Хотите добавить еще одну задачу? (да/нет): ").strip().lower()
        if another != 'да':
            break

    # Выводим задачи
    tasks = task_manager.tasks
    for idx, task in enumerate(tasks, start=1):
        print(f"Задача {idx}: {task.title} - {task.description}")

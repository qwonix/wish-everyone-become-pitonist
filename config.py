from os.path import exists as file_exists, join as path_join
from json import dumps as json_dumps, load as json_loads


# Класс для работы с key-value файлами json
class Config:
    filename: str
    data: dict = {}

    def __init__(self, working_directory: str, file: str):
        filename = path_join(working_directory, file)
        if not file_exists(filename):
            open(filename, "w+").write(json_dumps({}))

        self.filename = filename
        self.data = json_loads(open(filename, "r+"))

    def exists(self, key: str):
        try:
            self.try_get(key)
            return True
        except KeyError:
            return False

    def try_get(self, key: any):
        return self.data[key]

    def set(self, key: str, value: any):
        self.data[key] = value

    def save(self):
        open(self.filename, "w+").write(json_dumps(self.data, indent=4))

import os
import tempfile


class File:

    def __init__(self, path):
        self.path = path
        if not os.path.exists(self.path):
            print(f"Файла, расположенного по пути {self.path}, не существует. Создание нового файла...")
            self.write("")

    def __add__(self, other):
        filename = tempfile.mkstemp()[1]
        with open(filename, 'w') as f:
            file1_content = self.read()
            file2_content = other.read()
            f.write(file1_content+"\n"+file2_content)
            return File(filename)

    def __iter__(self):
        with open(self.path, 'r') as f:
            return iter(f.readlines())

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def write(self, string):
        with open(self.path, 'w') as f:
            f.write(string)
            return len(string)

    def __str__(self):
        return str(self.path)

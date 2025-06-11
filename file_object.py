import os

def ansi_color_text(text: str, color: str) -> str:
    colors = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "reset": "\033[0m"
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"

def deco(color: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                return ansi_color_text(result, color)
            return result
        return wrapper
    return decorator

class FileObject:
    def __init__(self, filepath: str):
        self._filepath = filepath

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, value):
        if not os.path.isfile(value):
            raise ValueError("File does not exist.")
        self._filepath = value

    @staticmethod
    def is_text_file(filepath):
        return filepath.endswith('.txt')

    @classmethod
    def from_directory(cls, dirpath):
        for fname in os.listdir(dirpath):
            if fname.endswith('.txt'):
                yield cls(os.path.join(dirpath, fname))

    def _generator(self):
        with open(self._filepath, 'r', encoding='utf-8') as f:
            for line in f:
                yield line.rstrip('\n')

    def lines(self):
        return (line for line in self._generator())

    def __str__(self):
        return f"FileObject({self._filepath})"

    def __add__(self, other):
        if not isinstance(other, FileObject):
            return NotImplemented
        new_path = f"{self._filepath}_concat_{os.path.basename(other._filepath)}"
        with open(new_path, 'w', encoding='utf-8') as fout:
            fout.writelines([line + '\n' for line in self.lines()])
            fout.writelines([line + '\n' for line in other.lines()])
        return FileObject(new_path)

    def read_all(self):
        return ''.join([line + '\n' for line in self.lines()])

class AdvancedFileObject(FileObject):
    @deco("cyan")
    def read_colored(self):
        return self.read_all()

    def concat_many(self, *file_objs):
        new_path = f"{self._filepath}_concat_many"
        with open(new_path, 'w', encoding='utf-8') as fout:
            fout.writelines([line + '\n' for line in self.lines()])
            for fobj in file_objs:
                fout.writelines([line + '\n' for line in fobj.lines()])
        return AdvancedFileObject(new_path)

    @deco("magenta")
    def __str__(self):
        return super().__str__()
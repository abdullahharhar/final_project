from file_object import FileObject, AdvancedFileObject

file = AdvancedFileObject("example.txt")
print(file.read_colored())  # Colored output
print(file)  # Colored string representation

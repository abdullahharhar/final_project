from file_object import AdvancedFileObject, ansi_color_text

file1 = AdvancedFileObject("example.txt")
file2 = AdvancedFileObject("example2.txt")
file3 = AdvancedFileObject("example3.txt")

label1 = ansi_color_text("----- First Text (example.txt) -----\n", "red")
label2 = ansi_color_text("----- Second Text (example2.txt) -----\n", "blue")
label3 = ansi_color_text("----- Third Text (example3.txt) -----\n", "magenta")

text1 = ansi_color_text(file1.read_all(), "red")
text2 = ansi_color_text(file2.read_all(), "blue")
text3 = ansi_color_text(file3.read_all(), "magenta")

full_text = (
    label1 + text1 + "\n" +
    label2 + text2 + "\n" +
    label3 + text3
)

print(full_text)

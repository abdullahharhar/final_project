import os
import pytest
from file_object import FileObject, AdvancedFileObject, ansi_color_text

@pytest.fixture
def tmp_text_files(tmp_path):
    file1 = tmp_path / "example.txt"
    file2 = tmp_path / "example2.txt"
    file3 = tmp_path / "example3.txt"
    file1.write_text("hello\nworld")
    file2.write_text("foo\nbar")
    file3.write_text("baz\nqux")
    return str(file1), str(file2), str(file3)

def test_property_setter(tmp_text_files):
    f1, _, _ = tmp_text_files
    obj = FileObject(f1)
    assert obj.filepath == f1

def test_static_and_class_method(tmp_text_files, tmp_path):
    f1, _, _ = tmp_text_files
    assert FileObject.is_text_file(f1)
    files = list(FileObject.from_directory(str(tmp_path)))
    assert len(files) == 3

def test_generator_and_lines(tmp_text_files):
    f1, _, _ = tmp_text_files
    obj = FileObject(f1)
    lines = list(obj.lines())
    assert lines == ["hello", "world"]

def test_str_and_add(tmp_text_files):
    f1, f2, _ = tmp_text_files
    obj1 = FileObject(f1)
    obj2 = FileObject(f2)
    obj3 = obj1 + obj2
    with open(obj3.filepath, "r", encoding="utf-8") as f:
        content = f.read()
    assert "hello" in content and "foo" in content

def test_read_all(tmp_text_files):
    f1, _, _ = tmp_text_files
    obj = FileObject(f1)
    assert "hello" in obj.read_all()

def test_advanced_concat_many(tmp_text_files):
    f1, f2, f3 = tmp_text_files
    adv = AdvancedFileObject(f1)
    adv2 = AdvancedFileObject(f2)
    adv3 = AdvancedFileObject(f3)
    new_obj = adv.concat_many(adv2, adv3)
    text = new_obj.read_all()
    assert "hello" in text and "foo" in text and "baz" in text

def test_decorator_colored_output(tmp_text_files):
    f1, _, _ = tmp_text_files
    adv = AdvancedFileObject(f1)
    colored = adv.read_colored()
    assert "\033[" in colored

def test_str_colored(tmp_text_files):
    f1, _, _ = tmp_text_files
    adv = AdvancedFileObject(f1)
    s = str(adv)
    assert "\033[" in s

def test_ansi_color_text_coloring():
    text = "test"
    colored_red = ansi_color_text(text, "red")
    assert "\033[31m" in colored_red and text in colored_red
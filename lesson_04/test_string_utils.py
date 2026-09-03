from string_utils import StringUtils


utils = StringUtils()


def test_capitalize_pozitive():
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_negative():
    assert utils.capitalize("") == ""


def test_trim_pozitive():
    assert utils.trim(" skypro") == "skypro"


def test_trim_negative():
    assert utils.trim("skypro") == "skypro"


def test_contains_pozitive():
    assert utils.contains("skypro", "y") is True


def test_contains_negative():
    assert utils.contains("skypro", "d") is False


def test_delete_symbol_pozitive():
    assert utils.delete_symbol("skypro", "y") == "skpro"


def test_delete_symbol_negative():
    assert utils.delete_symbol("", "d") == ""

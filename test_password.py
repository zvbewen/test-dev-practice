import pytest

def validate_password(pwd):
    """校验密码：8-20 位，至少含有一个数字和一个字母。
    合法返回 True，否则抛ValueError。"""
    if not isinstance(pwd, str):
        raise ValueError("密码必须是字符串")
    if len(pwd) < 8:
        raise ValueError("密码太短，至少8位")
    if len(pwd) > 20:
        raise ValueError("密码太长，最多 20 位")

    has_digit = False
    has_alpha = False
    for c in pwd:
        if c.isdigit():
            has_digit = True
        if c.isalpha():
            has_alpha = True

    if not has_digit:
        raise ValueError("密码必须包含至少一位数字")
    if not has_alpha:
        raise ValueError("密码必须包含至少一位字母")
    return True

@pytest.mark.parametrize("a,expected",[
    ("123456abc",True),
    ("abc123456",True),
    ("ab123456c",True),
    ("123abc456",True),
    ("123456ab",True),
    ("123456789987654321ab",True),
    (123456789,"密码必须是字符串"),
    ("12345ab","密码太短，至少8位"),
    ("123456789987654321abc","密码太长，最多 20 位"),
    ("abcdefghi","密码必须包含至少一位数字"),
    ("123456789","密码必须包含至少一位字母"),

])
def test_validate_password(a,expected):
    if expected == True:
        assert validate_password(a) == True
    else:
        with pytest.raises(ValueError,match=expected):
            validate_password(a)
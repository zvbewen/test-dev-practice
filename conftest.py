def pytest_make_parametrize_id(config, val, argname):
    # 如果参数是字符串，直接返回原内容，不做转义
    if isinstance(val, str):
        return val
    # 其他类型走默认逻辑
    return None

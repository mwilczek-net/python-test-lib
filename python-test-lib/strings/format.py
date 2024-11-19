import inspect

def skip_indentation(s: str):
    return inspect.cleandoc(s)

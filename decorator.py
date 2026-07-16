# def check_int(func):
#     def wrapper(*args, **kwargs):
#         for i in args:
#             if not isinstance(i, int):
#                 raise TypeError("All arguments must be integers")
#         return func(*args, **kwargs)
#     return wrapper


# @check_int
# def add(a,b):
#     return a+b
# print(add(1,"2"))


def check_int(func):
    def wrapper(*args, **kwargs):
        for i in args:
            if not isinstance(i, int):
                raise TypeError("All arguments must be integers")
        return func(*args, **kwargs)
    return wrapper


@check_int
def add(a, b):
    return a + b

print(add(1, "2"))
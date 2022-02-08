"""
def hello_world():
    print("Hello world!")


def higher_order(func):
    print("Получена функция {} в качестве аргумента".format(func))
    func()
    return func


higher_order(hello_world)


def wrapper_function():
    def hello_world():
        print("Hello world!!!")
    hello_world()


wrapper_function()
"""


def decorator_function(func):
    def wrapper():
        print("Функция-обёртка!")
        print("Оборачиваемая функция: {}".format(func))
        print("Выполняем обёрнутую функцию...")
        func()
        print("Выходим из обёртки")

    return wrapper


@decorator_function
def hello_world():
    print("Hello world!")


def hello_world():
    print("Hello world!!!")


hello_world()


# def benchmark(func):
#     import time
#
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print("[*] Время выполнения: {} секунд.".format(end - start))
#
#     return wrapper
#
#
# @benchmark
# def fetch_webpage():
#     import requests
#
#     webpage = requests.get("https://google.com")
#
#
# fetch_webpage()


# def benchmark(func):
#     import time
#
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         return_value = func(*args, **kwargs)
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end - start))
#         return return_value
#
#     return wrapper
#
#
# @benchmark
# def fetch_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     return webpage.text
#
#
# webpage = fetch_webpage('https://google.com')
# print(webpage)

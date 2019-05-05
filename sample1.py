
# coding:utf-8

class TestClass:
    name = ""
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("こんにちは、" + self.name + "！")

test_class = TestClass("Python")
test_class.hello()

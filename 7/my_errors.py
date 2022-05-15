from abc import abstractmethod


class MyException(Exception):

    #хотелось бы, не иннициализировать поле code ничем вообще, а просто сказать, что оно будет у наследников
    #потому что эеземпляров класса MyException не будет в принципе, а обращаться к полю code хочется для общего случая
    #но чет я не придумал, как это сделать
    @abstractmethod
    def __init__(self):
        self.code = None


class EverythingIsOk(MyException):
    def __init__(self):
        self.code = 200


class Error404(MyException):
    def __init__(self):
        self.code = 404


class Error500(MyException):
    def __init__(self):
        self.code = 500


class Error666(MyException):
    def __init__(self):
        self.code = 666

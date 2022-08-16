
class CommonException(Exception):
    """公共异常类"""

    def __init__(self,enum_cls):
        self.code = enum_cls.code
        self.errmsg = enum_cls.errmsg
        self.enum_cls = enum_cls
        super().__init__()



class BusinessException(CommonException):
    pass

class APIException(CommonException):
    pass
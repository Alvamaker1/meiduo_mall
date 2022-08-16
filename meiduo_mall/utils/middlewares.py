from django.middleware.common import MiddlewareMixin
from django.http.response import JsonResponse, HttpResponseServerError
from django.db import DatabaseError
from .exceptions import BusinessException
from .enums import StatusCodeEnum
from .result import R


class ExceptionMiddleware(MiddlewareMixin):

    """统一异常处理中间件"""

    def process_exception(self, request, exception):

        """
        统一异常处理信息
        request : 请求对象
        exception: 异常对象
        """
        if isinstance(exception, BusinessException):
            data = R.set_result(exception.enum_cls).data()
            return JsonResponse(data)
        elif isinstance(exception, DatabaseError):
            r = R.set_result(StatusCodeEnum.DB_ERR)
            return HttpResponseServerError(StatusCodeEnum.SERVER_ERR.errmsg)
        elif isinstance(exception, Exception):
            r = R.server_error()
            return HttpResponseServerError(r.errmsg)
